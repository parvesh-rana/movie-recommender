# movie_app/management/commands/load_similarity_matrix.py
import numpy as np
from django.core.management.base import BaseCommand
from movie_app.models import SimilarityMatrix, Movie

class Command(BaseCommand):
    help = 'Load similarity matrix from .npy file'

    def handle(self, *args, **options):
        matrix = np.load('../../msi2.npy')

        for i, row in enumerate(matrix):
            movie = Movie.objects.get(pk=i + 1)  # Assuming your movie IDs start from 1
            similar_indices = ','.join(map(str, row))
            SimilarityMatrix.objects.create(movie=movie, similar_indices=similar_indices)

        self.stdout.write(self.style.SUCCESS('Successfully loaded similarity matrix'))
