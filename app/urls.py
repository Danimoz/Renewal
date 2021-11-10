from django.urls import path
from .views import (
    TrademarkCreateView, 
    ContainerCreateView, 
    TrademarkUpdateView, 
    ContainerDeleteView, 
    TrademarkDeleteView, 
    ContainerUpdateView, 
    TrademarkDetailView,
    ContainerDetailView,
    render_pdf_view,
)
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('dashboard/', views.dashboard, name='app-dashboard'),
    path('trademark/', views.trademark, name='app-trademark'),
    path('container/', views.container, name='app-container'),
    path('trademark/new/', TrademarkCreateView.as_view(), name='trademark-create'),
    path('trademark/<int:pk>/update/', TrademarkUpdateView.as_view(), name='trademark-update'),
    path('container/<int:pk>/update/', ContainerUpdateView.as_view(), name='container-update'),
    path('trademark/<int:pk>/delete/', TrademarkDeleteView.as_view(), name='trademark-delete'),
    path('container/<int:pk>/delete/', ContainerDeleteView.as_view(), name='container-delete'),
    path('trademark/<int:pk>/', TrademarkDetailView.as_view(), name='trademark-detail'),
    path('container/<int:pk>/', ContainerDetailView.as_view(), name='container-detail'),
    path('trademark/pdf/<int:pk>/', render_pdf_view, name='testee-view'),
    path('container/new/', ContainerCreateView.as_view(), name='container-create'),
]
