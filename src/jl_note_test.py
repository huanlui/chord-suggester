import pytest
from jl_note import Note
from pytest import approx

@pytest.mark.parametrize("note_str,expected_pychord_value", [
    ("C",0), 
    ("G",7),
    ("D",2),
    ("C#",1),
    ("Db",1),
    ("F#",6),
])
def test_stores_its_corresponding_pychord_value(note_str, expected_pychord_value):
    note = Note(note_str)

    assert note.pychord_value == expected_pychord_value

@pytest.mark.parametrize("note_str", [
    ("C"), 
    ("G"),
    ("D"),
    ("C#"),
    ("Db"),
    ("F#"),
])
def test_has_a_string_representation(note_str):
    note = Note(note_str)

    assert str(note) == note_str

@pytest.mark.parametrize("note_str,expected_position_in_5th_circle", [
    ("C",0), 
    ("G",1),
    ("D",2),
    ("C#",7),
    ("Db",7),
    ("F#",6),
    ("F",11),
])
def test_returns_its_corresponding_position_in_5th_circle(note_str, expected_position_in_5th_circle):
    note = Note(note_str)

    assert note.position_in_5th_circle == expected_position_in_5th_circle

@pytest.mark.parametrize("note_str,expected_angle_in_5th_circle", [
    ("C",0), 
    ("G",30),
    ("D",60),
    ("C#",210),
    ("Db",210),
    ("F#",180),
    ("F",330),
])
def test_returns_its_corresponding_angle_in_5th_circle(note_str, expected_angle_in_5th_circle):
    note = Note(note_str)

    assert note.angle_in_5th_circle_degrees == expected_angle_in_5th_circle

@pytest.mark.parametrize("note_str,expected_x_y_in_5th_circle", [
    ("C",(0,1)), 
    ("G",(0.5,0.866)), 
    ("D",(0.866,0.5)), 
    ("A",(1,0)),
    ("E",(0.866,-0.5)),
    ("B",(0.5,-0.866)),
    ("F#",(0,-1)),
    ("Gb",(0,-1)),
    ("C#",(-0.5,-0.866)),
    ("G#",(-0.866,-0.5)),
    ("D#",(-1,0)),
    ("A#",(-0.866,0.5)),
    ("F",(-0.5,0.866)), 
])
def test_returns_its_corresponding_x_y_in_5th_circle(note_str, expected_x_y_in_5th_circle):
    note = Note(note_str)

    position = note.x_y_in_5th_circle

    assert position[0] == approx(expected_x_y_in_5th_circle[0], rel=0.001)
    assert position[1] == approx(expected_x_y_in_5th_circle[1], rel=0.001)

@pytest.mark.parametrize("note_str,note_2_str,expected_substraction", [
    ("C","G",(-0.5,0.134)), 
    ("G","C",(0.5,-0.134)), 
    ("D","D#",(1.866,0.5)), 
])
def test_can_be_substracted(note_str, note_2_str,expected_substraction ):
    note =   Note(note_str)
    note_2 = Note(note_2_str)

    substraction = note - note_2

    assert substraction[0] == approx(expected_substraction[0], rel=0.001)
    assert substraction[1] == approx(expected_substraction[1], rel=0.001)

@pytest.mark.parametrize("note_str,note_str_2", [
    ("C","C"), 
    ("G","G"),
    ("E","Fb"),
    ("E#","F"),
    ("B","Cb"),
    ("B#","C"),
])
def test_notes_that_are_equal_are_detected(note_str, note_str_2):
    note = Note(note_str)
    note2 = Note(note_str_2)
    assert note == note2

@pytest.mark.parametrize("note_str,note_str_2", [
    ("C","C#"), 
    ("G","A"),
    ("E","F"),
    ("E#","E"),
    ("B","C"),
    ("B#","A"),
])
def test_notes_that_are_different_are_detected(note_str, note_str_2):
    note = Note(note_str)
    note2 = Note(note_str_2)
    assert note != note2

@pytest.mark.parametrize("note_str,expected_relative_major", [
    ("C","Eb"), 
    ("G","Bb"),
    ("D","F"),
    ("C#","E"),
    ("Db","Fb"),
    ("F#","A"),
    ("B","D"),
])
def test_the_relative_major_is_3_semitones_above(note_str, expected_relative_major):
    note = Note(note_str)

    relative_major = note.relative_major

    assert relative_major == Note(expected_relative_major)
