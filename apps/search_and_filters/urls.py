from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.search_and_filters.views.search_history_view import SearchHistoryViewSet
from apps.search_and_filters.views.search_view import SearchViewSet
from apps.search_and_filters.views.search_history_user_view import UserSearchHistoryViewSet

router = DefaultRouter()
router.register(r'search-history', SearchHistoryViewSet, basename='search-history')
router.register(r'', SearchViewSet, basename='search')
router.register(r'user-search-history', UserSearchHistoryViewSet, basename='user-search-history')

urlpatterns = [
    path('', include(router.urls)),
]
