from jl_dictionaries import Dictionaries
import pytest

@pytest.mark.parametrize("quality_components,expected_quality_name", [
    ( (0,4,7),""), 
     ( (0,3,7),"m"), 
])
def test_return_quality_name_from_quality_components(quality_components, expected_quality_name):
    quality_name = Dictionaries.get_quality_name(quality_components)

    assert quality_name == expected_quality_name

@pytest.mark.parametrize("quality_name,expected_quality_components", [
    ( "",(0,4,7)), 
     ( "M",(0,4,7)), 
     ( "m",(0,3,7)), 
])
def test_return_quality_components_from_quality_name(quality_name, expected_quality_components):
    quality_components = Dictionaries.get_quality_components(quality_name)

    assert quality_components == expected_quality_components

@pytest.mark.parametrize("note_name,expected_note_value", [
    ( "C",0), 
    ( "B",11), 
    ( "D#",3), 
])
def test_return_note_value_from_note_name(note_name, expected_note_value):
    note_value = Dictionaries.get_note_value(note_name)

    assert note_value == expected_note_value

def test_return_all_possible_chords():
    chords = Dictionaries.get_all_possible_chords()

    assert len(chords) == 804

