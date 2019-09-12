def sumalista(lista):
   if len(lista) == 1:
        return lista[0]
   else:
        return lista[0] + sumalista(lista[1:])
		
def invertir(lista):
	return lista[::-1]
	
def igualLista(a,b):
	return a == b
	
def listaOrdenada (lista):
	if len(lista) == 0:
		return True
	elif len(lista) == 1:
		return True
	else:
		return lista[0] <= lista [1] and listaOrdenada(lista[1:])
		
def mostrarUbicacion (lista,n):
	return lista[n]

def mayor (lista):
	if len(lista) == 1:
		return lista[0]
	else:
		if lista[0] > mayor(lista[1:]):
			return lista[0]
		else:
			return mayor(lista[1:])

def contarPares(lista):
    if len(lista) == 0:
        return 0
    else:
        return len([x for x in lista if x%2==0])
        
def cuadrados(lista):
    return [x*x for x in lista]

print(cuadrados([x for x in range (1,11)]))