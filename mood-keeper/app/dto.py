from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class AccountCreate(BaseModel):
    handle: str
    email: EmailStr
    secret: str

class SessionCreate(BaseModel):
    handle: str
    secret: str

class AccountOut(BaseModel):
    id: int
    handle: str
    email: str
    created: datetime

class EntryCreate(BaseModel):
    mood: int
    comment: Optional[str] = None
    # Nuevos campos de hábitos
    horas_sueno: Optional[float] = None
    actividad_fisica: Optional[int] = None
    calidad_alimentacion: Optional[int] = None
    nivel_socializacion: Optional[int] = None

class EntryOut(BaseModel):
    id: int
    account_id: int
    handle: str
    mood: int
    comment: Optional[str]
    # Campos de hábitos
    horas_sueno: Optional[float] = None
    actividad_fisica: Optional[int] = None
    calidad_alimentacion: Optional[int] = None
    nivel_socializacion: Optional[int] = None
    created: datetime
