"""Unit tests for User model."""

import pytest
from uuid import uuid4
from app.models.user import User


class TestUserModel:
    """Tests for User model."""
    
    def test_user_repr(self):
        """Test User __repr__ method."""
        user = User(
            id=uuid4(),
            username="testuser",
            email="test@example.com"
        )
        repr_str = repr(user)
        assert "User" in repr_str
        assert "testuser" in repr_str
        assert "test@example.com" in repr_str
