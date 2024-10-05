import os
import time
import threading

#Función para el apagado programado:
def programar_apagado(tiempo_en_minutos):
    os.system(f'sudo shutdown -h +{tiempo_en_minutos}')
    print(f'El equipo se apagará en {tiempo_en_minutos} minutos. Escriba "Cancel" para que no se apague')

#Función para cancelar el apagado:
def cancelar_apagado():
    while True:
        cancelar = input('Escriba "Cancel" para detener el apagado ').lower()
        if cancelar == 'Cancel':
            os.system('sudo shutdown -c')
            print('Apagado cancelado')
            break

#Pregunta al usuario si desea apagar:
shutdown = input('Apagar? (y/n)').lower()

if shutdown == 'y':
    tiempo = input('En cuantas horas se apagará el equipo?: ')
    try:
        #Convirtiendo la hora a minutos:
        minutos = int(float(tiempo) * 60)
        
        #Ejecutar el apagado en un hilo separado:
        hilo_apagado = threading.Thread(target=programar_apagado, args=(minutos,))
        hilo_apagado.start()

        #Permitir cancelar en el hilo principal
        cancelar_apagado()

    except ValueError:
        print('Entrada inválida. Introduzca un número.')
        

else:

    exit()