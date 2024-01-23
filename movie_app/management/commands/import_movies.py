# movie_app/management/commands/import_movies.py
import csv
from django.core.management.base import BaseCommand
from movie_app.models import Movie

class Command(BaseCommand):
    help = 'Import movies from CSV file'

    def handle(self, *args, **options):
        with open('../../output2.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=['Title', 'Release Year', 'Poster'])
            next(csv_reader, None)
            for row in csv_reader:
                Movie.objects.create(
                    title=row['Title'],
                    year=row['Release Year'],
                    poster_url=row['Poster'],
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported movies'))
