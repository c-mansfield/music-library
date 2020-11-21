from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

from .forms import UserForm
from .models import Album, Song

# Create views from /music/
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()

#class LoginView(View):


class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_art']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_art']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # Get user reg page
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Post to add user to DB
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # Creates object from form fields
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Check db if user in db and details correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        # If any error on login
        return render(request, self.template_name, {'form': form})
