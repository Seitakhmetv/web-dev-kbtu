import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { CompanyService } from '../company.service';
import { Company, Vacancy } from '../models';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit, OnChanges {

  companies: Company[] = [];
  choose: boolean = false;
  selected_company_id: number = 0;

  constructor(private companiesService: CompanyService) { }

  ngOnInit(): void {
    this.getCompanies();
    this.choose = false;
  }

  ngOnChanges(changes: SimpleChanges): void {
    this.choose = false;
    console.log("Changed")
  }

  getCompanies(){
    this.companiesService.getCompanies().subscribe((data)=>{
      //console.log(data);
      this.companies = data;
    })
  }

  checked(id: number){
    console.log(id)
    this.choose = true;
    this.selected_company_id = id
  }
}
