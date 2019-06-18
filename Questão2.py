def criptografar(chave):
	res = ""
	res += str((int(chave[2]) + 6) %10 )
	res += str((int(chave[3]) + 6) %10 )
	res += str((int(chave[0]) + 6) %10 )
	res += str((int(chave[1]) + 6) %10 )

	return res

def descriptografar(chave):
	res = ""
	res += str((int(chave[2]) - 6) %10 )
	res += str((int(chave[3]) - 6) %10 )
	res += str((int(chave[0]) - 6) %10 )
	res += str((int(chave[1]) - 6) %10 )

	return res
chave = input("insira a chave a ser criptografada: ")
print("Chave criptografada: "+criptografar(chave))

chave = input("insira a chave a ser descriptografada: ")
print("Chave descriptografada: "+descriptografar(chave))

