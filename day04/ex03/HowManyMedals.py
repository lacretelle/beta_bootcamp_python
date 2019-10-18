from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../athlete_events.csv')

def howManyMedals(df, name):
    #print(data['Name'].head(30))
    med = data['Medal']
    print()
    dt = data[(data['Name'] == name)]
    print(dt)
    return

howManyMedals(data, 'John Aalberg')
