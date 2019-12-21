import pytest
from jl_note import Note

@pytest.mark.parametrize("note_str,expected_pychord_value", [
    ("C",0), 
    ("G",7),
    ("D",2),
    ("C#",1),
    ("Db",1),
    ("F#",6),
])
def test_should_store_its_corresponding_pychord_value(note_str, expected_pychord_value):
    note = Note(note_str)

    assert note.pychord_value == expected_pychord_value

@pytest.mark.parametrize("note_str,expected_position_in_5th_circle", [
    ("C",0), 
    ("G",1),
    ("D",2),
    ("C#",7),
    ("Db",7),
    ("F#",6),
])
def test_should_store_its_corresponding_position_in_5th_circle(note_str, expected_position_in_5th_circle):
    note = Note(note_str)

    assert note.position_in_5th_circle == expected_position_in_5th_circle
