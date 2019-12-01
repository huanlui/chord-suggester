
import pickle

def to_file(obj, path):
    with open(path, 'wb') as file:
          pickle.dump(obj, file) 
            
def from_file(path):
    with open(path, 'rb') as file:
        return pickle.load(file)    
