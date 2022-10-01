import time #importo una libreria para manejar el tiempo

#Inicio de la app
print("....")
time.sleep(2) #utilizo esta funcion para que el siguiente print aparezca desp de 2 seg
print(".......")
time.sleep(2)
print("..........")
time.sleep(2)
print(".............")
print(".................")
print(".....................")
print("........................")
print("..................................")
time.sleep(2) 
print("-----Bienvenido a la ZooGuia!-----")
print(" ")
nombre=input("Como te llamas?: ")
print(f'Bienvenido {nombre}!')
print(" ")
time.sleep(3)
print("-------------  Menu  -------------")
print("1. Ingresar Nuevos Registros")
print("2. Consultar Registros")
print("3. Salir del programa")
print(input('Ingrese una opcion: '))

#Cargar los Datos de los Animales
def CargaDeAnimales():
            animal=[]
            animal_quantity=int(input("Ingresa la cantidad de animales que deseas ingresar: "))
            print(f'Se van a insertar {animal_quantity} animales')
            
            for i in range(animal_quantity):
                especie=input('Ingrese la especie del animal: ')
                ubicacion=input('Ingrese el nombre del país o continente donde habita ese animal: ')
                poblacion=int(input('Ingrese la cantidad de animales que habitan: '))
                animal.append((especie,ubicacion,poblacion))
                        
                if poblacion == 0:
                    print('Extinto')
                elif poblacion<10000:
                    print('En vias de extincion')
                elif poblacion>=10000:
                    print('Fuera de peligro de extincion')
                    
            return animal

#Consultar los datos guardados
def AnimalesCargados(animal):
            print("..."*10)
            print("Registros cargados")
            print(" ")
            if len(animal) == 0:
                print('La lista esta vacia')
            else:
                for animal in animal:
                    print(animal)

#Menu Inicio dentro de un bucle while True para que aparezca desde el inicio
def Menu(animal):
    while True :
            print("-------------  Menu  -------------")
            print("1. Ingresar Nuevos Registros")
            print("2. Consultar Registros")
            print("3. Salir del programa")
            opcion= input('Ingrese una opcion: ')
            if opcion == '1':
                animal.append(CargaDeAnimales())
            elif opcion == '2':
                AnimalesCargados(animal)
            elif opcion == '3':
                print('Muchas gracias por usar el programa. Programa Finalizado')
                print("........................................................")
                break
            else:
                print('Opcion incorrecta, vuelve a ingresar una opcion: ')

#bloque principal
animal=CargaDeAnimales()
AnimalesCargados(animal)
Menu(animal)