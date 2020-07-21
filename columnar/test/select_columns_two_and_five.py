# SPDX-FileCopyrightText: 2019 Max Taggart
#
# SPDX-License-Identifier: MIT

from columnar import columnar
from click import style

headers = ['one', 'two', 'three', 'four', 'five']

data = [
    ['hi', '-', 'bye', 'None', 'stuff'],
    ['there', '-', 'how', 'None', 'other_stuff'],
    ['how', '-', 'are', 'None', 'third_stuff'],
]

table = columnar(data, headers, select=['two', 'fiv'])
print(table)
