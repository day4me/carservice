from django.urls import path
from .views import RequestCreateView, RequestUpdateView, RequestDeleteView, ChartData,Chart
from . import views

urlpatterns = [
    path('', views.home, name='carservice-main'),
    path('request/new', RequestCreateView.as_view(), name='request-create'),
    path('request/<int:pk>/update', RequestUpdateView.as_view(), name='request-update'),
    path('request/<int:pk>/delete', RequestDeleteView.as_view(), name='request-delete'),
    path('admin/request/<int:pk>/pdf', views.AdminRequestPDF, name='AdminRequestPDF'),
    path('admin/api/chart/data', ChartData.as_view(), name='chart-data'),
    path('chart', Chart.as_view(), name='chart'),
]