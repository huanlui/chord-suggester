import pytest
from jl_extended_chord import ExtendedChord
from pychord_jl import Chord
from jl_note import Note

@pytest.mark.parametrize("input_chord,expected_str_representation", [
    ("C","C"), 
    ("Dmaj","Dmaj"), 
    ("F#7","F#7"),
])
def test_should_have_the_same_str_representration_as_pychord(input_chord, expected_str_representation):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.__str__() == expected_str_representation


@pytest.mark.parametrize("input_chord, expected_root", [
    ("C", "C"), 
    ("Dmaj","D"), 
    ("F#7","F#"),
])
def test_should_return_root_as_a_jl_note(input_chord, expected_root):
    chord = ExtendedChord(Chord(input_chord))

    assert isinstance( chord.root, Note)
    assert str(chord.root) == expected_root

@pytest.mark.parametrize("input_chord, expected_slash_bass", [
    ("C/D", "D"), 
    ("Dmaj/F","F"), 
    ("F#7/A","A"),
])
def test_should_return_slash_bass_as_a_jl_note(input_chord, expected_slash_bass):
    chord = ExtendedChord(Chord(input_chord))

    assert isinstance(chord.slash_bass, Note)
    assert str(chord.slash_bass) == expected_slash_bass
