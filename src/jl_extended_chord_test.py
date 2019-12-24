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

@pytest.mark.parametrize("input_chord, expected_5th_circle_x", [
    ("C",0.0), 
    ("A",1.0), 
])
def test_x_in_5th_circle_is_the_same_as_root_for_major_chords (input_chord, expected_5th_circle_x):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.x_in_5th_circle == approx(expected_5th_circle_x, 0.001)

@pytest.mark.parametrize("input_chord, expected_5th_circle_y", [
    ("C",1.0), 
    ("A",0.0), 
])
def test_y_in_5th_circle_is_the_same_as_root_for_major_chords (input_chord, expected_5th_circle_y):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.y_in_5th_circle == approx(expected_5th_circle_y, 0.001)

@pytest.mark.parametrize("input_chord, expected_5th_circle_x", [
    ("C5",0.0), 
    ("A5",1.0), 
])
def test_x_in_5th_circle_is_the_same_as_root_for_neutral_chords (input_chord, expected_5th_circle_x):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.x_in_5th_circle == approx(expected_5th_circle_x, 0.001)

@pytest.mark.parametrize("input_chord, expected_5th_circle_y", [
    ("C5",1.0), 
    ("A5",0.0), 
])
def test_y_in_5th_circle_is_the_same_as_root_for_neutral_chords (input_chord, expected_5th_circle_y):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.y_in_5th_circle == approx(expected_5th_circle_y, 0.001)

@pytest.mark.parametrize("input_chord, expected_5th_circle_x", [
    ("Cm",-1), 
    ("Am",0), 
])
def test_x_in_5th_circle_is_the_same_as_root_relative_major_for_minor_chords (input_chord, expected_5th_circle_x):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.x_in_5th_circle == approx(expected_5th_circle_x, 0.001)

@pytest.mark.parametrize("input_chord, expected_5th_circle_y", [
    ("Cm",0), 
    ("Am",1), 
])
def test_y_in_5th_circle_is_the_same_as_root_relative_major_for_minor_chords (input_chord, expected_5th_circle_y):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.y_in_5th_circle == approx(expected_5th_circle_y, 0.001)

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

@pytest.mark.parametrize("input_chord, expected_intervals", [
    ("C",[3,4,7]), 
    ("C7",[3,4,6,7,10]), 
])
def test_returns_all_interval_combinations(input_chord, expected_intervals):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.intervals == expected_intervals

@pytest.mark.parametrize("input_chord, expected_complexity", [
     ("C",3.33), 
     ("Cm",3.33), 
     ("C7",5.6), 
     ("Cm7",4.25), 
     ("C9",6), 
     ("Cm9",5.66), 
     ("C9+11",6.375), 
     ("Cm9+11",6.375), 
     ("C13+11",5.6), 
     ("Cm13+11",6), 
     ("Cadd4",5),
     ("Cadd2",4),
     ("Cdim",8),
    ("Caug",5)
])
def test_returns_all_interval_combinations(input_chord, expected_complexity):
    chord = ExtendedChord(Chord(input_chord))

    assert chord.complexity == approx(expected_complexity, 0.01)





