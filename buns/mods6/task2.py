class DoubleElement:
    def __init__(self, *lst):
        self.data = list(lst)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        first_element = self.data[self.index]
        self.index += 1

        if self.index >= len(self.data):
            return first_element, None
        else:
            second_element = self.data[self.index]
            self.index += 1
            return first_element, second_element

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
