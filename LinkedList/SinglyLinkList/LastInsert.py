class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head 
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode


    def printList(self):
        currrentNode=self.head
        while True:
            if currrentNode is None:
                break
            print(currrentNode.data)
            currrentNode=currrentNode.next


firstNode=Node("John")
linkedlist=LinkedList()
linkedlist.insert(firstNode)
secondNode=Node("Suman")
linkedlist.insert(secondNode)
thirdNode=Node("Mathew")
linkedlist.insert(thirdNode)
linkedlist.printList()
