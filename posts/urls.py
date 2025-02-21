from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='detail'),
]