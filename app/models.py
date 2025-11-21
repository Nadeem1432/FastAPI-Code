from sqlmodel import SQLModel, Field

class Address(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    latitude: float
    longitude: float
