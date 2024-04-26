from django.urls import path

from .views import home_view, article_view, search_view, create_view, update_view, del_view, posts_by_user


urlpatterns = [
    path('', home_view, name='base'),
    path('search/', search_view, name='article_search'),
    path('create/', create_view, name='create_post'),
    path('posts_by_user/<str:author>/', posts_by_user, name='posts_by_user'),
    path('update/<int:id>/', update_view, name='update_post'),
    path('delete/<int:id>/', del_view, name='delete_post'),
    path('<slug:slug>/', article_view, name='article_detail'),
]