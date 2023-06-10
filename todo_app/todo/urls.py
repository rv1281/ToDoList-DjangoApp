from django.urls import include, path
from django.contrib.auth import views as auth_views
from todo.views import (
    home,
    signup,
    user_login,
    dashboard,
    logout_view,
    todo_list,
    create_todo,
    update_todo,
    delete_todo,
)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/todo/', todo_list, name='todo_list'),
    path('api/todo/create/', create_todo, name='create_todo'),
    path('api/todo/update/<int:pk>/', update_todo, name='update_todo'),
    path('api/todo/delete/<int:pk>/', delete_todo, name='delete_todo'),
]
