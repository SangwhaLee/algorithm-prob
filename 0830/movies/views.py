from django.shortcuts import render

# Create your views here.
def home(request):
    movie = ['relfection on you', 'harry potter', 'spider man',]

    context = {
        'movie': movie,
    }
    return render(request, 'movies/home.html', context)