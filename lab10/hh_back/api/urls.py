from django.contrib import admin
from django.urls import path
from api.views import company_list, get_company, list_of_company_vacancies, VacancyListAPIVIEW, GetVacancyAPIVIEW, top_ten
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', company_list),
    path('companies/<int:id>/', get_company),
    path('companies/<int:id>/vacancies/', list_of_company_vacancies),
    path('vacancies/', VacancyListAPIVIEW.as_view()),
    path('vacancies/<int:pk>/', GetVacancyAPIVIEW.as_view()),
    path('vacancies/top_ten', top_ten)
]
