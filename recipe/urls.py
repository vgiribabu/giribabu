from django.urls import path
from recipe import views
app_name = 'recipe'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:recipe_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
 #                               document_root=settings.MEDIA_ROOT)