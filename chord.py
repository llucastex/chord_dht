from __future__ import annotations
from typing import Any


EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'
NODE_LENGTH = 5

## We can create our own error
class EmptyQueueError(Exception):
    ...


class Node:
    def __init__(self, id, status = False) -> None:
        self.id = id
        self.online = status
        self.next: Node
        self.table = []
        self.onlineNodes = []
        self.reqPath = []
    
    def reqNode(self, chave):
        found = False
        i = 1
        actualNode = self
        while not found:

            while i <= len(actualNode.table)-1:
                if chave in actualNode.table:
                    found = True
                    return found, actualNode.id
                if chave >= actualNode.table[i-1] and chave <= actualNode.table[i]:
                    node = self.onlineNodes[i-1]
                    break
                elif i == len(actualNode.table)-1:
                    node = self.onlineNodes[i]
                i += 1
            actualNode = node
            found, actualNode.id = node.reqNode(chave)
        return found, actualNode.id
            
    # def generateTableNode(self, tableLength):
    #     for line in range(1,NODE_LENGTH + 1):
    #         FTp = self.id + 2**(line - 1)
    #         node = self.next

    #         if (FTp > tableLength ):
    #             # self.table.append(None)
    #             FTp = FTp - tableLength
    #             # continue

    #         i = 1
    #         while(i <= FTp):
    #             node = node.next
    #             i += 1
    #         while(True):
    #             if node.online:
    #                 self.table.append(FTp)
    #                 break
    #             else:
    #                 FTp += 1
    #                 node = node.next

    def getId(self):
        return self.id

    def __repr__(self) -> str:
        return f'{self.id}'
    
    def __bool__(self) -> bool:  # this method will evaluate if Node is assigned 
        return bool(self.id != EMPTY_NODE_VALUE)
    
    
class Queue:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0
            
    def generateTable(self):
        for nodeID in range(1, len(self) + 1):
            actualNode = self.getNode(nodeID)
            if not self.peekOnline(actualNode): continue

            for line in range(1,NODE_LENGTH + 1):
                FTp = nodeID + 2**(line - 1)
                while True:
                    try:
                        nextNode = self.getNode(FTp)
                        break
                    except:
                        FTp = FTp - len(self) 
                        
                while True:
                    if self.peekOnline(nextNode):
                        actualNode.table.append(FTp)
                        actualNode.onlineNodes.append(nextNode)
                        break
                    else:
                        # FTp += 1
                        nextNode = nextNode.next
                        FTp = nextNode.getId()
                        # nextNode = self.getNode(FTp)



            
        
    def enqueue(self, node_value, status) -> None:
        new_node = Node(node_value, status)

        if not self.first:
            self.first = new_node
        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            self.last.next = self.first

        
        self._count += 1
    
    def dequeue(self) -> Node:
        if not self.first:
            raise EmptyQueueError('Empty Queue')
        
        first = self.first 

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)
        
        self._count -= 1
        return first

    def delete(self, id) -> None: # i have to give it a better try
        if not self.first:
            raise EmptyQueueError('Empty Queue')
        aux_queue = Queue()
        for i in range(len(self)):
            node = self.dequeue()
            if node.value != id:
                aux_queue.enqueue(node)
        for e in aux_queue:
            self.enqueue(e)

    def getNode(self, nodeNumber):
        if nodeNumber > len(self):
            raise Exception(f"Sorry, node {nodeNumber} doesn't exist!")
        node = self.first
        for _ in range(1, nodeNumber):
            node = node.next
        return node
    
    def printNodeTable(self):
        node = self.first
        for _ in range(1, len(self) + 1):
            if self.peekOnline(node): print(node.table)
            node = node.next

    def peekOnline(self, node):
        return node.online

    def peek(self) -> Node:
        return self.first

    def __len__(self) -> int:
        return self._count
        
    def __bool__(self) -> bool:
        return bool(self._count)

    def __iter__(self) -> Queue:
        return self
    
    def __next__(self) -> Any:
        try:
            next_value = self.dequeue()
            return next_value
        except EmptyQueueError:
            raise StopIteration
    
    def __repr__(self) -> str:
        if not self.first:
            return 'Queue()'
        return f'Queue({self.first},{self.last})'


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1, True)
    queue.enqueue(2, False)
    queue.enqueue(3, False)
    queue.enqueue(4, True)
    queue.enqueue(5, False)
    queue.enqueue(6, False)
    queue.enqueue(7, False)
    queue.enqueue(8, False)
    queue.enqueue(9, True)
    queue.enqueue(10, False)
    queue.enqueue(11, True)
    queue.enqueue(12, False)
    queue.enqueue(13, False)
    queue.enqueue(14, True)
    queue.enqueue(15, False)
    queue.enqueue(16, False)
    queue.enqueue(17, False)
    queue.enqueue(18, True)
    queue.enqueue(19, False)
    queue.enqueue(20, True)
    queue.enqueue(21, True)
    queue.enqueue(22, False)
    queue.enqueue(23, False)
    queue.enqueue(24, False)
    queue.enqueue(25, False)
    queue.enqueue(26, False)
    queue.enqueue(27, False)
    queue.enqueue(28, True)
    queue.enqueue(29, False)
    queue.enqueue(30, False)
    queue.enqueue(31, False)
    queue.enqueue(32, False)
    queue.generateTable()
    queue.printNodeTable()
    print(queue.getNode(4).reqNode(28))
