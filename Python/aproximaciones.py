
objetivo=int(input('Escoge un número: '))
error=0.01
paso=error**2
respuesta=0.0

while abs(respuesta**2 - objetivo)>=error and respuesta<=objetivo:
    respuesta+=paso

if  abs(respuesta**2 - objetivo)>=error:
    print(f'No se encontro respuesta para el {objetivo}')
else:
    print(f'La raíz cuadrada para {objetivo} es {respuesta}')

