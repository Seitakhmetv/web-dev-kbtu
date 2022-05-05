from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import Http404
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def company_list(request):
    if request.method == 'GET':
        array_of_companies = Company.objects.all()
        serializer = CompanySerializer(array_of_companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_company(request, id):
    try:
        the_company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({'message': str(e)}, status=404)

    if request.method == 'GET':
        serializer = CompanySerializer(the_company)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CompanySerializer(instance=the_company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        the_company.delete()
        return Response({'message': 'deleted'}, status=204)


class VacancyListAPIVIEW(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        array_of_vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(array_of_vacancies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GetVacancyAPIVIEW(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        the_vacancy = self.get_object(pk)
        serializer = VacancySerializer(the_vacancy)
        return Response(serializer.data)

    def put(self, request, pk=None):
        the_vacancy = self.get_object(pk)
        serializer = VacancySerializer(instance=the_vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        the_vacancy = self.get_object(pk)
        the_vacancy.delete()
        return Response({'message': 'deleted'}, status=204)


@permission_classes((IsAuthenticated,))
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
@permission_classes((IsAuthenticated,))
def companyByCity(request, city):
    array_of_companies = Company.objects.all()

    citycompanies = []

    serializer = CompanySerializer(array_of_companies, many=True)
    for company in serializer.data:
        if company['city'].lower() == city:
            citycompanies.append(company)

    if len(citycompanies) > 0:
        return JsonResponse(citycompanies, safe=False)
    else:
        return JsonResponse({'message': f'no companies in {city}'}, safe=False)

    
    return JsonResponse(citycompanies, safe=False)

 
@permission_classes((IsAuthenticated,))
def top_ten(request):
    def comparator(a, b):
        return a['salary'] > b['salary']
    all_vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.get_json() for vacancy in all_vacancies]
    vacancies_json = sorted(vacancies_json, key=lambda d: d['salary'], reverse=True)[0:10]
    print(len(vacancies_json))
    return JsonResponse(vacancies_json, safe=False)