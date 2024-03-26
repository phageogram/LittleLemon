from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'), name='indexpage'),
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]