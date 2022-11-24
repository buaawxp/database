from django.urls import path

from . import views

urlpatterns = [

    path('', views.toLogin_view),
    path('index/', views.Login_view),
    path('regist_user/', views.regist_user),
    path('regist_admin/',views.regist_admin),\
    path('login/', views.login_user),
    #path('login_user/', views.login_user),
    path('change_pwd_user/', views.change_pwd_user),
    path('change_n_user/',views.change_n_user),
    path('change_p_user/',views.change_p_user),
    path('change_pwd_admin/',views.change_pwd_admin),
    path('login_admin/', views.login_admin),
    path('regist_clothing/', views.regist_clothing),
    path('regist_share/', views.regist_share),
    path('regist_order/', views.regist_order),
    path('regist_message/',views.regist_message),
    path('del_clothing/', views.del_clothing),
    path('del_share/', views.del_share),


]
