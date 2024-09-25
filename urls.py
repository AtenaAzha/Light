from django.urls import path
from . import views

urlpatterns = [
    path('' , views.LandingPage.as_view() , name = 'landingPage'),
    path('project/' , views.Projects.as_view() , name = 'Projects'),
    path('manging/' , views.Managing.as_view() , name = 'Managing'),
    path('Team/' , views.Team.as_view() , name = 'Team'),
    path('Home/' , views.Home.as_view() , name = 'Home'),
    path('processes/' , views.Processes.as_view() , name = 'Processes'),
]
