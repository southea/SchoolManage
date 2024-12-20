"""SchoolManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import api

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.homePage),

    path('instructor/<int:id>/home', views.instructorHome),
    path('instructor/<int:id>/profile', views.instructorProfile),
    path('instructor/<int:id>/grade', views.instructorGrade),
    path('instructor/<int:id>/applications', views.instructorApplications),
    path('instructor/<int:id>/application', views.instructorApplication),

    path('student/<int:id>/home', views.studentHome),
    path('student/<int:id>/profile', views.studentProfile),
    path('student/<int:id>/application', views.studentApplication),
    path('student/<int:id>/apply', views.studentApply),

    path('admin/home', views.adminHome),
    path('admin/add', views.adminAdd),
    path('admin/delete', views.adminDelete),
    path('admin/applications', views.adminApplications),
    path('admin/application', views.adminApplication),
    path('admin/edit', views.adminEdit),

    path('api/login', api.login),

    path('api/ins/update', api.insUpdate),
    path('api/ins/confirm', api.insConfirm),

    path('api/stu/update', api.stuUpdate),
    path('api/stu/apply', api.stuApply),

    path('api/admin/add/stu', api.adminAddStu),
    path('api/admin/add/ins', api.adminAddIns),
    path('api/admin/add/grade', api.adminAddGrade),
    path('api/admin/delete/stu', api.adminDeleteStu),
    path('api/admin/delete/ins', api.adminDeleteIns),
    path('api/admin/delete/grade', api.adminDeleteGrade),
    path('api/admin/edit/stu', api.adminEditStu),
    path('api/admin/edit/ins', api.adminEditIns),
    path('api/admin/edit/grade', api.adminEditGrade),


]
