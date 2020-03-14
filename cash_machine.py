depositos = [[100,0],[50,0],[20,0],[10,0],[5,0],[2,0]]
def depositar (num_notas, nota, depositos):
	try:
		cont = 0
		while True:
			if cont == 0:
				num_notas,nota = input("\
Para depositar siga o modelo \"(numeroNotas,tipoNota)\" Ex.: 2,100\n\
Para encerrar o depósito, digite 0.\n").split(",")
				cont += 1
			else:
				num_notas,nota = input().split(",")
			for k in depositos:
				if k[0] == int(nota):
					k[1]+=int(num_notas)
					break
	except ValueError:
		print("Deposito finalizado.\n")
	finally:
		return depositar

def saldof (depositos):
	saldo=0	
	for k in depositos:
		saldo += float(k[0]*k[1])
	return saldo

def sacar(valorWish,valorTrue,depositos):
	for k in depositos:
		while k[0]<= valorWish and k[1] > 0:
			valorWish -= k[0]
			k[1]-=1
			valorTrue += k[0]
	return depositos

operacoes = [depositar,sacar]
while True:
	saldo = saldof(depositos)
	if saldo <= 1:
		menu = int(input(f"Saldo Disponível: R${saldo:.2f}\n(1)Depositar notas\n(3)Encerrar\n")) 
	else:
		menu = int(input(f"Saldo Disponível: R${saldo:.2f}\n(1)Depositar notas\n(2)Sacar dinheiro\n(3)Encerrar\n"))
	num_notas = nota = ""
	if menu == 1:
		entrada = operacoes[menu-1](num_notas,nota,depositos)
	if menu == 2:
		saldo = saldof(depositos)
		valorWish = float(input(f"Informe o valor a ser sacado:\n"))
		while valorWish > saldo:
			valorWish = float(input(f"Valor não disponível em caixa. \
Informe o valor a ser sacado:\n"))
		valorTrue = 0
		entrada = operacoes[menu-1](valorWish,valorTrue,depositos)
		valorTrue = saldo-saldof(depositos)
		if valorTrue == 0 and saldo > valorWish:
			print("Desculpe, as notas disponíveis são mais altas do que o valor desejado.\nTente novamente.\n")
		else:
			print(f"Valor disponível sacado: R${valorTrue:.2f}.\nSaque concluído\n")
	if menu == 3:
		print("Volte Sempre.")
		break

input()