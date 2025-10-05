from typing import List, Optional
from datetime import date

from pydantic import BaseModel, field_serializer


class MovieDetailResponseSchema(BaseModel):
    id: int
    name: str
    date: date
    score: int
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: int
    revenue: float
    country: str

    @field_serializer("date")
    def serialize_date(self, v: date) -> str:
        return v.isoformat()

    @field_serializer("revenue")
    def serialize_revenue(self, v: float) -> int:
        return int(v)

    class Config:
        orm_mode = True


class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailResponseSchema]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int
