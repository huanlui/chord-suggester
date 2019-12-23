from pychord_jl.constants.scales import NOTE_VAL_DICT
from jl_note import Note
from enum import Enum

class ChordMode(Enum):
    Neutral = 0
    Major = 1
    Minor = 2

class ExtendedChord:
    NUMBER_OF_SEMITONES = 12 
    MAJOR_INTERVAL = 4
    MINOR_INTERVAL = 3
    def __init__(self,pytest_chord):
        self.pytest_chord = pytest_chord

    def __str__(self):
        return self.pytest_chord.__str__()

    @property
    def root(self):
        return Note(self.pytest_chord.root)

    @property
    def mode(self):
        components = self.pytest_chord.quality.components
        if self.MAJOR_INTERVAL in components: return ChordMode.Major
        if self.MINOR_INTERVAL in components: return ChordMode.Minor

        return ChordMode.Neutral

    @property 
    def note_inf_5h_circle(self):
        root_note = Note(self.pytest_chord.root)

        return root_note if self.mode != ChordMode.Minor else root_note.relative_major

    @property
    def x_in_5th_circle(self):
        return self.note_inf_5h_circle.x_y_in_5th_circle[0]

    @property
    def y_in_5th_circle(self):
        return self.note_inf_5h_circle.x_y_in_5th_circle[1]

    @property
    def slash_bass(self):
        return Note(self.pytest_chord.on or self.pytest_chord.root)

    @property
    def relative_on(self):
        diff = NOTE_VAL_DICT[self.pytest_chord.on] - NOTE_VAL_DICT[self.pytest_chord.root]

        return diff if diff > 0 else self.NUMBER_OF_SEMITONES + diff

    @property
    def relative_slash_bass(self):
        return self.slash_bass - self.root

    @property
    def relative_slash_x(self):
        return self.relative_slash_bass[0]

    @property
    def relative_slash_y(self):
        return self.relative_slash_bass[1]

