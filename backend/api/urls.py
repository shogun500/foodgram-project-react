from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.recipes import IngredientViewSet, RecipeViewSet, TagViewSet
from api.views.users import UsersViewSet

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
