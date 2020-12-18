from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project
from .forms import ProjectForm, EditForm
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
import requests
# Create your views here.


discord_auth_url = 'https://discord.com/api/oauth2/authorize?client_id=787008196056449064&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify'


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/oauth2/login')
def get_authenticated_user(request: HttpRequest):
    print(request.user)
    user = request.user
    return render(request, 'layout.html',
                  {
                      "logged": True,
                      "id": user.id,
                      "discord_tag": user.discord_tag,
                      "avatar": user.avatar,
                      "email": user.email,
                      "public_flags": user.public_flags,
                      "flags": user.flags,
                      "email": user.email,
                      "locale": user.locale,
                  })


def rules(request):
    return render(request, 'rules.html')


def info(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"message": "hello"})


def discord_login(request: HttpRequest):
    return redirect(discord_auth_url)


def discord_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    print(code)
    user = exchange_code(code)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    print(discord_user)
    login(request, discord_user)
    return redirect('index')


def exchange_code(code: str):
    data = {
        "client_id": "787008196056449064",
        "client_secret": "w8xji9cyP_ziK_peJ2K0MAMl1yFY3U3u",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://127.0.0.1:8000/oauth2/login/redirect",
        "scope": "identify",
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(
        "https://discord.com/api/oauth2/token", data=data, headers=headers)

    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/v6/users/@me', headers={
        "Authorization": 'Bearer %s' % access_token
    })
    user = response.json()
    return user


def logout_page(request):
    if request.method == "POST":
        logout(request)
    return render(request, 'logout.html')


def about(request):
    return render(request, 'about.html')


def discord_profile(request):
    return render(request, 'discord_profile.html')


class ProjectsView(ListView):
    model = Project
    template_name = 'project.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_details.html'

    def get_object(self):
        obj = super().get_object()
        obj.project_views += 1
        obj.save()
        return obj


class AddProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'add_project.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.discord_tag
        form.instance.author_id = self.request.user.id
        form.instance.author_avatar = self.request.user.avatar
        return super().form_valid(form)


class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'update_project.html'
    form_class = EditForm


class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete_project.html'
    success_url = reverse_lazy('project')
