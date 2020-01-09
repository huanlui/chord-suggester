import pytest
from pytest import approx
from jl_feature_extractor import FeatureExtractor
from jl_extended_chord import ChordMode
from math import atan2, pi
from jl_chord_parser import ChordParser

parse = ChordParser().parse

@pytest.mark.parametrize("raw_url,expected_artist", [
    ("https://tabs.ultimate-guitar.com/tab/1055161","Unknown"), 
    ("https://tabs.ultimate-guitar.com/tab/daVid-bowiE/space oddity","David Bowie"), 
    ("https://tabs.ultimate-guitar.com/tab/rollinG-StonES/12312","Rolling Stones"), 
])
def test_extracts_artist_from_url(raw_url, expected_artist):
    extractor = FeatureExtractor()

    artist = extractor.extract_pretty_artist(raw_url)

    assert artist == expected_artist


@pytest.mark.parametrize("input,expected_decade_as_number", [
    ("1950s",1950), 
    ("1960s",1960), 
    ("1970s",1970), 
    ("1980s",1980), 
    ("1990s",1990), 
    ("2000s",2000), 
    ("2010s",2010), 
])
def test_extracts_numeric_from_string_decade(input, expected_decade_as_number):
    extractor = FeatureExtractor()

    numeric_decade = extractor.extract_numeric_decade(input)

    assert numeric_decade == expected_decade_as_number

@pytest.mark.parametrize("chords,expected_cardinality", [
    (["C#"],1), 
    (["C#", "D"],2), 
    (["C#", "E", "E"],3), 
    ([],0), 
])
def test_extracts_cardinality(chords, expected_cardinality):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    cardinality = extractor.extract_cardinality(chords)

    assert cardinality == expected_cardinality

@pytest.mark.parametrize("chords,expected_unique_cardinality", [
    (["C#"],1), 
    (["C#", "D"],2), 
    (["C#", "E", "E"],2), 
    (["C#", "Emaj", "E"],2), 
    (["C#", "E", "E", "F", "C#m", "C#"],4),
    ([],0), 
])
def test_extracts_unique_cardinality(chords, expected_unique_cardinality):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    unique_cardinality = extractor.extract_unique_cardinality(chords)

    assert unique_cardinality == expected_unique_cardinality

@pytest.mark.parametrize("chords,mode,expected_mode_cardinality", [
    (["C#", "Em", "E", "F", "C#m", "C#", "C5"], ChordMode.Major, 4),
    (["C#", "Em", "E", "F", "C#m", "C#", "C5"], ChordMode.Minor, 2),
    (["C#", "Em", "E", "F", "C#m", "C#", "C5"], ChordMode.Neutral, 1),
    (["C#m", "E7", "Em", "Gm", "CbM7", "D5", "C5"],ChordMode.Major,2),
    (["C#m", "E7", "Em", "Gm", "CbM7", "D5", "C5"],ChordMode.Minor,3),
    (["C#m", "E7", "Em", "Gm", "CbM7", "D5", "C5"],ChordMode.Neutral,2),
])
def test_extracts_mode_cardinality(chords,mode, expected_mode_cardinality):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    mode_cardinality = extractor.extract_mode_cardinality(chords, mode)

    assert mode_cardinality == expected_mode_cardinality 

