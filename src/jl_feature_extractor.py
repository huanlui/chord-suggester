import pandas as pd

class FeatureExtractor:
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