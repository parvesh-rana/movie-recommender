from django.urls import path
from .views import index,similar_movies,search_results

urlpatterns=[
    path('', index, name='index'),
    path('movie/<int:movie_id>/', similar_movies, name='similar_movies'),
    path('search/',search_results, name='search_results'),
]