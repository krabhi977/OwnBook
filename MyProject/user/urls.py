from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('product/',views.product),
    path('order/',views.myorder),
    path('enquiry/',views.enquiry),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('Novel/',views.Novel),
    path('Fictional/',views.Fictional),
    path('Academic/',views.Academic),
    path('profile/',views.myprofile),
    path('viewproduct/',views.viewproduct),
    path('signout/',views.signout),
    path('myordr/',views.myordr),
    path('mycart/',views.mycart),
    path('',views.index),
]