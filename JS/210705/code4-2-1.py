class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')


memory=[]
head, current, pre = None, None, None
# dataArray=['다현','정연','쯔위','사나','지효']
import random
dataArray=[random.randint(100,999) for _ in range(20)]

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)
