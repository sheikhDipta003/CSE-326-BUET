from django.urls import path
from . import views

urlpatterns = [
    path('<int:member_id>/', views.DashboardView.as_view(), name='resident_dashboard'),
    # path('phy_status/<str:member_id>/', views.ResidentPhyStatusView.as_view(), name='phy_status'),
]
