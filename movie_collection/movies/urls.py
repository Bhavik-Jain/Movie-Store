from django.urls import path
from .views import MovieView, CollectionDetailView, CollectionsView


urlpatterns = [
    path('movies/', MovieView.as_view(), name='movies'),
    path('collection/', CollectionsView.as_view(), name='collection-view'),
    path('collection/<uuid:uuid>/', CollectionDetailView.as_view(), name='collection-detail'),
]