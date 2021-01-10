#stack by list

class stack(list):
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()


    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

# stack by singlely linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack_singly_linked:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data

    def is_empty(self):
        if self.head:
            return False
        return True

    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data

if __name__=="__main__":
    #s = stack()
    s2 = Stack_singly_linked()
    s2.push(1)
    s2.push(2)
    s2.push(3)

    print(s2.peek())
    print(s2.pop())
    print(s2.pop())
    print(s2.pop())
    print(s2.pop())
