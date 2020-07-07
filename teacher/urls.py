from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('t-login', views.login, name='t-login'),
    path('t-signup', views.signup, name='t-signup'),
    path('t_dash/', views.dashboard, name='t_dash'),
    path('t-profile-update', views.profileUpdate, name="t-profile-update"),
    path('teacher_logout', views.teach_logout, name='teach_logout'),    
    path('allstudent', views.allstudent, name="allstudent"),
    path('classes', views.classes, name="classes"),
    path('enterClass/<str:classno>', views.enterClass, name="enterClass"),
    path('taccount_details', views.taccount_details, name="taccount_details")
]
