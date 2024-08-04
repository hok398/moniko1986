from tabulate import tabulate

hola = print("Hola me podrias apoyar con los siguientes datos")
nombre = input("¿Como te llamas?: ")
apellido_paterno = input("coloca aqui tu apellido paterno:")
apellido_materno = input("coloca aqui tu apellido materno:")
edad = input("ingresa tu edad: ")
peso_en_kg = float (input ('Ingresa el valor de peso en kg: '))
altura_en_m = float (input ('Ingresa el valor de altura en m: '))
IMC=peso_en_kg/altura_en_m/altura_en_m
print()
print("Su IMC es de " + str (IMC))

if IMC<=16.00: 
    print('Criterio de ingreso en hospital.')
if IMC>=16.01 and IMC<18.99:  
    print("peso bajo ")
    print()
if IMC>=18.50 and IMC<24.99:
    print ('peso normal.')
    print()
if IMC>=25.00 and IMC<29.99:
    print('Sobrepeso (obesidad de grado I).')
    print()
if IMC>=30.00 and IMC<34.99:
    print ('Sobrepeso (obesidad de grado II).')
    print()
if IMC>=35.00 and IMC<39.99:
    print ('Sobrepeso (obesidad de grado III).')
    print()
if IMC>=39.99 and IMC<40:
    print ('Obesidad (obesidad de grado IV).')
    print()
if IMC>=40 and IMC<1000: 
    print ('Obesidad tumba.')
    print('su indice de IMC: ' + repr (IMC))
    print()
lista=[["Composición corporal","Índice de masa corporal(IMC)"],["Peso inferior al normal","Menos de 16.00"],["Normal","18.5 – 24.9"],["Peso superior al normal","25.0 – 29.9"],["Fuera de escala","Más de 30"]]
print()
print(tabulate(lista))
"alto"
