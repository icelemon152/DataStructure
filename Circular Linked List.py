class SingleNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head:
            curn = self.head
            while curn.next != self.head:
                curn = curn.next
            curn.next = node
            node.next = self.head
        else:
            self.head = node
            node.next = self.head

    def removeData(self,data):
        curn = self.head.next
        prevn = self.head

        #When head should be deleted
        if self.head.data == data:
            while curn != self.head:
                prevn = curn
                curn = curn.next

            prevn.next = curn.next
            self.head = curn.next
            return

        while curn != self.head:
            if curn.data == data:
                prevn.next = curn.next
                return
            prevn = curn
            curn = curn.next
        return -1

    def removePosition(self,idx):
        if idx == 0:
            if self.head:
                if self.head.next:
                    curn = self.head.next
                    while curn.next != self.head:
                        curn = curn.next #curn = self.head
                    curn.next = self.head.next
                    self.head = self.head.next
                    return
                else:
                    self.head = None
                    return
        else:
            prevn = self.head
            curn = self.head.next
            cur_i = 1
            while curn != self.head:
                if cur_i == idx:
                    nextn = curn.next
                    prevn.next = nextn
                    return
                prevn = curn
                curn = curn.next
                cur_i += 1

            return -1
    def getDataIndex(self,data):
        idx = 0
        curn = self.head

        if curn.data == data:
            return idx

        idx += 1
        curn = curn.next
        while curn != self.head:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1

    def insertNodeAtIndex(self,idx,node):

        if idx == 0:
            if self.head:
                curn = self.head.next
                #cur_i = 1
                while curn.next != self.head:
                    curn = curn.next
                    #cur_i += 1

                node.next = self.head
                self.head = node
                curn.next = self.head
                return
            else:
                self.head = node
                self.head.next = self.head
                return
        cur_i = 1
        prevn = self.head
        curn = self.head.next

        while curn.next != self.head:
            if cur_i == idx:
                prevn.next = node
                node.next = curn
                return
            prevn = curn
            curn = curn.next
            cur_i += 1

        if cur_i == idx:
            #prevn = curn
            #curn = curn.next
            prevn.next = node
            node.next = curn
            return
        #Insert at the last
        elif cur_i + 1 == idx:
            prevn = curn
            curn = curn.next
            prevn.next = node
            node.next = curn
            return
        return -1

    def insertNodeAtData(self,data,node):
        idx = self.getDataIndex(data)
        if idx >= 0:
            self.insertNodeAtIndex(idx,node)
        else:
            return -1
    def print(self):
        curn = self.head
        string = ''

        while curn:
            string += str(curn.data)
            if curn.next:
                string += '->'
            if curn.next == self.head:
                string = '->' + string
                break
            curn = curn.next
        print(string)

if __name__ == "__main__":
    circular = CircularLinkedList()
    circular.append(SingleNode(1))
    circular.append(SingleNode(2))
    circular.append(SingleNode(3))
    circular.append(SingleNode(4))
    circular.append(SingleNode(5))
    circular.print()
    circular.insertNodeAtIndex(0, SingleNode(0))
    circular.print()
    circular.insertNodeAtData(5, SingleNode(6))
    circular.print()
    print('remove')
    circular.removePosition(5)
    circular.print()
