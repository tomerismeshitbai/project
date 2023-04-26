export interface Book {
    id: number;
    name: string;
    description: string;
    genre: number;
    rate: string;
    size: string;
    img: string;
  }
  
  export interface Genre {
    id: number;
    name: string;
  }
  
  export class Commentary {
    static cnt = 0;
    constructor(
      public id: number = Commentary.cnt++,
      public username: string,
      public movie: string,
      public description: string
    ) {}
  }