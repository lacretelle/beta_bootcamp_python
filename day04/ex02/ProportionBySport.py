from FileLoader import FileLoader

def proportionBySport(data, year, sport, sex):
    #count d'une selection'
    dt = data['Sport']
    dt = data[(data['Year'] == year) & (data['Sport'] == sport) & (data['Sex'] == sex)]
    compare = data[(data['Year'] == year) & (data['Sex'] == sex)]
    c1 = dt['Sex'].count()
    c2 = compare['Sex'].count()
    res = c1 / c2
    print(res)
    return res

loader = FileLoader()
data = loader.load('../athlete_events.csv')
proportionBySport(data, 2004, 'Tennis', 'F')
