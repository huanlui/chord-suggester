import pytest
from jl_extended_chord import ExtendedChord
from pychord_jl import Chord

@pytest.mark.parametrize("input_chord,expected_str_representation", [
    ("C","C"), 
    ("Dmaj","Dmaj"), 
    ("F#7","F#7"),
])
def test_should_have_the_same_str_representration_as_pychord(input_chord, expected_str_representation):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.__str__() == expected_str_representation
