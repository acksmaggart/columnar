from columnar import columnar
from click import style

data = [
    ['Omloop Het Nieuwsblad', 'Saturday 2nd March', 'Gent, Belgium', "Men's - 200km / Women's - 130km"],
    ['Strade Bianche', 'Saturday 9th March', 'Tuscany, Italy', "Men's - 176km / Women's - 103km. Both men's and women's "],
    ['Milan-San Remo', 'Saturday 23rd March', 'Milan to San Remo, Italy', '295km'],
    ['Tour of Flanders', 'Sunday 7th April', 'Antwerp to Oudenaarde, Flanders region, Belgium', '260km'],
    ['Omloop Het Nieuwsblad', 'Saturday 2nd March', 'Gent, Belgium', "Men's - 200km / Women's - 130km"],
    ['Strade Bianche', 'Saturday 9th March', 'Tuscany, Italy', "Men's - 176km / Women's - 103km. Both men's and women's "],
    ['Milan-San Remo', 'Saturday 23rd March', 'Milan to San Remo, Italy', '295km'],
    ['Tour of Flanders', 'Sunday 7th April', 'Antwerp to Oudenaarde, Flanders region, Belgium', '260km'],
    ['Omloop Het Nieuwsblad', 'Saturday 2nd March', 'Gent, Belgium', "Men's - 200km / Women's - 130km"],
    ['Strade Bianche', 'Saturday 9th March', 'Tuscany, Italy', "Men's - 176km / Women's - 103km. Both men's and women's "],
    ['Milan-San Remo', 'Saturday 23rd March', 'Milan to San Remo, Italy', '295km'],
    ['Tour of Flanders', 'Sunday 7th April But this one is really long to make sure it takes up at least one column, hopefully two if we are lucky But this one is really long to make sure it takes up at least one column, hopefully two if we are lucky But this one is really long to make sure it takes up at least one column, hopefully two if we are lucky', 'Antwerp to Oudenaarde, Flanders region, Belgium', '260km'],
    ['Omloop Het Nieuwsblad', 'Saturday 2nd March', 'Gent, Belgium', "Men's - 200km / Women's - 130km"],
    ['Strade Bianche', 'Saturday 9th March', 'Tuscany, Italy', "Men's - 176km / Women's - 103km. Both men's and women's "],
    ['Milan-San Remo', 'Saturday 23rd March', 'Milan to San Remo, Italy', '295km'],
    ['Tour of Flanders', 'Sunday 7th April', 'Antwerp to Oudenaarde, Flanders region, Belgium', '260km'],
]

patterns = [
    ('Saturday.+', lambda text: style(text, fg='white', bg='blue')),
    ('\d+km', lambda text: style(text, fg='cyan')),
    ('Omloop Het Nieuwsblad', lambda text: style(text, fg='green')),
    ('Strade Bianche', lambda text: style(text, fg='white')),
    ('Milan-San Remo', lambda text: style(text, fg='red')),
    ('Tour of Flanders', lambda text: style(text, fg='yellow')),
]

table = columnar(data, 
    headers=['Race', 'Date', 'Location', 'Distance'], 
    patterns=patterns,
    justify=['l', 'r', 'c', 'l'],
    min_column_width=55,
    no_borders=True,
    preformatted_headers=True,
)
print(table)
