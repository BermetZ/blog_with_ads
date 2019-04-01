from django.shortcuts import render, get_object_or_404
from .models import Ad, Company, Comment
from .forms import AdForm, CompanyForm, CommentForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse


class AdList(ListView):
    template_name = 'ad_list.html'
    model = Ad


def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, 'ad_detail.html', {'ad': ad})


class AdCreate(CreateView):
    template_name = 'ad_edit.html'
    form_class = AdForm
    model = Ad

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ad_detail', kwargs={'pk': self.object.id})


class AdEdit(UpdateView):
    template_name = 'ad_edit.html'
    form_class = AdForm
    model = Ad

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ad_detail', kwargs={'pk': self.object.id})


class CompanyList(ListView):
    template_name = 'company_list.html'
    model = Company


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company_detail.html', {'company': company})


class CompanyCreate(CreateView):
    template_name = 'company_edit.html'
    form_class = CompanyForm
    model = Company

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('company_detail', kwargs={'pk': self.object.id})


class CompanyEdit(UpdateView):
    template_name = 'company_edit.html'
    form_class = CompanyForm
    model = Company

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ad_detail', kwargs={'pk': self.object.id})


def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'comment_detail.html', {'comment': comment})


class CommentCreate(CreateView):
    template_name = 'comment_edit.html'
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('comment_detail', kwargs={'pk': self.object.id})


class CommentEdit(UpdateView):
    template_name = 'comment_edit.html'
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ad_detail', kwargs={'pk': self.object.id})