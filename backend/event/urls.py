from django.urls import path
from . import views


urlpatterns = [
    path('', views.BrowseEventsView.as_view()),
    path('newest/', views.NewestEventsView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('my_events/', views.MyEventsView.as_view()),
    path('<int:pk>/', views.EventDetailView.as_view()),
]
