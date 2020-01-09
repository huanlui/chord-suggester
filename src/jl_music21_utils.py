from music21.chord import Chord
from music21.stream import Stream

def show_sequence(chord_sequence):
    stream = Stream()

    chord_names = [chord.standard_name for chord in chord_sequence]
    
    print(chord_names)
    chord_sequence = [chord_sequence[0], *chord_sequence] # to solve a music21 problem

    for extended_chord in chord_sequence:
        chord = Chord(notes=extended_chord.components, type='whole')
        stream.append(chord)

    stream.show()
    stream.show('midi')