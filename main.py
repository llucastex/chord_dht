from chord import *

# Adiciona 32 nós à rede, sinalizando quais estarão online
queue = Chord()
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

# Após adicionar os nós, devemos gerar a tabela de roteamento para cada nó
queue.generateTable()
# Imprime na tela as tabelas de roteamento para cada nó ativo
queue.printNodeTable()
print('----')
# Simula a requisição passando qual nó está fazendo a requisição e qual a chave requerida
queue.simulateRequest(client = 1, key = 26)
queue.simulateRequest(client = 4, key = 17)
queue.simulateRequest(client = 28, key = 12)
queue.simulateRequest(client = 4, key = 21)