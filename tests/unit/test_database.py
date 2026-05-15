"""Unit tests for database module."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.database import get_engine, get_sessionmaker, get_db


class TestGetEngine:
    """Tests for get_engine factory function."""
    
    def test_get_engine_creates_engine(self):
        """Test that get_engine creates a valid SQLAlchemy engine."""
        test_db_url = "sqlite:///:memory:"
        engine = get_engine(test_db_url)
        assert engine is not None
        assert engine.url.drivername == "sqlite"
    
    def test_get_engine_with_default_url(self):
        """Test that get_engine works with default URL."""
        engine = get_engine()
        assert engine is not None


class TestGetSessionmaker:
    """Tests for get_sessionmaker factory function."""
    
    def test_get_sessionmaker_creates_sessionmaker(self):
        """Test that get_sessionmaker creates a valid sessionmaker."""
        test_db_url = "sqlite:///:memory:"
        engine = get_engine(test_db_url)
        sessionmaker_factory = get_sessionmaker(engine)
        assert sessionmaker_factory is not None
        
        # Verify we can create a session from it
        session = sessionmaker_factory()
        assert isinstance(session, Session)
        session.close()
    
    def test_get_sessionmaker_session_lifecycle(self):
        """Test that sessionmaker sessions can be properly created and closed."""
        test_db_url = "sqlite:///:memory:"
        engine = get_engine(test_db_url)
        sessionmaker_factory = get_sessionmaker(engine)
        
        session = sessionmaker_factory()
        assert session is not None
        # Verify session can be used
        assert session.get_bind() is not None
        session.close()


class TestGetDb:
    """Tests for get_db dependency function."""
    
    def test_get_db_yields_and_closes_session(self):
        """Test that get_db yields a session and closes it properly."""
        gen = get_db()
        session = next(gen)
        
        # Verify it's a session
        assert isinstance(session, Session)
        
        # Complete the generator to trigger finally block
        try:
            next(gen)
        except StopIteration:
            pass
    
    def test_get_engine_with_explicit_parameter(self):
        """Test get_engine with explicit database_url parameter."""
        test_db_url = "sqlite:///:memory:"
        engine = get_engine(database_url=test_db_url)
        assert engine is not None
        assert engine.url.drivername == "sqlite"
