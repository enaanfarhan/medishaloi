from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # doctor
    path('doctor_search', views.doctor_search_v, name='doctor_search'),
    path('doctor_details/<int:post_id>', views.doctor_details_v, name="doctor_details"),

    #madichine
    path('madichine_search', views.madichine_search_v, name='madichine_search'),
    path('madichine_details/<int:post_id>', views.madichine_details_v, name="madichine_details"),

    # ambulance
    path('ambulance_search', views.ambulance_search_v, name='ambulance_search'),
    path('ambulance_details/<int:post_id>', views.ambulance_details_v, name="ambulance_details"),

    #login
    path('login', views.getLogin, name="login"),
    path('logout', views.getlogout, name="logout"),

    #register
    path('register', views.getRegister, name="register"),




]