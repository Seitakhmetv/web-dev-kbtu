import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { CompanyService } from '../company.service';
import { Vacancy } from '../models';

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit, OnChanges {

  vacancies: Vacancy[] = [];
  @Input()
  company_id: number = 0;

  constructor(private companiesService: CompanyService) { }

  ngOnInit(): void {
    this.getCompanyVacancy(this.company_id);
  }

  ngOnChanges(): void {
    this.getCompanyVacancy(this.company_id);
    console.log("CHanges vacan")
  }

  getCompanyVacancy(id: number){
    this.companiesService.getCompanyVacancies(id).subscribe((data)=>{
      console.log(data)
      this.vacancies = data;
    })
  }
}
