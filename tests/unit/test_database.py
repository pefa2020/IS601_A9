"""Unit tests for database module."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.database import get_engine, get_sessionmaker


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
