from django.urls import path

from . import views


app_name = 'projects'
urlpatterns = [
    # ex: /projects/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /projects/2/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
