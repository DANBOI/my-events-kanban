export interface Category {
  id: number;
  name: string;
}

export interface Event {
  id?: number;
  category: string;
  title: string;
  date: string;
  location: string;
  description?: string;
  participation_fee?: number;
  image_url?: string;
}
