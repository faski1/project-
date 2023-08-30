from django.urls import path
from .views import profile, login, logout

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]
