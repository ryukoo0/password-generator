import random
import string
contraseñas_guardadas = []
def generate_contraseña (longitud= 10):
    caracteres= string.ascii_letters+string.digits+string.punctuation
    contraseña= "".join(random.choice(caracteres)for _ in range(longitud))
    return contraseña

def mostrar_menu():
    print("\nMenu principal") #el "\n" representa un salto de linea. esto hara que el texto comience en una nueva linea
    print("1. Generar contraseña")
    print("2. mostrar contraseñas guardadas")
    print("3. salir")

def copiar_contraseña(contraseña):
    print(f"Contraseña '{contraseña}' copiada al portapapeles (simulado).")

def guardar_contraseña(contraseña):
   contraseñas_guardadas.append(contraseña) #se usa "append" para almacenar datos en una lista
   print(f"contraseña '{contraseña}' ha sido guardada") 

def ver_contraseñas_guardadas():
    print("contraseñas guardadas")
    if not contraseñas_guardadas:
        print("no hay contrasñas guardadas")
    else: 
        for idx, pwd in enumerate(contraseñas_guardadas): #"enumarate" nos permite obtener el indice y valor de cada elemento
        #"idx" es lo que nos va a ayudar a representar la posicion del elemento en la lista
        #"pwd" es la variable de que representa el valor del elemento en la lista
            print(f"{idx + 1}. {pwd}") #se usa "idx +1" para que la lista empize desde el 1 y no desde 0
def eliminar_contraseña():
    ver_contraseñas_guardadas()
    if contraseñas_guardadas:
            idx = int(input("Ingrese el número de la contraseña a eliminar: ")) - 1 #ponemos el -1 porque python comienza desde 0
            if 0 <= idx < len (contraseñas_guardadas): # el idx verifica que no se exceda el tamaño de la contraseña
                # el len nos da el numero total de elementos de la lista.
                eliminada = contraseñas_guardadas.pop(idx) #el pop va a borrar de la lista el elemento que queramos 
                print(f"contraseña '{eliminada} eliminada'")
            else:
                print("indice no valido.")

#bucle del menu principal
while True: #bucle del menu
    mostrar_menu()
    opcion = input("seleccione la opcion deseada")
    if opcion == '1':
        nueva_contraseña = generate_contraseña()  
        print(f"su contraseña es{nueva_contraseña}")
        action = input("desea (g)uardar o (c)opiar su contraeña")
        if action.lower() == 'c':
            copiar_contraseña(nueva_contraseña)
        elif action.lower() == 'g':
            guardar_contraseña(nueva_contraseña)
    break 
    
 



