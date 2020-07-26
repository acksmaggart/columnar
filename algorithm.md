<!--
SPDX-FileCopyrightText: 2019 Max Taggart

SPDX-License-Identifier: MIT
-->

if the columns do not all fit, calculate the amount that you would need to subtract from the largest column to make the table fit. if this number is less than 2 times the column delimeter, or is smaller than the next widest column, then distribute the amount between the two largest columns, if this makes them less than 3 times the column delimiter or less than the third largest column, distribute the amount between the four largest columns, etc. The end condition is reached when distributing the reduction between columns leads to a table that will fit in the terminal, or the table collapses down to be less than ncolumns + 1 wide, meaning that it would then contain only column delimiters.
Ideally when a suitable table size is found, the columns would be sized to utiltize the whole width of the screen.
