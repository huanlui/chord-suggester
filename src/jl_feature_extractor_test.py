import pytest
from jl_feature_extractor import FeatureExtractor
from jl_extended_chord import ChordMode

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

    cardinality = extractor.extract_cardinality(chords)

    assert cardinality == expected_cardinality

@pytest.mark.parametrize("chords,expected_unique_cardinality", [
    (["C#"],1), 
    (["C#", "D"],2), 
    (["C#", "E", "E"],2), 
    (["C#", "E", "E", "F", "C#m", "C#"],4),
    ([],0), 
])
def test_extracts_unique_cardinality(chords, expected_unique_cardinality):
    extractor = FeatureExtractor()

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

    mode_cardinality = extractor.extract_mode_cardinality(chords, mode)

    assert mode_cardinality == expected_mode_cardinality 