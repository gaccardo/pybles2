from pybles2.src import exceptions


class Pyble(object):

    def __init__(self, title=None, columns=list(), lines=list(),
                 line_token="-", column_token="#"):
        self.title = title
        self.columns = columns
        self.lines = lines
        self.line_token = line_token
        self.column_token = column_token

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_columns(self, columns):
        if self.columns == list():
            self.columns = columns
        else:
            raise exceptions.ColumnsAlreadySet

    def get_columns(self):
        return self.columns

    def add_line(self, line):
        if len(line) == len(self.columns):
            self.lines.append(line)
        else:
            raise exceptions.ColumnsNumberDoesNotMatch

    def get_lines(self):
        return self.lines

    def get_columns_width(self):
        widths = dict()
        to_measure = self.lines
        to_measure.append(self.columns)
        for i in range(len(self.columns)):
            for line in to_measure:
                if i in widths.keys():
                    if widths[i] < len(line[i]):
                        widths[i] = len(line[i])
                else:
                    widths[i] = len(line[i])

        for i, k in widths.iteritems():
            widths[i] = widths[i] + len(self.columns) * 2

        return widths

    def get_title_width(self):
        columns_width = self.get_columns_width()
        total = 0
        for i, k in columns_width.iteritems():
            total += columns_width[i]

        return total

if __name__ == "__main__":
    pb = Pyble()
    pb.set_title("this is a title")
    pb.set_columns(['columna', 'columnb'])
    pb.add_line(['1234234234', '234'])
    print pb.get_columns_width()
    print pb.get_title_width()
