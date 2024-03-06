from django.urls import path
from emailsend import views

urlpatterns=[
    path('',views.home,name='home'),
    path('email/',views.send_email,name="send_email"),
]