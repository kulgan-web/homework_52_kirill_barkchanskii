from django.urls import path
from webapp.views import index_page, create_task

urlpatterns = [
    path('', index_page),
    path('task/', create_task)
]