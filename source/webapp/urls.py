from django.urls import path
from webapp.views import index_page

urlpatterns = [
    path('', index_page),
]