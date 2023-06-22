from django.urls import path
from . import views

urlpatterns = [
    path('politics', views.PoliticsView.as_view()),
    path('sports', views.SportsView.as_view()),
    path('business', views.BusinessView.as_view()),
    path('hedge', views.HedgeView.as_view()),
    path('rockwell', views.RockWellView.as_view()),
]