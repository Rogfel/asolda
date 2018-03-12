# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse_lazy, reverse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Project, Image, Parameter

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
###########
# Project

# @method_decorator(login_required, name='dispatch')
class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(user = self.request.user)
        return context


class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project


class ProjectCreation(LoginRequiredMixin, CreateView):
    model = Project
    success_url = reverse_lazy('project-list')
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectCreation, self).form_valid(form)


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    success_url = reverse_lazy('project-list')
    fields = ['name', 'description']


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')

###########
# Image


class ImageList(LoginRequiredMixin, ListView):
    model = Image


class ImageDetail(LoginRequiredMixin, DetailView):
    model = Image
    # parameter = Parameter.objects.filter(image_id=Image.id).all()
    # def get_success_url(self):
    #     return reverse('project-detail', args=[self.kwargs.get('slug_proy')])
    def get_context_data(self, **kwargs):
        context = super(ImageDetail, self).get_context_data(**kwargs)
        context['parameters'] = Parameter.objects.all()
        return context


class ImageCreation(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['name', 'img']

    def form_valid(self, form):
        form.instance.project = Project.objects.get(
            slug=self.kwargs.get('slug_proy'))
        return super(ImageCreation, self).form_valid(form)

    def get_success_url(self):
        return reverse('project-detail', args=[self.kwargs.get('slug_proy')])


class ImageUpdate(LoginRequiredMixin, UpdateView):
    model = Image
    # success_url = reverse_lazy('image-list')
    fields = ['name', 'img']

    def get_success_url(self):
        return reverse('project-detail', args=[self.kwargs.get('slug_proy')])


class ImageDelete(LoginRequiredMixin, DeleteView):
    model = Image
    # success_url = reverse_lazy('image-list')

    def get_success_url(self):
        return reverse('project-detail', args=[self.kwargs.get('slug_proy')])
