from django.urls import path
from .views import MovieCreateView, MovieListView, MovieDetailView, SongListView, SongCreateView, SongDetailView


urlpatterns = [
    path("list", MovieListView.as_view(), name="MoviewListView"),
    path("<pk>/detail", MovieDetailView.as_view(), name="MovieDetailView"),
    path("create", MovieCreateView.as_view(), name="MovieCreateView"),
    path("slist", SongListView.as_view(), name="SongListView"),
    path("<pk>/sdetail", SongDetailView.as_view(), name="SongDetailView"),
    path("screate", SongCreateView.as_view(), name="SongCreateView"),
]

