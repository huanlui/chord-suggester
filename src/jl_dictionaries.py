from pychord_jl.constants import QUALITY_DICT
from pychord_jl.constants.scales import NOTE_VAL_DICT, VAL_NOTE_DICT

def calculate_reverse_qualities_dict():
    reverse_qualities_dict = {}
    for key,value in QUALITY_DICT.items():
        if value not in reverse_qualities_dict.keys():
            reverse_qualities_dict[value] = key

    return reverse_qualities_dict

def calculate_all_possilbe_chords(reverse_qualities_dict):
    notes = [note_names[0] for note_names in VAL_NOTE_DICT.values()]
    qualities = reverse_qualities_dict.values()

    possible_chords = []
    for note in notes:
        for quality in qualities:
            possible_chords.append(f'{note}{quality}')     

    return possible_chords

class Dictionaries:
    reverse_qualities_dict = calculate_reverse_qualities_dict()
    all_possible_chords = calculate_all_possilbe_chords(reverse_qualities_dict)

    @classmethod
    def get_quality_name(cls,quality_components):
        return cls.reverse_qualities_dict[quality_components]

    @classmethod
    def get_quality_components(cls,quality_name):
        return QUALITY_DICT[quality_name]

    @classmethod
    def get_note_name(cls,note_value):
        return VAL_NOTE_DICT[note_value][0]

    @classmethod
    def get_note_value(cls,note_name):
        return NOTE_VAL_DICT[note_name]

    @classmethod
    def get_all_possible_chords(cls):
        return cls.all_possible_chords


