from django.urls import path
import core.views
from core.views import HomeView, PlaysView, PlayView, PerformanceView, AuthorsView, AuthorView, \
    AboutView, ActorView, DirectorView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

    path('plays/', PlaysView.as_view(), name='plays'),
    path('play/<int:pk>', PlayView.as_view(), name='play'),  # delete or make as buy page
    path('performance/<int:pk>', PerformanceView.as_view(), name='performance'),

    path('authors/', AuthorsView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorView.as_view(), name='author'),

    #path('actors/',),
    path('actor/<int:pk>', ActorView.as_view(), name='actor'),

    path('director/<int:pk>', DirectorView.as_view(), name='director'),

]

