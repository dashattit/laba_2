from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, AuthorListCreateView, AuthorDetailView

#создаем экземпляр DefaultRouter
router = DefaultRouter()
#регистрируем ViewSets
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

#включаем маршруты в urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
]