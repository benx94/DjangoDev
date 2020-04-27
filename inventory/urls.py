from django.urls import path
from django.conf.urls import url
from .views import (inventory_addnew, inventory_update, inventory_delete)

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name='index'),
    path('inventoryIndex', views.inventory_index, name='inventory_index'),
    path('materielIndex', views.materiel_index, name='materiel_index'),
    path('inventoryAdd', views.inventory_add, name='inventory_add'),
    #url(r'^create/$', views.inventoryAddNew.as_view(), name='inventory_addnew'),
    #url(r'^(?P<pk>\d+)/update/$', views.inventoryUpdate.as_view(), name='inventory_update'),
    #url(r'^(?P<pk>\d+)/delete/$', views.inventoryDelete.as_view(), name='inventory_delete'),
    path('inventoryAddNew', views.inventory_addnew, name='inventory_addnew'),
    path('inventoryUpdate/<int:test_id>/', views.inventory_update, name='inventory_update'),
    path('inventoryDelete/<int:test_id>/', views.inventory_delete, name='inventory_delete'),
]