from pychord_jl.constants.scales import NOTE_VAL_DICT, VAL_NOTE_DICT
from math import cos,sin,pi
import jl_constants as constants

class Note:
    def __init__(self, str_value):
        self.str_value = str_value
        self.pychord_value = NOTE_VAL_DICT[str_value]

    @staticmethod
    def from_Music21_name(note_name):
        return Note(note_name[:-1])

    @staticmethod
    def from_pychord_value(pychord_value):
        return Note(VAL_NOTE_DICT[pychord_value][0])

    @property
    def position_in_5th_circle(self):
        return (self.pychord_value * 7) % 12

    @property
    def angle_in_5th_circle_degrees(self):
        return self.position_in_5th_circle * constants.STEP_ANGLE

    # https://towardsdatascience.com/feature-engineering-time-3934038e0dbe
    @property
    def x_y_in_5th_circle(self):
        angle_radians = (self.angle_in_5th_circle_degrees * pi) / 180

        return (
            sin(angle_radians),
            cos(angle_radians)
        )

    @property
    def relative_major(self):
        relative_major_value = (self.pychord_value + 3) % constants.NUMBER_OF_NOTES
        return Note(VAL_NOTE_DICT[relative_major_value][0])

    @property
    def complementary(self):
        return None
    
    def __sub__(self,other):
        self_x_y = self.x_y_in_5th_circle
        other_x_y = other.x_y_in_5th_circle

        return (
            self_x_y[0] - other_x_y[0],
            self_x_y[1] - other_x_y[1],
        )
    
    def __repr__(self):
        return f"{self.str_value}-{self.pychord_value}"

    def __str__(self):
        return self.str_value

    def __hash__(self):
        return hash(self.pychord_value)

    def __eq__(self, other):
        return (
             self.__class__ == other.__class__ and
             self.pychord_value == other.pychord_value
         )

