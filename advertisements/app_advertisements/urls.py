from django import path
from .views import index

urlpatterns = (
    path('', index)
)
