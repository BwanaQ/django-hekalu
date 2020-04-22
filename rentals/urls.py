from django.urls import path
from .views import (
    EstateListView,

    EstateUpdateView,
    EstateDetailView,
    EstateDeleteView,
    EstateCreateView,

    RentalListView,

    RentalCreateView,
    RentalUpdateView,
    RentalDetailView,
    RentalDeleteView,

)

urlpatterns = [
    path('', EstateListView.as_view(), name='estate_list'),

    path('estate_edit/<int:pk>/', EstateUpdateView.as_view(), name='estate_edit'),
    path('estate_detail/<int:pk>/', EstateDetailView.as_view(), name='estate_detail'),
    path('estate_delete/<int:pk>/', EstateDeleteView.as_view(), name='estate_delete'),
    path('estate_new/', EstateCreateView.as_view(), name='estate_new'),

    path('<int:estate_pk>/', RentalListView.as_view(), name='rental_list'),

    path('rental_new/<int:pk>/', RentalCreateView.as_view(), name='rental_new'),
    path('rental_detail/<int:pk>/', RentalDetailView.as_view(), name='rental_detail'),
    path('rental_edit/<int:pk>/', RentalUpdateView.as_view(), name='rental_edit'),
    path('rental_delete/<int:pk>/', RentalDeleteView.as_view(), name='rental_delete'),

]
