from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Company, Vacancy

# Create your views here.
def company_list(request):
    array_of_companies = Company.objects.all()
    json_of_companies = [company.get_json() for company in array_of_companies]
    return JsonResponse(json_of_companies, safe=False)

def get_company(request, id):
    try:
        the_company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=404)
    return JsonResponse(the_company.get_json(), status=200, safe=False)

def vacancy_list(request):
    array_of_vacancies = Vacancy.objects.all()
    json_of_vacancy = [vacancy.get_json() for vacancy in array_of_vacancies]
    return JsonResponse(json_of_vacancy, safe=False)

def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=404)
    return JsonResponse(vacancy.get_json(), status=200, safe=False)


def list_of_company_vacancies(request, id):
    try:
        the_company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=404)
    the_company = the_company.get_json()
    
    vacancies = Vacancy.objects.all()
    the_vacancies = [vacancy.get_json() for vacancy in vacancies]

    company_vacancy_list = []

    for vacancy in the_vacancies:
        if vacancy['company'] == the_company['name']:
            company_vacancy_list.append(vacancy)
    return JsonResponse(company_vacancy_list, safe=False)

def top_ten(request):
    def comparator(a, b):
        return a['salary'] > b['salary']
    all_vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.get_json() for vacancy in all_vacancies]
    vacancies_json = sorted(vacancies_json, key=lambda d: d['salary'], reverse=True)[0:10]
    print(len(vacancies_json))
    return JsonResponse(vacancies_json, safe=False)