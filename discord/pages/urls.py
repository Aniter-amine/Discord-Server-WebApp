from django.urls import path, include
from . import views
from .views import AddProjectView, ProjectDetailView, ProjectsView, DeleteProjectView, UpdateProjectView
urlpatterns = [
    path('', views.index, name="index"),
    path('project/', ProjectsView.as_view(), name="project"),
    path('rules/', views.rules, name="rules"),
    path('auth/user/', views.get_authenticated_user,
         name="get_authenticated_user"),
    path('oauth2/login/', views.discord_login, name="login"),
    path('oauth2/login/redirect',
         views.discord_login_redirect, name="login_redirect"),
    path('logout/',
         views.logout_page, name="logout"),
    path('profile/', views.discord_profile, name="discord_profile"),
    path('add_project/', AddProjectView.as_view(), name="add_project"),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/edit/<int:pk>', UpdateProjectView.as_view(), name='update_project'),
    path('project/delete/<int:pk>',
         DeleteProjectView.as_view(), name='delete_project'),
]
