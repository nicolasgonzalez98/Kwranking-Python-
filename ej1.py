import os



def carga_keywords():
	keywords = []
	try:
		fichero = open('keywords.txt')
		print('Archivo cargado correctamente!')
		keys = fichero.readlines()
		for palabra in keys:
			keywords.append(palabra.replace('\n',''))
	except FileNotFoundError:
		print('El archivo no existe.')
	return keywords

def mostrar_keywords(lista):
	contador = 0
	for kw in lista:
		print(kw)
		contador += 1
		if contador == 20:
			contador = 0
			input('Mostrar mas...')
	
def imprimir_menu(menu):
	for i in range(len(menu)):
		print(f'[{i}] - {menu[i]}')

def comprueba_keywords(kw, dominio):
	start = 0
	auth_data = {'q':kw, 'start':start}
	res = request.get(f'https://www.google.com/search',data = auth_data)
	


n = True
lista = []
opciones = ['Salir', 'Importar palabras clave', 'Mostrar palabras clave']

while n:
	imprimir_menu(opciones)
	opcion = int(input('>>>'))
	if opcion == 0:
		n = False
	else:
		if opcion == 1:
			lista = carga_keywords()
			
		else:
			if len(lista) == 0:
				print('No descargaste el archivo keywords.txt, intente nuevamente.')
			else:
				mostrar_keywords(lista)
    
	input('Pulse un boton para continuar...')
	os.system('cls')
