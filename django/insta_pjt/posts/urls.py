from django.urls import path, include
from posts import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/comments/create/', views.comment_create, name="comment_create"),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comment_delete, name="comment_delete"),
    path('<int:post_id>/like/', views.like, name="like"),
    path('likes/', views.show_likes, name="show_likes"),
    path('followings/', views.show_followings, name="show_followings"),
]