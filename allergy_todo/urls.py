from django.contrib import admin
from django.urls import path
from allergy import views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('register/', views.registerform, name='registerform'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # CRUD
    path('profile/', views.profile, name='profile'),
    path('createNewAllergy/', views.createNewAllergy, name='createNewAllergy'),
    path('createNewHospitalization', views.createNewHospitalization, name='createNewHospitalization'),
    path('allergy/<int:allergy_pk>', views.updateallergy, name='updateallergy'),
    path('allergy/<int:allergy_pk>/delete', views.deleteallergy, name='deleteallergy'),



    path('Emergency/', views.Emergency, name='Emergency'),
    path('json/', views.json, name='json'), 
    path('index', views.index, name='index'),
      
]
