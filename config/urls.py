

from django.contrib import admin
from django.urls import path

from decision_tree_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simular/', views.simulador_pnjs, name='simular_pnjs'),
]
