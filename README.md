# Columnar

A library for creating columnar output strings using data as input.

## Installation 
```
pip install columnar
```

## Example
```python
from columnar import columnar
from click import style

data = [
    ['Omloop Het Nieuwsblad', 'Saturday 2nd March', 'Gent, Belgium', "Men's - 200km / Women's - 130km"],
    ['Strade Bianche', 'Saturday 9th March', 'Tuscany, Italy', "Men's - 176km / Women's - 103km. Both men's and women's "],
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

table = columnar(data, headers=['Race', 'Date', 'Location', 'Distance'], transformation_patterns=patterns)
print(table)
```
![Table Displaying Spring Classics](https://github.com/MaxTaggart/columnar/raw/master/columnar/images/example_spring_classics.png)


## Column Sizing Algorithm
There are an infiniate number of ways to determine column sizing and text wrapping given a dataset. This package allows the user to specify a minimum column width, a maximum column width, and a "wrap max" which parameterized wrapping and column sizing. The rest of the logic that goes into determining how to fit data into a table when the data is wider than the terminal employs a pretty simple heuristic. First determine how wide each column wants to be without wrapping. If all the columns are too wide to fit on the screen, shrink as many columns as are needed in order for the table to fit, starting with the widest column and progressing through the columns from largest to smallest. If the size of columns falls below the minimum column width then raise an exception.


## Text Wrapping
The contents of a column are wrapped as needed to fit in the column with no effort made to split on spaces. The maximum number of times the contents of a column are wrapped before being truncated is given by `wrap_max`. Another way to think about `wrap_max` is that `wrap_max + 1` is the maximum number of rows a single cell can occupy. Any content past the `wrap_max + 1`th row is truncated.