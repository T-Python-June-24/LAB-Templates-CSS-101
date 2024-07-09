

import pandas as pd
from django.shortcuts import render
from .form import MovieForm
from .recommendation_engine import get_recommendations

def home_view(request):
    form = MovieForm()
    return render(request, 'recommender/home.html', {'form': form})

def recommend_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie_title = form.cleaned_data.get('title')
            try:
                movie_data = pd.read_csv('filmtv_movies.csv')
                filtered_movies = movie_data[movie_data['title'].str.contains(movie_title, case=False, na=False)]
                
                if filtered_movies.empty:
                    return render(request, 'recommender/home.html', {'form': form, 'error': 'No movies found with that title'})
                
                if len(filtered_movies) == 1:
                    chosen_movie = filtered_movies.iloc[0]
                else:
                    return render(request, 'recommender/home.html', {'form': form, 'error': 'Multiple movies found, please be more specific'})
                
                recommendations = get_recommendations(chosen_movie, movie_data)
                if recommendations:
                    return render(request, 'recommender/results.html', {'movies': recommendations})
                else:
                    return render(request, 'recommender/home.html', {'form': form, 'error': 'No recommendations found'})
            except FileNotFoundError:
                return render(request, 'recommender/home.html', {'form': form, 'error': 'Movie data file not found'})
        else:
                return render(request, 'recommendations/index.html', {'form': form, 'error': 'Please enter a movie title'})
    else:
        form = MovieForm()
    return render(request, 'recommender/home.html', {'form': MovieForm(), 'error': 'Invalid request'})
