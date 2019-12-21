from pychord_jl.constants.scales import NOTE_VAL_DICT

class Note:
    def __init__(self, str_value):
        self.str_value = str_value
        self.pychord_value = NOTE_VAL_DICT[str_value]

    @property
    def position_in_5th_circle(self):
        return (self.pychord_value * 7) % 12
