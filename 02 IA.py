#Inicializar las tres variables
numero_a = 0
numero_b=0
numero_c = 0

#Pedir al usuario los primeros dos numeros
numero_a = float(input("Ingrese un numero: "))

numero_b = float(input("Ingrese otro numero: "))

#imprimir la division de los primeros dos numeros
print(f"Resultado: {numero_a}/{numero_b} = ", numero_a/numero_b)

#pido ingresar un numero con dos decimales
numero_c = float(input("Ingrese un numero con hasta 2 decimales"))
#muestro el numero ingresado
print("El numero ingresado es :", numero_c)
#calculo en resultado la division del tercer y el segundo numero
resultado = numero_c / numero_b
#imprimo lo calculado
print(f"Resultado: {numero_c}/{numero_b} = {resultado:.2f}")
#calculo la resta del tercer y el primer numero
resultado = numero_c - numero_a
#muestro el resultado
print(f"Resultado: {numero_c}-{numero_a} = {resultado:.2f}")
