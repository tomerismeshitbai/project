import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Book} from "./models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class BookService {


  constructor(private client: HttpClient) {
  }

  BASE_URL = 'http://127.0.0.1:8000';

  getBooks(): Observable<Book[]> {
    return this.client.get<Book[]>(`${this.BASE_URL}/api/books/`);
  }

  getBookDetail(id: string): Observable<Book> {
    return this.client.get<Book>(`${this.BASE_URL}/api/books/${id}/`);
  }

  getBooksByGenreId(id: any): Observable<Book[]> {
    return this.client.get<Book[]>(`${this.BASE_URL}/api/genres/${id}/`);
  }

}
