import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {BookListComponent} from "./components/book-list/book-list.component";
import {HomeComponent} from "./components/home/home.component";
import {GenreComponent} from "./components/genre/genre.component";


const routes: Routes = [
  // {path: '', redirectTo: '/books', pathMatch: 'full', component: HomeComponent},
  // {path: 'books/:id', component: BookListComponent},
  // {path: 'genres/:id', component: GenreComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
