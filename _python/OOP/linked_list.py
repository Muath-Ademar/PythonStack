class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Slist:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def printValues(self):
        runner = self.head
        while runner !=None:
            print(f"{runner.value} ------>", end="" )
            runner=runner.next
        print("None")
        return self
    def add_to_back(self, val):
        new_node = Node(val)
        if self.head == None:
            self.add_to_front(val)
            return self
        runner = self.head
        while runner.next !=None:
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        if self.head == None:
            return self
        self.head = self.head.next
        return self
    def remove_from_back(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
        else:
            runner = self.head
            while runner.next.next != None:
                runner = runner.next
            runner.next = None
            return self
    def remove_val_beg(self, val):
        if self.head == None:
            return self
        if self.head.value == val:
            self.head = self.head.next 
            return self
    def MergeLists(self,newList):
        current = self.head 
        while current.next:
            current = current.next
        current.next = newList.head
        return self
    def mergeZigZag(self, newList):
        current = self.head
        current2 =newList.head
        while current:
            temp = current.next
            temp2 = current2.next
            current.next =current2
            current2.next = temp
            current = temp
            current2 = temp2
        return self


Mylist = Slist()
Mylist.add_to_back("Muath").add_to_back("ademar").add_to_back(1).add_to_back(2)
newList = Slist()
newList.add_to_back("Mike").add_to_back("robert").add_to_back(3).add_to_back(4)
Mylist.mergeZigZag(newList).printValues()

# Mylist.MergeLists(newList).printValues()






def zigzag(self, newList):
    current = self.head
    current2 = newList.head
    while current:
        temp1 = current.next
        temp2 = current2.next
        current.next = current2
        current2.next = temp1
        current = temp1
        current2 = temp2
    return self
    