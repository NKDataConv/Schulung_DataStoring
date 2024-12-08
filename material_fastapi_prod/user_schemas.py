from pydantic import BaseModel
from typing import Optional
from datetime import date


# Pydantic-Modell für Benutzer
class UserBase(BaseModel):
    Name: str
    Email: str
    Adresse: str
    Geburtsdatum: Optional[date] = None


# Pydantic-Modell für Benutzererstellung
class UserCreate(UserBase):
    pass


# Pydantic-Modell für die Antwort (z. B. ohne sensible Daten wie Passwörter)
class UserResponse(UserBase):
    index: int

    class Config:
        orm_mode = True