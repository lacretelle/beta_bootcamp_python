from FileLoader import FileLoader
import numpy as np
#from YoungestFellah import youngestFellah

loader = FileLoader()
data = loader.load('../athlete_events.csv')
#print(data.keys())
index = data.index
col = data.columns
val = data.values
print(col)
df = data['Age']
filt = data['Year'] == '2004'
filf = data['Sex'] == 'F'
film = data['Sex'] == 'M'
resF = df.mask(filt & filf).min()
resH = df.mask(filt & film).min()
res = { 'f': resF, 'm': resH}
print(res)
#print(data[y & f])
#youngestFellah(data, 2004)
