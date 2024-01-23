from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=255)
    year=models.IntegerField()
    poster_url=models.URLField()

    def get_absolute_url(self):
        return f'/movie/{self.id}/'

class SimilarityMatrix(models.Model):
    movie=models.OneToOneField(Movie,on_delete=models.CASCADE, related_name='similarity_matrix')
    similar_indices=models.TextField()