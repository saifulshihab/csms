from django.urls import path
from . import views

urlpatterns = [
    path('enterOfficer', views.enterOfficer, name="enterOfficer"),
    path('signup', views.registration, name="signup"),
    path('backlogin', views.backlogin, name="backlogin"),
    path('officerReg', views.officerReg, name="officerReg"),
    path('offcierLogin', views.offcierLogin, name="offcierLogin"),
    path('logout', views.logout, name="logout"),
    path('school_detail/<str:school_eiin>/',
         views.school_detail, name="school_detail"),
    path('dash', views.dash, name="dash"),
    path('hpend', views.hpend, name="hpend")



]
