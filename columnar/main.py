import os
import io
import operator
from functools import reduce
from itertools import zip_longest
from collections import namedtuple

class Columnar():

    def __call__(self, data, headers, head=0, justify='left', wrap_max=5, max_column_width=0, 
                min_column_width=5, row_sep='-', column_sep='|'):
        self.wrap_max = wrap_max
        self.max_column_width = max_column_width
        self.min_column_width = min_column_width
        self.justify = justify
        self.head = head
        self.terminal_width = os.get_terminal_size().columns
        self.row_sep = row_sep
        self.column_sep = column_sep
        

        logical_rows = self.convert_data_to_logical_rows([headers] + data)
        column_widths = self.get_column_widths(logical_rows)
        truncated_rows = self.wrap_and_truncate_logical_cells(logical_rows, column_widths)
        
        justification_map = {
            'left': lambda text, width: text.ljust(width),
            'center': lambda text, width: text.center(width),
            'right': lambda text, width: text.rjust(width)
        }
        justifications = []
        if type(justify) is str:
            justifications = [justification_map[justify]] * len(column_widths)
        else:
            justifications = [justification_map[spec] for spec in justifications]

        table_width = sum(column_widths) + ((len(column_widths) + 1) * len(row_sep))
        out = io.StringIO()
        for lrow in truncated_rows:
            for row in lrow:
                justified_row_parts = [justifier(text, width) for text, justifier, width in zip(row, justifications, column_widths)]
                # out.write(self.column_sep + self.column_sep.join(justified_row_parts) + self.column_sep + '\n')
                out.write(self.column_sep.join(justified_row_parts) + '\n')
            out.write(self.row_sep * table_width + '\n')
        return out.getvalue()


    def convert_data_to_logical_rows(self, full_data):
        """
        Takes a list of lists of items. Returns a list of logical rows, where each logical
        row is a list of lists, where each sub-list in a logical row is a physical row to be
        printed to the screen. There will only be more than one phyical row in a logical
        row if one of the columns wraps past one line.
        """
        logical_rows = []
        for row in full_data:
            cells_varying_lengths = []
            for cell in row:
                lines = str(cell).split('\n')
                cells_varying_lengths.append(lines)
            cells = [[cell_text or '' for cell_text in physical_row] for physical_row in zip_longest(*cells_varying_lengths)]
            logical_rows.append(cells)
        return logical_rows


    def distribute_between(self, diff, columns, n):
        subset = columns[:n]
        width = sum([column['width'] for column in subset])
        remainder = width - diff 
        new_width = remainder // n
        for i in range(n): columns[i]['width'] = new_width
        return columns

    def widths_sorted_by(self, columns, key):
        return [column['width'] for column in sorted(columns, key=lambda x: x[key])]

    def current_table_width(self, columns):
        return sum([len(self.column_sep) + column['width'] for column in columns]) + len(self.column_sep)


    def get_column_widths(self, logical_rows):
        """
        Calculated column widths, taking into account the terminal width,
        the number of columns, and the column seperators that will be used
        to delimit columns.
        """
        # terminal_width = os.get_terminal_size().columns

        max_widths = []
        for column in zip(*reduce(operator.add, logical_rows)):
            lengths = [len(cell) for cell in column]
            max_natural = max(lengths)
            max_width = max_natural if self.max_column_width == 0 else min(max_natural, self.max_column_width)
            max_widths.append(max_width)

        columns = sorted([{'column_no' : no, 'width': width} for no, width in enumerate(max_widths)], key=lambda x: x['width'], reverse=True)
        if self.current_table_width(columns) <= self.terminal_width:
            return self.widths_sorted_by(columns, 'column_no')

        # the table needs to be narrowed
        for i in range(len(columns)): 
            # include the next largest column in the size reduction
            diff = self.current_table_width(columns) - self.terminal_width
            columns = self.distribute_between(diff, columns, i + 1)
            if i < len(columns) - 1 and columns[0]['width'] < columns[i + 1]['width']:
                # if the columns that were just shrunk are smaller than the next largest column,
                # keep distributing the size so we have evenly-shrunken columns
                continue
            elif columns[0]['width'] >= self.min_column_width and self.current_table_width(columns) <= self.terminal_width:
                return self.widths_sorted_by(columns, 'column_no')
                
        raise ValueError("Could not fit table in current terminal, try reducing the number of columns.")

            
        
    def wrap_and_truncate_logical_cells(self, logical_rows, column_widths):
        lrows_out = []
        for lrow in logical_rows:
            cells_out = []
            # for cell in map(lambda column_cells: reduce(lambda cell_list, cell: cell_list + [cell], column_cells, []), zip(*lrow)):
            for cell, width in zip(map(list, zip(*lrow)), column_widths):
                # at this point `cell` is a list of strings, representing each line of the cell's contents
                cell_out = []
                for line in cell:
                    while len(line) > width:
                        cell_out.append(line[:width])
                        line = line[width:]

                    cell_out.append(line)
                cells_out.append(cell_out[:self.wrap_max])
            cells_out_padded = [[text or '' for text in line] for line in zip_longest(*cells_out)]
            lrows_out.append(cells_out_padded)
        return lrows_out