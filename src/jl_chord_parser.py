from pychord_jl import Chord
from pychord_jl.constants.scales import NOTE_VAL_DICT

class Note:
    def __init__(self, str_value):
        self.str_value = str_value
        self.pychord_value = NOTE_VAL_DICT[str_value]

    @property
    def position_in_5th_circle(self):
        return (self.pychord_value * 7) % 12

class ChordParser:

    def parse(self,input):
        input = self.replace_german_system(input)
        input = self.replace_6_9(input)
        input = self.replace_enharmonic(input)
        input = self.replace_errors(input)

        try:
            return Chord(input)
        except:
            return None

    def replace_german_system(self,input):
        if input[0] == 'H':
            return 'Bb' + input[1:]

        return input

    def replace_6_9(self,input):
        return (input
                .replace('6/9', '6_9')
                .replace('7/9', '7_9')
                .replace('7/5', '7_5')
                .replace('7/6', '7_6')
                )

    def replace_enharmonic(self,input):
        return (input
                .replace('E#', 'F')
                .replace('B#', 'C')
                .replace('Fb', 'E')
                .replace('Cb', 'B')
                )

    def replace_errors(self,input):
        return (input
                .replace('G(2)', 'G')
                .replace('A*', 'A')
                .replace('(III)', '')
                .replace('Gm#', 'G#m')
                .replace('Fm#', 'F#m')
                .replace('Am#', 'A#m')
                )


