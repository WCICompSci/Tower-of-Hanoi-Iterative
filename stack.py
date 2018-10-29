# stack.py
# David Gurevich
# October 26, 2018

class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_legal(self, other):
        try:
            return self.peek() < other.peek()
        except IndexError:
            return False

    def get_name(self):
        return self.name

    def disk_move(self, other):
        if not self.is_empty() and (other.is_empty() or self.is_legal(other)):
            other.push(self.pop())
        elif not other.is_empty() and (self.is_empty() or other.is_legal(self)):
            self.push(other.pop())

    def print_tower(self, i, num_of_disks):
        k = ((2 * num_of_disks) - 2) - (0 if i < 0 else i) # Number of spaces
        middle_char = "|"
        print(((" " * k)+ ("=" *i) + middle_char + ("=" * i) +(" " * k)).ljust(num_of_disks + 2), end=" ")

    def __str__(self):
        return str(self.items)
