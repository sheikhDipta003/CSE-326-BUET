from django.urls import path
from . import views

urlpatterns = [
    path('<int:nurse_id>/', views.DashboardView.as_view(), name='dashboard'),
    path('add_checkup_data/<int:checkup_id>/', views.CheckupDataEntryView.as_view(), name='add_checkup_data'),
    path('add_checkup_data_special/<int:checkup_id>/', views.CheckupDataSpecialEntryView.as_view(), name='add_checkup_data_special'),
    path('resident_condition/', views.ResidentConditionView.as_view(), name='resident_condition'),
    # With this setup, the CheckupDataListView view already expects the order_by parameter in the URL; order_by is passed as a query parameter in the URL, such as '/checkup_data/?order_by=blood_pressure', '/checkup_data/?order_by=sugar', or '/checkup_data/?order_by=heartrate'.
    path('checkup_data/', views.CheckupDataListView.as_view(), name='checkup_data_list'),
]
