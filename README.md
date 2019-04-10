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

table = columnar(data, headers=['Race', 'Date', 'Location', 'Distance'], patterns=patterns)
print(table)
```
![Table Displaying Spring Classics](https://github.com/MaxTaggart/columnar/raw/master/columnar/images/example_spring_classics.png)

Or for that fresh Docker look:

```python
from columnar import columnar

headers = ['name', 'id', 'host', 'notes']

data = [
    ['busybox', 'c3c37d5d-38d2-409f-8d02-600fd9d51239', 'linuxnode-1-292735', 'Test server.'],
    ['alpine-python', '6bb77855-0fda-45a9-b553-e19e1a795f1e', 'linuxnode-2-249253', 'The one that runs python.'],
    ['redis', 'afb648ba-ac97-4fb2-8953-9a5b5f39663e', 'linuxnode-3-3416918', 'For queues and stuff.'],
    ['app-server', 'b866cd0f-bf80-40c7-84e3-c40891ec68f9', 'linuxnode-4-295918', 'A popular destination.'],
    ['nginx', '76fea0f0-aa53-4911-b7e4-fae28c2e469b', 'linuxnode-5-292735', 'Traffic Cop'],
]

table = columnar(data, headers, no_borders=True)
print(table)
```

[Table Displaying No-border Style](https://github.com/MaxTaggart/columnar/raw/master/columnar/images/example_no_borders.png)


## Patterns
Columnar supports patterns, which are two-item tuples each containing a regular expression and a function. The regular expression is applied to each item in `data` using `re.search()` and if there is a match the corresponding function is applied to the text of that element. Only the first matching pattern is applied, meaning patterns can be prioritized by their order in the input array. This can be used to perform colorization, casing, or other custom tasks that will affect the display of the text in the table.


## Color Support
As noted above, color may be applied to text by adding it to the text through a pattern. However, text may also be pre-colored by applying ANSI color codes to the text before it is passed to `columnar` as made easy by libraries like `click` and `colorama`. Note however, that any color that is applied will be applied to the contents of the whole cell. For example, if the text for a cell is 
```python
f"unmodified text {click.style('modified text', fg='blue')} more unmodified text"
```
the entire cell's text will be turned blue.


## Selecting Columns
If your table has a large number of columns, or you wish to highlight a subset of the columns use the `select` keyword argument. It takes a list of strings which are compiled to regular expressions using `re.compile(arg, re.I)` and used to select columns using `pattern.search(column_name)`. For example, given the following columns

```
['Name', 'BirthDate', 'Zip Code', 'City Code', 'County Code']
```

using `select=['name', '.*code']` will select all columns except the `BirthDate` column.

## Dropping Columns
It is often the case that one or more columns of the data will not be useful. For example, columns where all the values are "Null" or "-". To filter out these columns use the `drop` keyword argument. This argument takes a list of values and drops any column whose contents are a subset of those values. For example, given four columns

```
a   NA  1   -
b   NA  2   Null
-   NA  3   -
d   NA  4   None
```

using `drop=['-', 'Null', 'NA', 'None']` will drop the second and fourth columns, even though the first column contains a dash also.


## Column Sizing Algorithm
There are an infinite number of ways to determine column sizing and text wrapping given a dataset. This package allows the user to specify a minimum column width, a maximum column width, and a "wrap max" which partially define wrapping and column sizing. The rest of the logic that goes into determining how to fit data into a table when the data is wider than the terminal employs a pretty simple heuristic. First determine how wide each column wants to be without wrapping. If all the columns are too wide to fit on the screen, shrink as many columns as are needed in order for the table to fit, starting with the widest column and progressing through the columns from largest to smallest. If the size of the columns falls below the minimum column width then raise an exception. This should only happen if there are so many columns that `terminal_width / num_columns` is less than the minimum column width.


## Text Wrapping
The contents of a column are wrapped as needed to fit in the column with no effort made to split on spaces. The maximum number of times the contents of a column are wrapped before being truncated is given by `wrap_max`. Another way to think about `wrap_max` is that `wrap_max + 1` is the maximum number of rows a single cell can occupy. Any content past the `wrap_max + 1`th row is truncated.