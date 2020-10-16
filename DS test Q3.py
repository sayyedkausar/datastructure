class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('stavk is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('stavk is empty')
        return self._data.pop()

    def display(self):
        return self._data


s = Stack()
print(s.__len__())
print(s.is_empty())
s.push(1)
s.push(3)
s.push(5)
s.push(8)
print(s.display())
print(s.top())
s.pop()
s.pop()
print(s.display())

print(s.__len__())
print(s.is_empty())
