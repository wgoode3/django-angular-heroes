import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HeroService {

  private _httpClient: HttpClient; 
  
  constructor(_httpClient: HttpClient) { 
    this._httpClient = _httpClient;
  }

  getAll() {
    return this._httpClient.get("/hero");
  }

  create(hero) {
    return this._httpClient.post("/hero", hero);
  }

}
