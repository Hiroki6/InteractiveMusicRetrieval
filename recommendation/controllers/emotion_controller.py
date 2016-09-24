# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect

from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from recommendation.models import Song, Artist, Preference
from recommendation.forms import MusicSearchForm, EmotionSearchForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from recommendation.fm import recommend_lib
from django.contrib.sites.models import Site
from .. import helpers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
import time
import sys
sys.dont_write_bytecode = True 

"""
印象語検索
"""
@login_required
def index(request):
    return render(request, 'emotions/emotion_search.html')

@login_required
def relevant_feedback(request):
    k_songs, error_msg = _emotion_search(request)
    return render(request, 'emotions/relevant_feedback.html', {'songs': k_songs, 'url': "relevant_feedback", 'error_msg': error_msg})

@login_required
def emotion_feedback(request):
    k_songs, error_msg = _emotion_search(request)
    return render(request, 'emotions/emotion_feedback.html', {'songs': k_songs, 'url': "emotion_feedback", 'error_msg': error_msg})

def _emotion_search(request):
    error_msg = ""
    k_songs = []
    if request.method == 'GET' and request.GET.has_key("emotion-search"):
        emotion = request.GET['emotion-search']
        if emotion == "0":
            error_msg = "印象語を選択してください"
        else:
            songs = helpers.search_by_emotion(int(emotion))
            k_songs = helpers.get_random_k_songs(10, songs)
    
    return k_songs, error_msg