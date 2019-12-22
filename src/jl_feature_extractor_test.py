import pytest
from jl_feature_extractor import FeatureExtractor

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