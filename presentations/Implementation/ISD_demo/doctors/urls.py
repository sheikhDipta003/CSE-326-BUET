from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='doctor_dashboard'),
    path('<int:doctor_id>/', views.DashboardView.as_view(), name='doctor_dashboard'),
    path('add_prescription/', views.addSuggesions.as_view(), name='add_prescription'),
    path('create_appointment/', views.createAppointment.as_view(), name='create_appointment'),
    path('checkup_report_status/', views.checkup_report_status_view.as_view(), name='checkup_report_status'),
    path('member_condition/<int:member_id>/', views.member_condition_view.as_view(), name='member_condition'),
    path('nurse_schedule/<int:member_id>/', views.nurse_schedule_view.as_view(), name='nurse_schedule'),
    path('prescription/', views.prescription_view.as_view(), name='prescription'),
    path('resident_status/', views.resident_status_view.as_view(), name='resident_status'),
]
