class ExtendedInterval:
    COMPLEXITY_DICTIONARY = {
        0:0,
        1:10,
        2:8,
        3:5,
        4:4,
        5:2,
        6:11,
        7:1,
        8:6,
        9:3,
        10:7,
        11:9
    }

    def __init__(self,distance_in_semitones):
        self.distance_in_semitones = distance_in_semitones
        self.complexity = self.COMPLEXITY_DICTIONARY[distance_in_semitones]

  
