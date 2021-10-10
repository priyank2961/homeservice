"""homeservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.http import request
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.aboutView),
    path('e_signin/', views.e_signinView),
    path('e_signup/', views.e_signupView),
    path('e_displayAppointment/', views.e_displayAppointmentView),
    path('e_pendingAppointment/',views.e_pendingAppointmentView),
    path('e_AcceptRequest/', views.e_AcceptRequestView),
    path('e_CancelRequest/', views.e_CancelRequestView),
    path('e_homepage/', views.e_homepageView),
    path('startpage/',views.startpage),
    path('c_selectServiceName/', views.c_selectServiceNameView),
    path('assignrole/', views.assignroleView),
    path('c_saveData/', views.c_saveDataView),
    path('c_addappoint/',views.c_addappointmentView),
    path('c_signInCheck/', views.c_signInCheckView),
    path('c_selectDate/', views.c_selectDateView),
    path('c_homepage/', views.c_homepageView),
    path('c_displayappoint/',views.c_displayappointView),
    path('c_submitAppointment/', views.c_submitAppointmentView),
    path('e_saveData/', views.e_savedataView),
    path('e_signincheck/', views.e_signincheckView),
    path('c_signup/', views.c_signupView),
    path('c_deleteAppoint/', views.c_deleteAppointView),
    path('c_date_time/', views.c_date_timeView),
    path('c_signin/', views.c_signinView),
]
