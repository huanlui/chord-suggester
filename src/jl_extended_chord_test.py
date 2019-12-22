import pytest
from jl_extended_chord import ExtendedChord, ChordMode
from pychord_jl import Chord
from jl_note import Note
from pytest import approx

@pytest.mark.parametrize("input_chord,expected_str_representation", [
    ("C","C"), 
    ("Dmaj","Dmaj"), 
    ("F#7","F#7"),
])
def test_has_the_same_str_representration_as_pychord(input_chord, expected_str_representation):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.__str__() == expected_str_representation

@pytest.mark.parametrize("input_chord, expected_mode", [
    ("C",ChordMode.Major), 
    ("C/F#",ChordMode.Major), 
    ("Em",ChordMode.Minor),
    ("Fm7",ChordMode.Minor),
    ("D5",ChordMode.Neutral),
])
def test_detects_mode_of_the_chord(input_chord, expected_mode):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.mode == expected_mode

@pytest.mark.parametrize("input_chord, expected_root_x", [
    ("C",0.0), 
    ("A",1.0), 
])
def test_returns_root_x(input_chord, expected_root_x):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.root_x == approx(expected_root_x, 0.001)

@pytest.mark.parametrize("input_chord, expected_root_y", [
    ("C",1.0), 
    ("A",0.0), 
])
def test_returns_root_y(input_chord, expected_root_y):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.root_y == approx(expected_root_y, 0.001)

@pytest.mark.parametrize("input_chord, expected_root", [
    ("C", "C"), 
    ("Dmaj","D"), 
    ("F#7","F#"),
])
def test_returns_root_as_a_jl_note(input_chord, expected_root):
    chord = ExtendedChord(Chord(input_chord))

    assert isinstance( chord.root, Note)
    assert str(chord.root) == expected_root

@pytest.mark.parametrize("input_chord, expected_slash_bass", [
    ("C", "C"), 
    ("C/D", "D"), 
    ("Dmaj/F","F"), 
    ("F#7/A","A"),
])
def test_returns_slash_bass_as_a_jl_note(input_chord, expected_slash_bass):
    chord = ExtendedChord(Chord(input_chord))

    assert isinstance(chord.slash_bass, Note)
    assert str(chord.slash_bass) == expected_slash_bass

@pytest.mark.parametrize("input_chord, expected_relative_slash_x", [
    ("C",0.0), 
    ("C/A",1.0), 
])
def test_returns_relative_x_of_slash_respecting_the_root(input_chord, expected_relative_slash_x):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.relative_slash_x == approx(expected_relative_slash_x, 0.001)

@pytest.mark.parametrize("input_chord, expected_relative_slash_y", [
    ("C",0.0), 
    ("C/F#",-2.0), 
])
def test_returns_relative_y_of_slash_respecting_the_root(input_chord, expected_relative_slash_y):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.relative_slash_y == approx(expected_relative_slash_y, 0.001)



