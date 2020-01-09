from jl_chord_parser import ChordParser
from jl_extended_chord import ChordMode
import statistics 
from math import atan2, pi
import jl_constants as constants

class FeatureExtractor:
    def __init__(self):
        self.parser = ChordParser()
    
    def extract_chord_object_list_removing_non_valid(self,chord_names_str):
        chord_names = eval(chord_names_str) # Data comes in string format, we must convert it to an array.
        extended_chords = [self.parser.parse(chord_name) for chord_name in chord_names] # parse returns non if chord is not valid
        valid_extended_chords = [chord for chord in extended_chords if chord is not None] 

        return valid_extended_chords

    def extract_raw_artist(self,url):
        plain_url = url.replace('https://tabs.ultimate-guitar.com/tab/','')
        splitted = plain_url.split('/')
        if len(splitted) == 1:
            return 'Unknown'
        
        if len(splitted) == 2:
            return splitted[0]
        
        raise Exception(f'Cannot extract artist from {url}. Splitted is {splitted}')
        
    def extract_pretty_artist(self,url):
        raw_artist = self.extract_raw_artist(url)
        raw_artist = raw_artist.replace('-','_')
        return " ".join([word.capitalize() for word in raw_artist.split('_')])

    def extract_numeric_decade(self,input):
        return int(input.replace('s',''))

    def extract_cardinality(self,extended_chords):
        return len(extended_chords)

    def extract_unique_cardinality(self,chords):
        return len(set([chord.standard_name for chord in chords]))

    def extract_mode_cardinality(self,extended_chords,mode):
        return len([chord for chord in extended_chords if chord.mode == mode ])

    def extract_harmonic_mean(self, extended_chords): 
        mean = lambda values: sum(values) / len(values)

        x = [chord.x_in_5th_circle for chord in extended_chords]
        y = [chord.y_in_5th_circle for chord in extended_chords]

        x_avg = statistics.mean(x)
        y_avg = statistics.mean(y)

        return (x_avg, y_avg)

    def extract_harmonic_mean_x(self,chords):
        return self.extract_harmonic_mean(chords)[0]

    def extract_harmonic_mean_y(self,chords):
        return self.extract_harmonic_mean(chords)[1]

    def extract_harmonic_mean_position(self, chords):
        mean = self.extract_harmonic_mean(chords)
        angle = atan2(mean[0], mean[1])

        angle_degrees = angle * 180 / pi

        if abs(angle_degrees) < 0.001:
            angle_degrees = 0

        if angle_degrees < 0:
            angle_degrees = 360 + angle_degrees


        return angle_degrees / constants.STEP_ANGLE

    def extract_harmonic_mean_in_scale(self, harmonic_mean_in_5th_circle):

        return (int(round(harmonic_mean_in_5th_circle)) * 7) % 12     

    def extract_subdominant_width(self, extended_chords):
        armonic_mean = self.extract_harmonic_mean_position(extended_chords)
        diffs = [substract_positions(armonic_mean,chord.note_in_5h_circle.position_in_5th_circle) \
                   for chord in extended_chords]

        diffs = [diff for diff in diffs if diff > 0] # onyly subdominant (positive difference)

        return max(diffs) if len(diffs) > 0 else 0

    def extract_dominant_width(self, extended_chords):
        armonic_mean = self.extract_harmonic_mean_position(extended_chords)
        diffs = [substract_positions(armonic_mean,chord.note_in_5h_circle.position_in_5th_circle) \
                   for chord in extended_chords]

        diffs = [diff for diff in diffs if diff < 0] # onyly dominant (positive difference)

        return abs(min(diffs)) if len(diffs) > 0 else 0

    def extract_complexity(self,extended_chords): 
        complexities = [chord.complexity for chord in extended_chords]

        return sum(complexities) / len(complexities)

    def extract_relative_on_list(self, extended_chords):
        relatives = [chord.relative_on for chord in extended_chords]

        relatives = [relative for relative in relatives if relative is not None]

        return list(set(relatives))

    def extract_transposed_chords_names(self, extended_chords, semitones):
        transposed = [chord.transpose(semitones).standard_name for chord in extended_chords]

        return transposed    

def substract_positions(position_1, position_2):
    diff = position_1 - position_2

    if abs(diff) > constants.NUMBER_OF_NOTES / 2:
        if diff < 0: 
            return diff + 12
        else:
            return diff - 12
    
    return diff






        

