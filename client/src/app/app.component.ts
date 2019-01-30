import { Component } from '@angular/core';
import { HeroService } from './hero.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Heroes';
  heroes = [];
  hero = {};
  private _heroService: HeroService;

  constructor(_heroService: HeroService) {
    this._heroService = _heroService;
  }

  ngOnInit(){
    let observable = this._heroService.getAll();
    observable.subscribe( data => {
      this.heroes = data['heroes']
    });
  }

  newHero(){
    let observable = this._heroService.create(this.hero);
    observable.subscribe( data => {
      console.log(data);
      this.hero = {};
      this.ngOnInit();
    });
  }

  imageAdded(e){
    console.log("someone added an image", e);
    let _this = this;        
    let file = e.target.files[0];        
    let reader = new FileReader();        
    reader.addEventListener("load", function() {                
        _this.hero['filename'] = file.name;                
        _this.hero['image'] = reader.result;    
        console.log(_this.hero);                  
    }, false);
    if (file) {              
        reader.readAsDataURL(file);        
    }
  }


}
