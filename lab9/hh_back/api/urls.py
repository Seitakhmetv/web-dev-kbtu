from django.contrib import admin
from django.urls import path
from api.views import company_list, get_company, list_of_company_vacancies, vacancy_list, get_vacancy, top_ten

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:id>/', get_company),
    path('companies/<int:id>/vacancies/', list_of_company_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>/', get_vacancy),
    path('vacancies/top_ten', top_ten)
]
