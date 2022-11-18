from __future__ import annotations
from typing import Any

EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'

class Node:

    def __init__(self, id, status = False) -> None:
        self.id = id
        self.online = status
        self.next: Node
        self.table = []
        self.onlineNodes = []
        self.prevKeys = []
    
    # Passa as chaves para o proximo nó online
    def sendSucc(self) -> None:
        if self.online: return
        done = False
        actualNode = self
        accNode = self.next
        while not done:
            if not accNode.online:
                accNode = accNode.next
            else:
                done = True
        accNode.prevKeys.append(actualNode)

    # Faz a requisição para um nó
    def reqNode(self, chave):
        found = False
        i = 1
        actualNode = self
        while not found:
            for el in actualNode.prevKeys:
                if chave == el.id:
                    found = True
                    return found, actualNode.id

            while i <= len(actualNode.table)-1:
                if chave == actualNode.id:
                    found = True
                    return found, actualNode.id
                if (i == len(actualNode.table)-1) and (chave > actualNode.table[i]): # so se for o ultimo
                    node = self.onlineNodes[i]
                    break
                if (chave >= actualNode.table[i-1]) and (chave < actualNode.table[i]):
                    node = self.onlineNodes[i-1]
                    break
                if (chave == actualNode.table[i]):
                    node = self.onlineNodes[i]
                    break
                if (chave < actualNode.table[i - 1]):
                    node = self.onlineNodes[i-1]
                    break
                i += 1
            actualNode = node
            print(f"Requesting node: {node.id}")
            found, nodeId = node.reqNode(chave)
        return found, nodeId

    def getId(self) -> int:
        return self.id

    def __repr__(self) -> str:
        return f'{self.id}'
    
    def __bool__(self) -> bool:
        return bool(self.id != EMPTY_NODE_VALUE)
    
    