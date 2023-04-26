import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { TopBarComponent } from './components/top-bar/top-bar.component';
import { BookListComponent } from './components/book-list/book-list.component';
import { BookFilterComponent } from './components/book-filter/book-filter.component';
import { GenreComponent } from './components/genre/genre.component';
import { RegisterComponent } from './components/register/register.component';
import { BookDetailsComponent } from './components/book-details/book-details.component';
import { AboutComponent } from './components/about/about.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    TopBarComponent,
    BookListComponent,
    BookFilterComponent,
    GenreComponent,
    RegisterComponent,
    BookDetailsComponent,
    AboutComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
