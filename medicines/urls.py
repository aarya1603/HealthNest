from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('add/', views.add_medicine, name='add_medicine'),
    path('taken/<int:dose_id>/', views.mark_taken, name='mark_taken'),
    path('delete/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
    path('skipped/<int:dose_id>/', views.mark_skipped, name='mark_skipped'),
]
