from typing import List, Optional
from datetime import date

from pydantic import BaseModel, field_serializer, validator


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
    revenue: int
    country: str

    @field_serializer("date")
    def serialize_date(self, v: date) -> str:
        return v.isoformat()

    @validator("revenue", pre=True)
    def validate_revenue(cls, v):
        return int(v)

    class Config:
        orm_mode = True


class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailResponseSchema]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int
