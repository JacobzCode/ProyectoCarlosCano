"""
Tests for storage_db module
Testing database operations with SQLAlchemy
"""
import pytest
from app.database import init_db, SessionLocal, Account, Entry
from app.storage_db import AccountStoreDB, EntryStoreDB


@pytest.fixture
def db_session():
    """Create a test database session"""
    init_db()
    session = SessionLocal()
    yield session
    session.close()


@pytest.fixture
def account_store():
    """Create account store instance"""
    return AccountStoreDB()


@pytest.fixture
def entry_store():
    """Create entry store instance"""
    return EntryStoreDB()


def test_create_account(account_store, db_session):
    """Test account creation"""
    handle = "testuser_create"
    email = "test@example.com"
    hashed = "hashed_password_123"
    
    account = account_store.create(handle, email, hashed, db=db_session)
    
    assert account is not None
    assert account.handle == handle
    assert account.email == email
    assert account.hashed == hashed
    assert account.id > 0


def test_find_account_by_handle(account_store, db_session):
    """Test finding account by handle"""
    handle = "testuser_find"
    email = "find@example.com"
    hashed = "hashed_password_456"
    
    # Create account
    created = account_store.create(handle, email, hashed, db=db_session)
    
    # Find account
    found = account_store.find_by_handle(handle, db=db_session)
    
    assert found is not None
    assert found.handle == handle
    assert found.email == email
    assert found.id == created.id


def test_find_nonexistent_account(account_store, db_session):
    """Test finding account that doesn't exist"""
    found = account_store.find_by_handle("nonexistent_user", db=db_session)
    assert found is None


def test_create_entry(entry_store, db_session):
    """Test entry creation"""
    entry = entry_store.create(
        account_id=1,
        handle="testuser",
        mood=7,
        comment="Feeling good today",
        horas_sueno=8.0,
        actividad_fisica=6,
        calidad_alimentacion=7,
        nivel_socializacion=5,
        db=db_session
    )
    
    assert entry is not None
    assert entry.mood == 7
    assert entry.comment == "Feeling good today"
    assert entry.horas_sueno == 8.0
    assert entry.actividad_fisica == 6
    assert entry.id > 0


def test_create_entry_minimal(entry_store, db_session):
    """Test entry creation with minimal fields"""
    entry = entry_store.create(
        account_id=1,
        handle="testuser",
        mood=5,
        db=db_session
    )
    
    assert entry is not None
    assert entry.mood == 5
    assert entry.comment is None
    assert entry.horas_sueno is None


def test_list_entries(entry_store, db_session):
    """Test listing all entries"""
    # Create some entries
    entry_store.create(1, "user1", 7, db=db_session)
    entry_store.create(1, "user1", 6, db=db_session)
    entry_store.create(2, "user2", 8, db=db_session)
    
    entries = entry_store.list_all(db=db_session)
    
    assert len(entries) >= 3
    assert all(isinstance(e, Entry) for e in entries)


def test_get_entry_by_id(entry_store, db_session):
    """Test getting specific entry by ID"""
    created = entry_store.create(1, "testuser", 9, "Great day!", db=db_session)
    
    found = entry_store.get(created.id, db=db_session)
    
    assert found is not None
    assert found.id == created.id
    assert found.mood == 9
    assert found.comment == "Great day!"


def test_get_nonexistent_entry(entry_store, db_session):
    """Test getting entry that doesn't exist"""
    found = entry_store.get(999999, db=db_session)
    assert found is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
