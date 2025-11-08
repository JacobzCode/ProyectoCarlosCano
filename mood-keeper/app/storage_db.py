"""Storage layer using SQLAlchemy ORM"""
from typing import Optional, List
from sqlalchemy.orm import Session
from .database import Account, Entry, get_db, init_db
from datetime import datetime


class AccountStoreDB:
    """Database-backed account storage"""
    
    def __init__(self):
        init_db()
    
    def create(self, handle: str, email: str, hashed: str, db: Session = None):
        """Create new account"""
        should_close = False
        if db is None:
            db = next(get_db())
            should_close = True
        
        try:
            account = Account(handle=handle, email=email, hashed=hashed)
            db.add(account)
            db.commit()
            db.refresh(account)
            return account
        finally:
            if should_close:
                db.close()
    
    def find_by_handle(self, handle: str, db: Session = None):
        """Find account by handle"""
        should_close = False
        if db is None:
            db = next(get_db())
            should_close = True
        
        try:
            return db.query(Account).filter(Account.handle == handle).first()
        finally:
            if should_close:
                db.close()


class EntryStoreDB:
    """Database-backed entry storage"""
    
    def __init__(self):
        init_db()
    
    def create(self, account_id: int, handle: str, mood: int, comment: Optional[str] = None,
               horas_sueno: Optional[float] = None, actividad_fisica: Optional[int] = None,
               calidad_alimentacion: Optional[int] = None, nivel_socializacion: Optional[int] = None,
               db: Session = None):
        """Create new entry with mood and habits"""
        should_close = False
        if db is None:
            db = next(get_db())
            should_close = True
        
        try:
            entry = Entry(
                account_id=account_id,
                handle=handle,
                mood=mood,
                comment=comment,
                horas_sueno=horas_sueno,
                actividad_fisica=actividad_fisica,
                calidad_alimentacion=calidad_alimentacion,
                nivel_socializacion=nivel_socializacion
            )
            db.add(entry)
            db.commit()
            db.refresh(entry)
            return entry
        finally:
            if should_close:
                db.close()
    
    def list_all(self, db: Session = None) -> List[Entry]:
        """List all entries"""
        should_close = False
        if db is None:
            db = next(get_db())
            should_close = True
        
        try:
            return db.query(Entry).order_by(Entry.created.desc()).all()
        finally:
            if should_close:
                db.close()
    
    def get(self, eid: int, db: Session = None) -> Optional[Entry]:
        """Get entry by ID"""
        should_close = False
        if db is None:
            db = next(get_db())
            should_close = True
        
        try:
            return db.query(Entry).filter(Entry.id == eid).first()
        finally:
            if should_close:
                db.close()
