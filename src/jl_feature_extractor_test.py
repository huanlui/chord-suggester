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