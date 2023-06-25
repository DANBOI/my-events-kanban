export interface Event {
  id: number;
  category: string;
  title: string;
  date: string;
  location: string;
  description?: string;
  participation_fee?: number;
  img_url?: string;
}