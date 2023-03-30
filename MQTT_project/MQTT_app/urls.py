from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('publish', views.publish_message, name='publish'),
    path('UPdate', views.start_mqtt, name='update'),
]