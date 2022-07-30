from unicodedata import name
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('branchfess/',views.branchfees,name="branch"),
    path('landing/',views.landing,name="landing"),
    path('hostel/',views.hostel,name="hostel"),
    path('documentVerification/',views.docuveri,name="doc"),
    path('campusTour/',views.camtour,name="campustour"),
    path('digitalHandbook/',views.digihand,name="digihand"),
    path('offlineCounseling/',views.offcouns,name="offcouns"),
    path('maps/',views.maps,name="maps"),
    path('login/',views.login,name="login"),
]