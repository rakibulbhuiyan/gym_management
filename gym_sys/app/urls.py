from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('pagedetail/<int:id>/', views.page_detail,name='pagedetail'),
    path('faq/', views.faq_list,name='faq'),
    path('enquiry/', views.enquiry,name='enquiry'),
    path('gellary/', views.gellary,name='gellary'),
    path('gellarydetail/<int:id>/', views.gellary_detail,name='gallery_detail'),
    path('pricing/', views.pricing,name='pricing'),

    path('checkout/<int:plan_id>/', views.checkout,name='checkout'),

    #accounts::::::trainer (login,profile, dashboard,
    path('accounts/signup/', views.signup,name='signup'),
    path('trainerlogin/', views.trainerlogin,name='trainerlogin'),
    path('trainer_changepassword/', views.trainer_password_change,name='trainer_changepassword'),
    path('trainerlogout/', views.trainerlogout,name='trainerlogout'),
    path('trainer_dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
    path('trainer_profile/', views.trainer_profile, name='trainer_profile'),
    path('trainer_subcriber/', views.trainer_subcriber, name='trainer_subcriber'),
    path('trainer_payments/', views.trainer_payments, name='trainer_payments'),

    #notifications
    path('notification/', views.notification,name='notification'),
    path('get_notifs/', views.get_notifs,name='get_notifs'),
    path('mark_as_read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),

    #dashboard work
    path('user_dashboard/', views.user_dashboard,name='user_dashboard'),
    path('update_profile/', views.update_Profile,name='update_profile'),
]