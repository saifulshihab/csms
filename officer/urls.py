from django.urls import path
from . import views

urlpatterns = [
    path('enterOfficer', views.enterOfficer, name="enterOfficer"),
    path('signup', views.registration, name="signup"),
    path('backlogin', views.backlogin, name="backlogin"),
    path('officerReg', views.officerReg, name="officerReg"),
    path('offcierLogin', views.offcierLogin, name="offcierLogin"),
    path('logout', views.logout, name="logouts"),
    path('school_detail/<str:school_eiin>/',
         views.school_detail, name="school_detail"),
    path('student_feedback', views.student_feedbacks, name="student_feedbacks"),
    path('dash', views.dash, name="dash"),
    path('hpend', views.hpend, name="hpends"),
    path('reject_head/<str:h_empid>/', views.reject_head, name="reject_head"),
    path('head_approve/<str:h_empid>/', views.head_approve, name="head_approve"),
    path('allheadmaster', views.allheadmasters, name="allheadmasters"),
    path('registered_schools', views.registered_schools, name="registered_schools"),
    path('assign_co/<str:se>', views.assign_co, name="assign_co")
]
