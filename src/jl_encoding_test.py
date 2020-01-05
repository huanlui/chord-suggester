from jl_encoding import Encoder
from pytest import approx
import pytest

categories = ['Apple', 'Orange', 'Grape']

@pytest.mark.parametrize("category,expected_number", [
    ("Apple",1), 
    ("Orange",2), 
    ("Grape",3),
])
def test_converts_category_to_number(category, expected_number):
    sut = Encoder(categories)

    number = sut.to_number(category)

    assert number == expected_number

@pytest.mark.parametrize("number,expected_category", [
    (1,"Apple"), 
    (2,"Orange"), 
    (3,"Grape"),
])
def test_converts_number_to_category(number,expected_category):
    sut = Encoder(categories)

    category = sut.to_category(number)

    assert category == expected_category
