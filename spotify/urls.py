from django.urls import path 
from . import views
from . views import SongCreateView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name="home"),
    path('play/<int:id>',views.playSong, name="play"),
    path('create',SongCreateView.as_view(), name="create"),
    path('times/',views.MyTimedView.as_view(),name='timeview'),

    path('signup/',views.signup, name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]






