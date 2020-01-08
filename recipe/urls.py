from django.urls import path
from recipe import views
app_name = 'recipe'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:recipe_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]