from django.shortcuts import render
from .models import Movie, Song
from django.views.generic import CreateView, ListView, DetailView


class MovieCreateView(CreateView):
    model = Movie
    fields = "__all__"
    template_name = "movie/add.html"
    success_url = "/music/list"


class MovieListView(ListView):
    model = Movie
    template_name = "movie/index.html"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/detail.html"


class SongCreateView(CreateView):
    model = Song
    fields = "__all__"
    template_name = "song/add.html"
    success_url = "/music/slist"


class SongListView(ListView):
    model = Song
    template_name = "song/index.html"


class SongDetailView(DetailView):
    model = Song
    template_name = "song/detail.html"
