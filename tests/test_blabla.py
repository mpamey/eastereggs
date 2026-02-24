from src.process import process 


def test_addition():
    # Arrange
    getal_1 = 2
    getal_2 = 3
    
    validate_sum = 5
    # Act
    result = process.addition(getal_1, getal_2)
    # Assert
    assert result == validate_sum
    
    
def test_subtraction():
    # Arrange
    getal_1 = 5
    getal_2 = 3
    
    validate_subtraction = 2
    # Act
    result = process.subtraction(getal_1, getal_2)
    # Assert
    assert result == validate_subtraction
