from os import link
from platform import node


class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.key = None
        

class LinkedList():
    def __init__(self) -> None:
        self.head = None


    def Insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    def displayValues(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

def main():
    linkedList = LinkedList()
    linkedList.Insert("hari")
    linkedList.Insert("SUman")
    linkedList.Insert('Tech')
    linkedList.Insert('Harry')
    linkedList.displayValues()

if __name__ == '__main__':
    main()