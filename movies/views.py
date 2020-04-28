from django.shortcuts import render
from .models import Movie


# Create your views here.
def intro(request):
    return render(request, 'movies/foo.html')


def first_movie(request):
    data = {'title': 'The Good, The Bad And The Ugly',
            'synopsys': 'A western movie',
            'release': '1966'}
    return render(request, 'movies/first_movie.html', data)


def get_all_movies(request):
    data = {'movies' : [{'title': '1 - The Good, The Bad & The Ugly',
                           'synopsys' : 'A western',
                           'release': '1966'},
                           {'title': '2 - The Good, The Bad & The Ugly',
                           'synopsys' : 'A western',
                           'release': '1966'},
                           {'title': '3 - The Good, The Bad & The Ugly',
                           'synopsys' : 'A western',
                           'release': '1966'}]            }

    return render(request, 'movies/all-movies.html', data)


def create(request):

    movie = Movie(title="My Movie 2", synopsys="Something there",
                  release_year="1989", duration=180)
    movie.save()

    data = {'movie': movie}
    return render(request, 'movies/create.html', data)


def read(request):

    movies = Movie.objects.all()
    data = {'movies': movies}

    return render(request, 'movies/read.html', data)
