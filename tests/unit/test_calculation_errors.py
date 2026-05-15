"""Integration tests for calculation model error handling."""

import pytest
from app.models.calculation import (
    Addition,
    Subtraction,
    Multiplication,
    Division
)


class TestCalculationErrorHandling:
    """Tests for error handling in calculation subclasses."""
    
    def test_addition_with_non_list_inputs(self):
        """Test Addition raises ValueError when inputs is not a list."""
        add = Addition(user_id="test-user", inputs="not a list")
        with pytest.raises(ValueError, match="Inputs must be a list"):
            add.get_result()
    
    def test_addition_with_insufficient_inputs(self):
        """Test Addition raises ValueError with fewer than 2 inputs."""
        add = Addition(user_id="test-user", inputs=[5])
        with pytest.raises(ValueError, match="at least two numbers"):
            add.get_result()
    
    def test_subtraction_with_non_list_inputs(self):
        """Test Subtraction raises ValueError when inputs is not a list."""
        sub = Subtraction(user_id="test-user", inputs="not a list")
        with pytest.raises(ValueError, match="Inputs must be a list"):
            sub.get_result()
    
    def test_subtraction_with_insufficient_inputs(self):
        """Test Subtraction raises ValueError with fewer than 2 inputs."""
        sub = Subtraction(user_id="test-user", inputs=[5])
        with pytest.raises(ValueError, match="at least two numbers"):
            sub.get_result()
    
    def test_multiplication_with_non_list_inputs(self):
        """Test Multiplication raises ValueError when inputs is not a list."""
        mult = Multiplication(user_id="test-user", inputs="not a list")
        with pytest.raises(ValueError, match="Inputs must be a list"):
            mult.get_result()
    
    def test_multiplication_with_insufficient_inputs(self):
        """Test Multiplication raises ValueError with fewer than 2 inputs."""
        mult = Multiplication(user_id="test-user", inputs=[5])
        with pytest.raises(ValueError, match="at least two numbers"):
            mult.get_result()
    
    def test_division_with_non_list_inputs(self):
        """Test Division raises ValueError when inputs is not a list."""
        div = Division(user_id="test-user", inputs="not a list")
        with pytest.raises(ValueError, match="Inputs must be a list"):
            div.get_result()
    
    def test_division_with_insufficient_inputs(self):
        """Test Division raises ValueError with fewer than 2 inputs."""
        div = Division(user_id="test-user", inputs=[5])
        with pytest.raises(ValueError, match="at least two numbers"):
            div.get_result()
    
    def test_division_by_zero_first_divisor(self):
        """Test Division raises ValueError when dividing by zero."""
        div = Division(user_id="test-user", inputs=[10, 0])
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            div.get_result()
    
    def test_division_by_zero_second_divisor(self):
        """Test Division raises ValueError when second divisor is zero."""
        div = Division(user_id="test-user", inputs=[100, 2, 0])
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            div.get_result()


class TestCalculationRepr:
    """Tests for __repr__ methods."""
    
    def test_addition_repr(self):
        """Test Addition __repr__ method."""
        add = Addition(user_id="test-user", inputs=[1, 2, 3])
        repr_str = repr(add)
        assert "Calculation" in repr_str
        assert "addition" in repr_str or "inputs" in repr_str
    
    def test_subtraction_repr(self):
        """Test Subtraction __repr__ method."""
        sub = Subtraction(user_id="test-user", inputs=[10, 3])
        repr_str = repr(sub)
        assert "Calculation" in repr_str
    
    def test_multiplication_repr(self):
        """Test Multiplication __repr__ method."""
        mult = Multiplication(user_id="test-user", inputs=[2, 3])
        repr_str = repr(mult)
        assert "Calculation" in repr_str
    
    def test_division_repr(self):
        """Test Division __repr__ method."""
        div = Division(user_id="test-user", inputs=[10, 2])
        repr_str = repr(div)
        assert "Calculation" in repr_str
