from django_filters import rest_framework as filters
from .models import Author

class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  #поиск без учёта регистра

    class Meta:
        model = Author
        fields = ['name']