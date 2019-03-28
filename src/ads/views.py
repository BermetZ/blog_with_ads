from django.shortcuts import render, get_object_or_404, redirect
from .models import Ad
from django.views.generic import ListView, CreateView, UpdateView


class AdList(ListView):
    template_name = 'ad_list.html'
    print(Ad.objects.all())
    model = Ad

