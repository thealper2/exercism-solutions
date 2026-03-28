class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        self._head = None
        self._length = 0

        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        return self._length

    def head(self):
        if self._length == 0:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        new_node = Node(value, self._head)
        self._head = new_node
        self._length += 1

    def pop(self):
        if self._length == 0:
            raise EmptyListException("The list is empty.")

        value = self._head.value()
        self._head = self._head.next()
        self._length -= 1
        return value

    def reversed(self):
        reversed_list = LinkedList()
        for value in self:
            reversed_list.push(value)
            
        return reversed_list
