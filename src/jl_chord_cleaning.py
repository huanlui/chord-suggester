import pandas as pd
from jl_song_data import SongData
from jl_chord_scraping import ChordExtractor

class ChordDatasetCleaner:
    def clean_dataset(self,df, raw_html_output):
        df = (df
          .groupby(['url', 'name', 'decade'])
          .agg({'genre': self.genres, 'chords': self.chords, 'uuid':self.uuid }))
        
        df = df.reset_index()
        
        with_chords = df[df["chords"].notnull()]
        
        without_chords = df[df["chords"].isnull()]
        with_chords_filled = self.fill_songs_without_chords(without_chords, raw_html_output)

        final = pd.concat([with_chords, with_chords_filled])
        
        return final
        
    def fill_songs_without_chords(self,without_chords, raw_html_output):
        song_data = SongData(df=without_chords)
        extractor = ChordExtractor(raw_html_output)
        print(f'Re extracting chords for {len(without_chords)} songs')
        for index,url in enumerate(without_chords['url']):
            print(f'{index}. {url}')
            try:
                chords = extractor.extract_song_data(url)
                song_data.add_details(chords)
            except Exception as e: 
                print(f'Error in {url}. {e}')
    
        return song_data.df[song_data.df["chords"].notnull()] # discard songs with error
        
    def genres(self,series):
        return series.str.cat(sep='%%')

    def extract_single_not_null(self,series):
        no_nulls = series[series.notnull()].unique()

        if len(no_nulls) > 1:
            raise Exception(f'More than one different (and non null) elements: {no_nulls}. ')

        if len(no_nulls) == 0:
            return None

        return no_nulls[0]

    def chords(self,series):
        return self.extract_single_not_null(series)

    def uuid(self,series):
        return self.extract_single_not_null(series)
        
    