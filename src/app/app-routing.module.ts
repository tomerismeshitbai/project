import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {BookListComponent} from "./components/book-list/book-list.component";
import {HomeComponent} from "./components/home/home.component";
import {GenreComponent} from "./components/genre/genre.component";
import { LoginComponent } from './components/login/login.component';
import { BookDetailsComponent } from './components/book-details/book-details.component';
import { AboutComponent } from './components/about/about.component';


const routes: Routes = [
  // {path: '', redirectTo: '/books', pathMatch: 'full', component: HomeComponent},
  {path: 'books', component: BookListComponent},
  {path: 'books/:id', component: BookDetailsComponent },
  {path: 'login', component: LoginComponent},
  {path: 'about', component: AboutComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
