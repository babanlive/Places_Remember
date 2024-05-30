from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from .forms import PlaceForm
from .models import Place


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title_page': 'Главная страница',
    }


class HomeView(LoginRequiredMixin, ListView):
    model = Place
    template_name = 'places/home.html'
    context_object_name = 'posts'
    title_page = 'Домашняя страница'

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user).select_related('user')


class CreatePlace(LoginRequiredMixin, CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/add_place.html'
    extra_context = {
        'title_page': 'Добавить воспоминание',
    }
    success_url = reverse_lazy('places:home')

    def form_valid(self, form):
        place = form.save(commit=False)
        place.user = self.request.user
        place.save()
        return super().form_valid(form)


class EditPlace(LoginRequiredMixin, UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/add_place.html'
    extra_context = {
        'title_page': 'Редактировать воспоминание',
    }
    success_url = reverse_lazy('places:home')


def page_not_found(request, exception):
    if isinstance(exception, Http404):
        return render(
            request,
            '404.html',
            {
                'title_page': 'Страница не найдена',
                'title': 'Страница не найдена',
                'message': 'К сожалению, мы не можем найти такую страницу.',
            },
        )

    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
