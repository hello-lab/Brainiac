
from django.contrib import admin
from django.urls import path, include
from dashboard.views import *

urlpatterns = [
    path("", home_page, name ="admin"),
    path('tools/study_music', study_music),
    path('tools/timer', timer),
    path('forum/', forum),
    path('learn/', learning_page),
    path('help/', help_page),
    path('profile/', profile_page),
    path('logout/', logout_view),
    path('quizzes/', quizzes_view),
    path('404/', e404_page),
    path('quiz/<int:quiz_id>/', quiz_view, name='quiz_view'),
    path('podcasts/', podcasts),
]

