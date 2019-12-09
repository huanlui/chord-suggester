import pandas as pd 
import os

class SongData:
    SEPARATOR = '^'
    
    def __init__(self, initial_data_path=None, df=None):
        self.df = pd.DataFrame(data=[], columns=['url','name','genre','decade','chords','uuid'])
        
        if initial_data_path is not None and os.path.isfile(initial_data_path):
            self.df = pd.read_csv(initial_data_path, sep=self.SEPARATOR)
        
        if df is not None:
            self.df = df
            
    def add_basic_data(self,basic_data):
        self.df = self.df.append(basic_data,ignore_index=True)

    def add_details(self,details):
        self.df.loc[self.df['url'] == details["url"], ["chords"]] = str(details["chords"])
        self.df.loc[self.df['url'] == details["url"], ["uuid"]] = details["uuid"]
        
    def has_basic_data(self,url):
        return (self.df['url'] == url).any()
    
    def has_chords(self,url):
        return ((self.df['url'] == url) & (self.df['chords'].notnull())).any()
        
    def get_chords(self,url):
        return eval( self.df[self.df['url'] == url]['chords'][0])
    
    def has_genre_and_decade(self, genre, decade):
        return ((self.df['genre'] == genre) & (self.df['decade'] == decade)).any()
    
    def save(self, path):
        self.df.to_csv(path,index=False,sep=self.SEPARATOR)
