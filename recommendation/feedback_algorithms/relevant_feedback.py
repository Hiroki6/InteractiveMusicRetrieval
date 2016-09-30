# -*- coding:utf-8 -*-

"""
印象語検索における適合性フィードバックによるモデルの学習
"""

import numpy as np
import redis
import common_functions as common
from RelevantFeedback import cy_relevant_feedback as cy_rf
import sys
from recommendation import models

HOST = 'localhost'
PORT = 6379
DB = 2

class RelevantFeedback:
    """
    適合性フィードバックによるオンライン学習クラス
    """
    def __init__(self, user, emotion):
        self.user = user
        self._get_params_by_redis()
        self.emotion = emotion
        self.cy_obj = cy_rf.CyRelevantFeedback(self.W, self.bias, 43)

    def _get_params_by_redis(self):
        self.r = common.get_redis_obj(HOST, PORT, DB)
        key =  "W_" + self.user
        self.W = common.get_one_dim_params(self.r, key)
        self.bias = common.get_scalar(self.r, "bias", self.user)

    def _get_learning_data(self, learning_method):
        """
        学習データの取得
        """
        relevant_datas = models.EmotionRelevantSong.objects.order_by("id").filter(user_id=int(self.user)).values()
        self.song_relevant = {} # {song_id: relevant_type}
        if learning_method == "online":
            relevant_datas = relevant_datas.reverse()
            self.song_relevant[relevant_datas[0]["song_id"]] = relevant_datas[0]["relevant_type"]
        else:
            for relevant_data in relevant_datas:
                self.song_relevant[relevant_data["song_id"]] = relevant_data["relevant_type"]

    def set_learning_params(self, l_rate, beta, learning_method = "online"):
        """
        学習パラメータの設定
        """
        self.beta = beta
        self.cy_obj.set_learning_params(l_rate, beta)
        self._get_learning_data(learning_method)
        self._set_listening_songs()

    def _set_listening_songs(self):

        self.songs, self.song_tag_map = common.get_listening_songs(self.user)

    def fit(self):
        """
        CyRelevantFeedbackクラスを用いたモデルの学習
        """
        error = 0
        for i in xrange(100):
            before_error = error
            for song_id, relevant_type in self.song_relevant.items():
                print "song_id: %d" % (song_id)
                self.cy_obj.fit(self.song_tag_map[song_id], relevant_type)
            error = self._calc_all_error()
            print error
            if error < 0.0001 or abs(error - before_error) < 0.000001:
                self.bias = self.cy_obj.get_bias()
                break

        self.update_params_into_redis()

    def _calc_all_error(self):

        error = 0.0
        for song_id, relevant_type in self.song_relevant.items():
            print "song_id: %d" % (song_id)
            error += pow(self.cy_obj.calc_error(self.song_tag_map[song_id], relevant_type), 2)
        error += self.beta * np.linalg.norm(self.W)

        return error

    def get_top_k_songs(self, k=1):
        """
        検索対象の印象語に含まれている楽曲から回帰値の高いk個の楽曲を取得する
        """
        songs, song_tag_map = common.get_not_listening_songs(self.user, self.emotion)
        top_song = 0
        top_song_value = -sys.maxint
        rankings = [(self.cy_obj.predict(tags), song_id) for song_id, tags in song_tag_map.items()]
        common.listtuple_sort_reverse(rankings)
        return rankings[:k]

    def update_params_into_redis(self):
        common.delete_redis_key(self.r, "W_"+self.user)
        common.save_one_dim_array(self.r, "W_" + self.user, self.W)
        common.save_scalar(self.r, "bias", self.user, self.bias)
