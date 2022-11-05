from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django_filters import rest_framework as filters
from .models import Movie
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

# Removes permissions from views

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAuthenticated, ) # bug 6
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly) # bug 8?
    queryset = Movie.objects.all()
