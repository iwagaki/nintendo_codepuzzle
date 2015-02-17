import sys

class Bars(list):
    def pos(self, i):
        if i >= len(self):
            i -= len(self)
        return i

    def nextvalue(self, i):
        count = 0
        table = [{ " ":" ", "i":"T", "T":"i", "I":"I" }, { " ":"i", "i":"I", "T":" ", "I":"T" }]

        if self[self.pos(i + 0)] in ["i", "I"]:
            count += 1
        if self[self.pos(i + 2)] in ["i", "I"]:
            count += 1

        return table[count % 2][self[self.pos(i + 1)]]

    def next(self):
        newline = [' '] * len(self)

        for i in range(len(self)):
            newline[self.pos(i + 1)] = self.nextvalue(i)

        self[:] = newline

        return self

    def __str__(self):
        return ''.join(self)
