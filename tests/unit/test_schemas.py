"""Unit tests for Pydantic schemas."""

import pytest
from uuid import uuid4
from pydantic import ValidationError
from app.schemas.calculation import CalculationCreate, CalculationUpdate, CalculationType, CalculationBase


class TestCalculationCreateValidation:
    """Tests for CalculationCreate schema validation."""
    
    def test_calculation_create_insufficient_inputs(self):
        """Test CalculationCreate with fewer than 2 inputs."""
        user_id = uuid4()
        with pytest.raises(ValidationError):
            CalculationCreate(
                type="addition",
                inputs=[5],
                user_id=user_id
            )
    
    def test_calculation_create_division_by_zero_validation(self):
        """Test CalculationCreate validates division by zero."""
        user_id = uuid4()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            CalculationCreate(
                type="division",
                inputs=[10, 0],
                user_id=user_id
            )
    
    def test_calculation_create_division_with_zero_as_second_divisor(self):
        """Test CalculationCreate catches zero in division divisors."""
        user_id = uuid4()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            CalculationCreate(
                type="division",
                inputs=[100, 2, 0],
                user_id=user_id
            )
    
    def test_calculation_create_valid_addition(self):
        """Test valid CalculationCreate for addition."""
        user_id = uuid4()
        calc = CalculationCreate(
            type="addition",
            inputs=[10.5, 3, 2],
            user_id=user_id
        )
        assert calc.type == CalculationType.ADDITION
        assert calc.inputs == [10.5, 3, 2]
        assert calc.user_id == user_id
    
    def test_calculation_create_valid_division(self):
        """Test valid CalculationCreate for division."""
        user_id = uuid4()
        calc = CalculationCreate(
            type="division",
            inputs=[100, 2, 5],
            user_id=user_id
        )
        assert calc.type == CalculationType.DIVISION
        assert calc.inputs == [100, 2, 5]


class TestCalculationUpdateValidation:
    """Tests for CalculationUpdate schema validation."""
    
    def test_calculation_update_insufficient_inputs(self):
        """Test CalculationUpdate with insufficient inputs."""
        with pytest.raises(ValidationError):
            CalculationUpdate(inputs=[5])
    
    def test_calculation_update_valid(self):
        """Test valid CalculationUpdate."""
        update = CalculationUpdate(inputs=[42, 7])
        assert update.inputs == [42, 7]
    
    def test_calculation_update_none_inputs(self):
        """Test CalculationUpdate with None inputs (no update)."""
        update = CalculationUpdate(inputs=None)
        assert update.inputs is None
    
    def test_calculation_update_with_floats(self):
        """Test CalculationUpdate with float inputs."""
        update = CalculationUpdate(inputs=[10.5, 2.5])
        assert update.inputs == [10.5, 2.5]


class TestSchemaConfiguration:
    """Tests for schema model configuration."""
    
    def test_calculation_base_has_model_config(self):
        """Test that CalculationBase has model_config."""
        assert hasattr(CalculationBase, 'model_config')
        assert CalculationBase.model_config is not None
    
    def test_calculation_create_has_model_config(self):
        """Test that CalculationCreate has model_config."""
        assert hasattr(CalculationCreate, 'model_config')
        assert CalculationCreate.model_config is not None
        # Verify json_schema_extra is present
        assert 'json_schema_extra' in CalculationCreate.model_config
    
    def test_calculation_update_has_model_config(self):
        """Test that CalculationUpdate has model_config."""
        assert hasattr(CalculationUpdate, 'model_config')
        assert CalculationUpdate.model_config is not None
        # Verify json_schema_extra is present
        assert 'json_schema_extra' in CalculationUpdate.model_config
