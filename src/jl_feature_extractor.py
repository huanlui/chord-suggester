from jl_chord_parser import ChordParser
from jl_extended_chord import ChordMode
import statistics 
from math import atan2, pi

class FeatureExtractor:
    def __init__(self):
        self.parser = ChordParser()

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

    def extract_cardinality(self,chords):
        return len(chords)

    def extract_unique_cardinality(self,chords):
        return len(set(chords))

    def extract_mode_cardinality(self,chords,mode):
        extended_chords = [self.parser.parse(chord) for chord in chords]

        return len([chord for chord in extended_chords if chord.mode == mode ])

    def extract_harmonic_mean(self, chords): 
        extended_chords = [self.parser.parse(chord) for chord in chords]

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

        if angle_degrees < 0:
            angle_degrees = 360 + angle_degrees

        return angle_degrees / 30
