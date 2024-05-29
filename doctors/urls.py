from django.urls import path
from .views import manage_patient_records, view_patient_record, delete_patient_record, e_prescribe, update_patient_record

urlpatterns = [
    path('records/', manage_patient_records, name='manage_patient_records'),
    path('record/view/<int:record_id>/', view_patient_record, name='view_patient_record'),
    path('record/delete/<int:record_id>/', delete_patient_record, name='delete_patient_record'),
    path('record/update/<int:record_id>/', update_patient_record, name='update_patient_record'),
    path('e_prescribe/', e_prescribe, name='e_prescribe'),
]