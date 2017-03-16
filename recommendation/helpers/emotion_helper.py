# -*- coding:utf-8 -*-
"""
印象語検索システムに関するhelper関数
"""
from recommendation.models import *
import redis
import numpy as np
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
import random
from recommendation.feedback_algorithms import exec_functions
from datetime import datetime
from common_helper import *

"""
フィードバック用のフィードバック辞書の実装
"""
def get_feedback_dict():

    feedbacks = [("pop", "明るい"), ("ballad", "静かな"), ("rock", "激しい")]
    feedback_dict = {}
    for index, feedback in enumerate(feedbacks):
        feedback_dict[index] = feedback
    
    return feedback_dict

def get_random_k_songs(k, song_obj):
    k_song_objs = []
    for i in xrange(k):
        index = random.randint(0, len(song_obj)-1)
        k_song_objs.append(song_obj[index])
    return k_song_objs

"""
ユーザーのフィードバックの内容と対象楽曲の永続化
"""
def save_user_song(user_id, song_id, situation, feedback_type):
    
    now = datetime.now()
    if EmotionEmotionbasedSong.objects.filter(user_id=user_id, song_id=song_id, situation=situation).exists():
        EmotionEmotionbasedSong.objects.filter(user_id=user_id, song_id=song_id, situation=situation).update(updated_at=now, feedback_type=feedback_type)
    else:
        EmotionEmotionbasedSong.objects.create(user_id=user_id, song_id=song_id, situation=situation, feedback_type=feedback_type, created_at=now, updated_at=now)

"""
モデルから楽曲取得(emotion)
"""
"""def get_top_song(user, emotions):
    song_ids = exec_functions.get_song_by_emotion(user, emotions)
    return get_song_objs(song_ids)"""
def get_top_song(user, situation, emotions, feedback_type):
    song_obj = None
    if SearchSong.objects.filter(user_id=user, situation=situation, feedback_type=feedback_type).exists():
        song_obj = get_now_search_song(user, situation, feedback_type)
    else:
        print "get_top_song"
        song_ids = exec_functions.get_song_by_emotion(user, emotions)
        song_obj = get_song_objs(song_ids)
        save_search_song(user, song_obj[0].id, situation, feedback_type)
    return song_obj

"""
学習と楽曲の取得(emotion)
"""
def learning_and_get_song(user, emotions):
    song_ids = exec_functions.learning_and_get_song_by_emotion(user, emotions, True)
    return get_song_objs(song_ids)

"""
一つ前の楽曲取得
すでに楽曲がEmotionEmotionbasedSongに含まれていたら、objectを走査する
含まれていない場合、最新のsong_objを取得する
"""
def get_back_song(user, song_id, situation):
    back_song_id = 0
    if EmotionEmotionbasedSong.objects.filter(user_id=user, situation=situation, song_id=song_id).exists():
        all_songs_by_situation = EmotionEmotionbasedSong.objects.order_by("updated_at").filter(user_id=user, situation=situation).values().reverse()
        for index, song_obj in enumerate(all_songs_by_situation):
            if song_obj["song_id"] == song_id:
                back_song_id = all_songs_by_situation[index+1]["song_id"]
                break
    else:
        back_song_id = EmotionEmotionbasedSong.objects.order_by("id").filter(user_id=user, situation=situation).values().reverse()[0]["song_id"]
    if back_song_id:
        SearchSong.objects.filter(user_id=user, situation=situation, song_id=back_song_id, feedback_type=1).update(updated_at=datetime.now())
    return get_song_obj(back_song_id)

"""
そのユーザーの視聴した楽曲を全て削除する
"""
def delete_user_listen_song(user_id):
    EmotionEmotionbasedSong.objects.filter(user_id=user_id).delete()
    SearchSong.objects.filter(user_id=user_id).delete()
    RecommendSong.objects.filter(user_id=user_id).delete()
    SituationEmotion.objects.filter(user_id=user_id).delete()
