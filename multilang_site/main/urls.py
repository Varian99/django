from django.urls import path
from . import views

# URLs du projet
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('switch_language/<str:lang_code>/', views.switch_language, name='switch_language'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
]