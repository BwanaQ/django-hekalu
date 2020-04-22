from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Estate, Rental


# ========== Estate CRUD =========


class EstateListView(LoginRequiredMixin, ListView):
    model = Estate
    template_name = 'estate/estate_list.html'

    def get_queryset(self):
        return Estate.objects.filter(manager=self.request.user)

class EstateDetailView(LoginRequiredMixin, DetailView):
    model = Estate
    template_name = 'estate/estate_detail.html'


class EstateUpdateView(LoginRequiredMixin, UpdateView):
    model = Estate
    fields = ('title', 'description',)
    template_name = 'estate/estate_edit.html'

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.manager != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class EstateDeleteView(LoginRequiredMixin, DeleteView):
    model = Estate
    template_name = 'estate/estate_delete.html'
    success_url = reverse_lazy('estate_list')

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.manager != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class EstateCreateView(LoginRequiredMixin, CreateView):
    model = Estate
    fields = ('title', 'description',)
    template_name = 'estate/estate_new.html'
    login_url = 'login'

    def form_valid(self, form): # new
        form.instance.manager = self.request.user
        return super().form_valid(form)


# ========== Rental CRUD =========

class RentalListView(LoginRequiredMixin, ListView):
    model = Rental
    template_name = 'rental/rental_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(estate=self.kwargs['estate_pk'])

class RentalCreateView(LoginRequiredMixin, CreateView):
    model = Rental
    fields = ('category','title', 'description','rent','is_occupied')
    template_name = 'rental/rental_new.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        self.estate = get_object_or_404(Estate, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form): # new
        form.instance.manager = self.request.user
        form.instance.estate = self.estate
        return super().form_valid(form)

class RentalDetailView(LoginRequiredMixin, DetailView):
    model = Rental
    template_name = 'rental/rental_detail.html'

class RentalUpdateView(LoginRequiredMixin, UpdateView):
    model = Rental
    fields = ('category','title', 'description','rent','is_occupied')
    template_name = 'rental/rental_edit.html'

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.manager != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class RentalDeleteView(LoginRequiredMixin, DeleteView):
    model = Rental
    template_name = 'rental/rental_delete.html'

    def get_success_url(self):
        return reverse_lazy('rental/rental_list', kwargs={'estate_pk': self.object.estate.pk})
