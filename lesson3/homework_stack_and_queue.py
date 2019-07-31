class DataStructure:
    def __init__(self, max_size):
        self._data_set = []
        self._max_size = max_size

    def add_element(self, new_element):
        if not self.is_full():
            self._data_set.append(new_element)
        else:
            raise Exception(f"Your {self.__class__.__name__} is full!")

    def is_empty(self):
        return not self._data_set

    def is_full(self):
        return len(self._data_set) == self._max_size

    def remove_element(self):
        pass

    def get_element(self):
        pass


class Stack(DataStructure):
    def get_element(self):
        """simply return last added element of Stack"""
        if not self.is_empty():
            return self._data_set[-1]
        else:
            raise Exception("Your Stack is empty!")

    def remove_element(self):
        """return last added element of Stack and remove it from Stack"""
        if not self.is_empty():
            return self._data_set.pop()
        else:
            raise Exception("Your Stack is empty!")

    def __repr__(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            return f"Stack{tuple(self._data_set)}"


class Queue(DataStructure):
    def get_element(self):
        """simply return first added element of Queue"""
        if not self.is_empty():
            return self._data_set[-1]
        else:
            raise Exception("Your Stack is empty!")

    def remove_element(self):
        """return first added element of Queue and remove it from Queue"""
        if not self.is_empty():
            return self._data_set.pop(0)
        else:
            raise Exception("Your Queue is empty!")

    def __repr__(self):
        if self.is_empty():
            return "Empty Queue"
        else:
            return f"Queue{tuple(self._data_set)}"


stack = Stack(5)
print(stack)
print(stack.is_empty())
stack.add_element(1)
stack.add_element(2)
stack.add_element(3)
stack.add_element(4)
print(stack.remove_element())
print(stack)
stack.add_element(2)
print(stack)
print(stack.is_full())
stack.add_element(2)
print(stack.is_full())

queue = Queue(6)
print(queue)
queue.add_element(1)
queue.add_element(2)
queue.add_element(3)
queue.add_element(4)
print(queue.remove_element())
print(queue.remove_element())
print(queue)
queue.add_element(2)
print(queue)
