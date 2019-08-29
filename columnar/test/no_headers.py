from columnar import columnar
from click import style

data = [
    ['Strade Bianche', 'Saturday 9th March', 'Tuscany, Italy', "Men's - 176km / Women's - 103km. Both men's and women's "],
    ['Omloop Het Nieuwsblad', 'Saturday 2nd March', 'Gent, Belgium', "Men's - 200km / Women's - 130km"],
    ['Milan-San Remo', 'Saturday 23rd March', 'Milan to San Remo, Italy', '295km'],
    ['Tour of Flanders', 'Sunday 7th April', 'Antwerp to Oudenaarde, Flanders region, Belgium', '260km']
]

patterns = [
    ('Saturday.+', lambda text: style(text, fg='white', bg='blue')),
    ('\d+km', lambda text: style(text, fg='cyan')),
    ('Omloop Het Nieuwsblad', lambda text: style(text, fg='green')),
    ('Strade Bianche', lambda text: style(text, fg='white')),
    ('Milan-San Remo', lambda text: style(text, fg='red')),
    ('Tour of Flanders', lambda text: style(text, fg='yellow')),
]

table = columnar(data, no_headers=True, patterns=patterns)
print(table)
