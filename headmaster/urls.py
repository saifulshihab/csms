from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('head_logout', views.head_logout, name="head_logout"),
    path('about', views.about, name='about'),
    path('teacherverification', views.teacherverification,
         name='teacherverification'),
    path('teacher_reject/<str:t_empid>/',
         views.teacher_reject, name="teacher_reject"),
    path('teacher_approve/<str:t_empid>/',
         views.teacher_approve, name="teacher_approve"),
    path('allteacher', views.allteachers, name="allteachers"),
    path('assign_teacher', views.assign_teacherr, name="assign_teacher"),
    path('change_tname', views.change_tname, name="change_tname"),
    path('delete_teacher/<int:id>/', views.delete_teacher, name="delete_teacher"),
    path('account_details', views.account_details, name="account_details")
]
