import { Component, OnChanges, OnInit } from '@angular/core';
import { CompanyService } from './company.service';
import { Company } from './models';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'hh_front';

  logged = false
  username = '';
  password = '';
  companies: Company[] = [];

  ngOnInit() {
    const token = localStorage.getItem('token');
    if(token){
      this.logged = true
    }
  }

  constructor(private companyService: CompanyService){}

  login(){
    this.companyService.login(this.username, this.password).subscribe((data)=>{
      
      localStorage.setItem('token', data.token)

      this.logged=true;
      this.username = '';
      this.password = '';
    })
  }

  logout(){
    this.logged = false;
    localStorage.removeItem('token');
  }

  city_select(city: string){
    console.log(city)
    this.companyService.getCityCompanies(city).subscribe((data)=>{
      console.log(data);
      this.companies = data;
    })
  }
}