@pytest.mark.parametrize("chords,expected_harmonic_mean_position", [
    (["C", "G", "C", "F", "G", "C"], 0.17),
     (['F#/G#', 'C#/G#', 'D#m/G#', 'C#/G#', 'F#/G#', 'C#/G#', 'G#m7', 'Am7', 'F', 'C', 'Em/B', 'D', 'F', 'E', 'Dm', 'C', 'Dm7/G', 'C', 'Am7', 'F', 'C', 'Em/B', 'D', 'F', 'Am/E', 'E', 'Dm', 'C', 'Dm7/G', 'C', 'C', 'C/G', 'C', 'C/G', 'Dm', 'Dm/C', 'G7/B', 'G7', 'Am', 'C/G', 'F', 'D9/F#', 'G', 'E7/G#', 'Am', 'Fm', 'F#/G#', 'C#/G#', 'D#m/G#', 'C#/G#', 'F#/G#', 'C#/G#', 'G#m7', 'Am7', 'F', 'C', 'Em/B', 'D', 'F', 'Am/E', 'E', 'Dm', 'C', 'Dm7/G', 'C', 'C', 'C/G', 'C', 'C/G', 'Dm', 'Dm/C', 'G7/B', 'G7', 'Am', 'C/G', 'F', 'D9/F#', 'G', 'E7/G#', 'Am', 'Fm', 'F#/G#', 'C#/G#', 'D#m/G#', 'C#/G#', 'F#/G#', 'C#/G#', 'G#m7', 'Am7', 'F', 'C', 'Em/B', 'D', 'F', 'Am/E', 'E', 'Dm', 'C', 'Dm7/G', 'C', 'Dm7/G', 'C', 'Dm7/G', 'C'], 11.94),
    (["C", "Am"], 0),
    (["D"], 2),
    (["C", "G", "C", "F", "G", "C", "F#"], 0.2),
     (["C", "G", "C", "F", "G", "C", "Db"], 0)
])
def test_extract_harmonic_mean_position(chords, expected_harmonic_mean_position):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    harmonic_mean_position = extractor.extract_harmonic_mean_position(chords)

    assert harmonic_mean_position == approx(expected_harmonic_mean_position,0.1)

@pytest.mark.parametrize("chords,expected_subdominant_width", [
     (["C", "G", "C", "F", "G", "C", "F#"], 1.2),
     (["C", "G", "C", "F", "G", "C", "Db"], 5.2),
     (["C"], 0)
])
def test_extract_harmonic_subdominant_width(chords, expected_subdominant_width):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    subdominant_width = extractor.extract_subdominant_width(chords)

    assert subdominant_width == approx(expected_subdominant_width,0.1)

@pytest.mark.parametrize("chords,expected_dominant_width", [
     (["C", "G", "C", "F", "G", "C", "F#"], 5.8),
     (["C", "G", "C", "F", "G", "C", "Db"], 1),
     (["C"], 0)
])
def test_extract_harmonic_dominant_width(chords, expected_dominant_width):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    dominant_width = extractor.extract_dominant_width(chords)

    assert dominant_width == approx(expected_dominant_width,0.1)

@pytest.mark.parametrize("chords,expected_complexity", [
     (["C", "G", "F#"], 3.33),
     (["C", "G7", "Cm"], 4.08),
     (["C11", "C9+11"], 5.44)
])
def test_extract_complexity(chords, expected_complexity):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    complexity = extractor.extract_complexity(chords)

    assert complexity == approx(expected_complexity,0.1)

@pytest.mark.parametrize('chords, expected_relative_on_list', [
    (['C/G', 'C/D', 'C/A', 'G/D', 'G/A'], [9,2,7]),
     (['G/A', 'F#/G' ], [1,2]),
     (['C', 'A'], [])
])
def test_extract_relative_on_list(chords, expected_relative_on_list):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    relative_on_list = extractor.extract_relative_on_list(chords)

    assert relative_on_list == expected_relative_on_list

@pytest.mark.parametrize('chords, semitones, expected_transposed_chords', [
    (['C', 'G', 'C'], 1, ['Db', 'Ab', 'Db']),
     (['C', 'G', 'C'], -1, ['B', 'F#', 'B']),
])
def test_extract_transposed_chords(chords, semitones, expected_transposed_chords):
    extractor = FeatureExtractor()
    chords = [parse(chord) for chord in chords]

    transposed_chords = extractor.extract_transposed_chords_names(chords, semitones)

    assert transposed_chords == expected_transposed_chords

@pytest.mark.parametrize('harmonic_mean_in_5th_circle, expected_harmonic_mean_in_scale', [
    (1,7),
    (-1,5),
    (1.2,7),
    (1.8,2),
    (-1.7,10),
])
def test_extract_harmonic_mean_in_scale(harmonic_mean_in_5th_circle, expected_harmonic_mean_in_scale):
    extractor = FeatureExtractor()

    harmonic_mean_in_scale = extractor.extract_harmonic_mean_in_scale(harmonic_mean_in_5th_circle)

    assert harmonic_mean_in_scale == expected_harmonic_mean_in_scale