import pytest
from grade_calculator import calculate_final_grade, letter_grade


def test_average_grade():
    assert calculate_final_grade([80, 90, 100]) == 90


def test_invalid_score():
    with pytest.raises(ValueError):
        calculate_final_grade([50, -10])


def test_empty_scores():
    with pytest.raises(ValueError):
        calculate_final_grade([])


def test_letter_A():
    assert letter_grade(95) == "A"


def test_letter_F():
    assert letter_grade(50) == "F"
