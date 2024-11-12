from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('new', views.new_show),
    path('<int:id>', views.show_by_id),
    path('<int:id>/edit', views.edit_show),
    path('create', views.new_show_create),
    path('<int:id>/destroy', views.delete_show),
    path('<int:id>/update', views.update_show),
]
