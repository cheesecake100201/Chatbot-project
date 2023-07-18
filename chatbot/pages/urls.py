from django.urls import path
from .views import home_view, register_view, dashboard_view, login_view, query_view, view_conversation
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='chat_login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('query/', query_view, name='query'),
    path('conversation/', view_conversation, name='view')
]