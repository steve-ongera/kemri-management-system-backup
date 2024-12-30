# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    path('search_doctor/' , views.search_doctors , name="search_doctors"),

    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('patient/search/', views.patient_search, name='patient_search'),
    path('patients/randomized/', views.randomized_patients_view, name='randomized_patients'),
    path('patients/unrandomized/', views.unrandomized_patients_view, name='unrandomized_patients'),

    path('interns/', views.intern_list, name='intern_list'),
    path('interns/<int:pk>/', views.intern_detail, name='intern_detail'),
    path('interns/add/', views.intern_create, name='intern_create'),
    path('interns/<int:pk>/edit/', views.intern_update, name='intern_update'),
    path('interns/<int:pk>/delete/', views.intern_delete, name='intern_delete'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('departments/add/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),

    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),

    path('medical-records/', views.medical_record_list, name='medical_record_list'),
    path('medical-records/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    path('medical-records/add/', views.medical_record_create, name='medical_record_create'),
    path('medical-records/<int:pk>/edit/', views.medical_record_update, name='medical_record_update'),
    path('medical-records/<int:pk>/delete/', views.medical_record_delete, name='medical_record_delete'),

    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staff/add/', views.staff_create, name='staff_create'),
    path('staff/<int:pk>/edit/', views.staff_update, name='staff_update'),
    path('staff/<int:pk>/delete/', views.staff_delete, name='staff_delete'),

    path('nonstaff/', views.nonstaff_list, name='nonstaff_list'),
    path('nonstaff/<int:pk>/', views.nonstaff_detail, name='nonstaff_detail'),
    path('nonstaff/add/', views.nonstaff_create, name='nonstaff_create'),
    path('nonstaff/<int:pk>/edit/', views.nonstaff_update, name='nonstaff_update'),
    path('nonstaff/<int:pk>/delete/', views.nonstaff_delete, name='nonstaff_delete'),

    path('reports/', views.report_list, name='report_list'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
    path('reports/add/', views.report_create, name='report_create'),
    path('reports/<int:pk>/edit/', views.report_update, name='report_update'),
    path('reports/<int:pk>/delete/', views.report_delete, name='report_delete'),

    path('lab-tests/', views.labtest_list, name='labtest_list'),
    path('lab-tests/<int:pk>/', views.labtest_detail, name='labtest_detail'),
    path('lab-tests/add/', views.labtest_create, name='labtest_create'),
    path('lab-tests/<int:pk>/edit/', views.labtest_update, name='labtest_update'),
    path('lab-tests/<int:pk>/delete/', views.labtest_delete, name='labtest_delete'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),

    
    path('messages/<str:username>/', views.send_message, name='message_thread'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/create/<str:username>/', views.create_chat, name='create_chat'),



    path('help-and-support/', views.help_and_support, name='help_and_support'),
    path('system-settings/', views.system_settings, name='system_settings'),

    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),

    path('tb-patients/', views.tb_patient_list, name='tb_patient_list'),
    path('tb_patient_add', views.tb_patient_add , name='tb_patient_add'),
    path('tb-patient/<int:pk>/', views.tb_patient_detail, name='tb_patient_detail'),
    path('tb-patient/<int:pk>/update/', views.tb_patient_update, name='tb_patient_update'),
    path('tb-patient/<int:pk>/delete/', views.tb_patient_delete, name='tb_patient_delete'),
    path('search-patient/', views.search_tb_patient, name='search_tb_patient'),
    path('tb-dashboard/', views.tb_dashboards, name='tb_dashboard'),
    path("tb_Patient_graphs/" , views.graph_tb , name="graph_tb"), 
    path('randomized-tb-patients/', views.randomized_tb_patients_view, name='randomized_tb_patients'),
    path('unrandomized-tb-patients/', views.unrandomized_tb_patients_view, name='unrandomized_tb_patients'),
    path('hiv-positive-tb-patients/', views.hiv_positive_tb_patients_view, name='hiv_positive_tb_patients'),
    path('pregnant-tb-patients/', views.pregnant_tb_patients_view, name='pregnant_tb_patients'),

    path('vaccine-performance/', views.vaccine_performance, name='vaccine_performance'),  #  Add this line
    path('vaccine-analysis/', views.vaccine_analysis, name='vaccine_analysis'),
    path('county_victims_analysis/', views.county_victims_analysis, name='county_victims_analysis'),
    path('tb_patients_map/', views.tb_patients_map, name='tb_patients_map'),

    path('answer/<int:assignment_id>/', views.answer_questionnaire, name='answer_questionnaire'),
    path('responses/<int:questionnaire_id>/', views.view_responses, name='view_responses'),
    path('list_questionnaires/', views.list_questionnaires, name='questionnaire_list'),

    path('serious_adverse_event_list/', views.serious_adverse_event_list, name='serious_adverse_event_list'), 
    path('patient/<int:patient_id>/create-serious-adverse-event/', views.create_serious_adverse_event, name='create_serious_adverse_event'),
    path('serious-adverse-event/<int:event_id>/', views.view_serious_adverse_event_detail, name='serious_adverse_event_detail'),
    path('serious-adverse-event/<int:event_id>/update/', views.update_serious_adverse_event, name='update_serious_adverse_event'),
    path('serious-adverse-event/<int:event_id>/delete/', views.delete_serious_adverse_event, name='delete_serious_adverse_event'),

    path('lost-to-follow-up/', views.lost_to_follow_up_list, name='lost_to_follow_up_list'),
    path('lost-to-follow-up/create/', views.lost_to_follow_up_create, name='lost_to_follow_up_create'),
    path('lost-to-follow-up/<int:pk>/', views.lost_to_follow_up_detail, name='lost_to_follow_up_detail'),
    path('lost-to-follow-up/<int:pk>/update/', views.lost_to_follow_up_update, name='lost_to_follow_up_update'),
    path('lost-to-follow-up/<int:pk>/delete/', views.lost_to_follow_up_delete, name='lost_to_follow_up_delete'),


    path('withdrawn-consents/', views.withdrawn_consent_list, name='withdrawn_consent_list'),
    path('withdrawn-consents/create/', views.withdrawn_consent_create, name='withdrawn_consent_create'),
    path('withdrawn-consents/<int:id>/', views.withdrawn_consent_detail, name='withdrawn_consent_detail'),
    path('withdrawn-consents/<int:id>/update/', views.withdrawn_consent_update, name='withdrawn_consent_update'),
    path('withdrawn-consents/<int:id>/delete/', views.withdrawn_consent_delete, name='withdrawn_consent_delete'),
]


