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
            
    # Gera a tabela de roteamento para cada nó ativo na rede
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

    # Simula uma requisição feita para um nó
    def simulateRequest(self, client: int, key: int) -> None:
        if not self.peekOnline(self.getNode(client)):
            raise Exception(f"Node {client} is not online!")
        print(f"\nNode {client} is requesting key {key}")
        self.getNode(client).reqNode(key)

    # Adiciona um nó novo na rede
    def enqueue(self, id: int, status: bool) -> None:
        new_node = Node(id, status)

        if not self.first:
            self.first = new_node
        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            self.last.next = self.first

        self._count += 1
    
    # Retorna o nó baseado no seu ID
    def getNode(self, id: int) -> Node:
        if id > len(self):
            raise Exception(f"Sorry, node {id} doesn't exist!")
        node = self.first
        for _ in range(1, id):
            node = node.next
        return node
    
    # Printa a tabela de roteamento dos nós ativos
    def printNodeTable(self) -> None:
        node = self.first
        for _ in range(1, len(self) + 1):
            if self.peekOnline(node): print(f"Nó {node.getId()}: {node.table}")
            node = node.next

    # Printa os nós que cada nó é responsável
    def printPrevKeys(self) -> None:
        node = self.first
        for _ in range(1, len(self) + 1):
            if self.peekOnline(node):
                print(f"Node {node.id} takes care of: {node.prevKeys}")
            node = node.next

    def peekOnline(self, node: Node) -> bool:
        return node.online

    def __len__(self) -> int:
        return self._count
        
    def __bool__(self) -> bool:
        return bool(self._count)

    def __iter__(self) -> Chord:
        return self