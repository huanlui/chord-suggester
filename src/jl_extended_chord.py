from pychord_jl.constants.scales import NOTE_VAL_DICT
from jl_note import Note
class ExtendedChord:
    NUMBER_OF_SEMITONES = 12 
    def __init__(self,pytest_chord):
        self.pytest_chord = pytest_chord

    def __str__(self):
        return self.pytest_chord.__str__()

    @property
    def root(self):
        return Note(self.pytest_chord.root)

    @property
    def root_x(self):
        return Note(self.pytest_chord.root).x_y_in_5th_circle[0]

    @property
    def root_y(self):
        return Note(self.pytest_chord.root).x_y_in_5th_circle[1]

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
