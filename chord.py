from __future__ import annotations
from typing import Any

from node import *

class EmptyChordError(Exception):
    ...

class Chord:
    NODE_LENGTH = 5

    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0
            
    def generateTable(self) -> None:
        for nodeID in range(1, len(self) + 1):
            actualNode = self.getNode(nodeID)
            actualNode.sendSucc() # Passa as chaves para o proximo nó online
            if not self.peekOnline(actualNode): continue

            for line in range(1, self.NODE_LENGTH + 1):
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
                        nextNode = nextNode.next
                        FTp = nextNode.getId()

    def simulateRequest(self, client, key) -> None:
        if not self.getNode(client).online:
            raise Exception(f"Node {client} is not online!")
        print(f"\nNode {client} is requesting key {key}")
        self.getNode(client).reqNode(key)

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
            raise EmptyChordError('Empty Chord')
        
        first = self.first 

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)
        
        self._count -= 1
        return first

    def getNode(self, nodeNumber) -> Node:
        if nodeNumber > len(self):
            raise Exception(f"Sorry, node {nodeNumber} doesn't exist!")
        node = self.first
        for _ in range(1, nodeNumber):
            node = node.next
        return node
    
    def printNodeTable(self) -> None:
        node = self.first
        for _ in range(1, len(self) + 1):
            if self.peekOnline(node): print(node.table)
            node = node.next

    def printPrevKeys(self) -> None:
        node = self.first
        for _ in range(1, len(self) + 1):
            if self.peekOnline(node):
                print(f"Node {node.id} takes care of: {node.prevKeys}")
            node = node.next

    def peekOnline(self, node) -> bool:
        return node.online

    def __len__(self) -> int:
        return self._count
        
    def __bool__(self) -> bool:
        return bool(self._count)

    def __iter__(self) -> Chord:
        return self