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
    def relative_on(self):
        diff = NOTE_VAL_DICT[self.pytest_chord.on] - NOTE_VAL_DICT[self.pytest_chord.root]

        return diff if diff > 0 else self.NUMBER_OF_SEMITONES + diff

