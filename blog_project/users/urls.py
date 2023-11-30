from django.urls import path
from . import views 
from .views import ProfileUpdateView

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
]