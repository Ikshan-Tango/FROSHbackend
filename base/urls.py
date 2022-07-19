from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('branchfess/',views.branchfees,),
    path('hostel/',views.hostel),
    path('DocumentVerification/',views.docuveri),
    path('CampusTour/',views.camtour),
    path('DigitalHandbook/',views.digihand),
    path('OfflineCounseling/',views.offcouns),
    path('Maps/',views.maps),
    path('Login/',views.login),
]