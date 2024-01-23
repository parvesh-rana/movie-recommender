# movie_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Movie, SimilarityMatrix

def index(request):
    # Get 40 random movies
    random_movies = Movie.objects.order_by('?')[:40]
    return render(request, 'index.html', {'movies': random_movies})

def similar_movies(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    similar_indices = [int(idx) for idx in movie.similarity_matrix.similar_indices.split(',')]
    similar_movies=[Movie.objects.get(id=similar_id) for similar_id in similar_indices[:40]]
    print(f"Similar Movies for {movie.title} (ID: {movie.id}): {[similar_movie.id for similar_movie in similar_movies]}")
    return render(request, 'similar_movies.html', {'movie':movie,'movies': similar_movies})

def search_results(request):
    query=request.GET.get('q','')
    results=Movie.objects.filter(title__icontains=query)
    return render(request, 'search_results.html' , {'query':query,'results':results})