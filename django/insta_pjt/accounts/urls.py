from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('delete/', views.delete, name="delete"),
    path('update/', views.update, name="update"),
    path('password/', views.password, name="password"),
    path('<str:user_name>/', views.profile, name="profile"),
    path('profile_update/', views.profile_update, name="profile_update"),
    path('<int:user_pk>/follow/', views.follow, name="follow"),
]