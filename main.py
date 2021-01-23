import time
from numpy import arange
import matplotlib.pyplot as plt

from entradas.entradas import vetor_degrau, vetor_rampa, vetor_seno
from planta.motor import MotorDC

def main():
    print('Inicio do processo')
    time.sleep(1)
    print('Desafio... Realize o controle do processo')
    time.sleep(5)
    print('Parte mais dificil: Julgue!')
    print('Escolha o metodo que melhor lhe convem')
    print('e proponha um bom controle para o sistema')
    time.sleep(5)

    degrau = vetor_degrau()
    rampa = vetor_rampa()
    seno = vetor_seno()


    # print('Entradas Disponiveis')
    # print('Terminando a visualizacao, feche a janela')
    # plt.plot(x, degrau, x, rampa, x, seno)
    # plt.show()

    print('Agora a resposta do motor a cada uma das entradas')
    motor1 = MotorDC()
    [t1, y1] = motor1.response(degrau)
    plt.plot(t1, degrau, t1, y1)
    plt.show()

    [t1, y1] = motor1.response(rampa)
    plt.plot(t1, rampa, t1, y1)
    plt.show()

    [t1, y1] = motor1.response(seno)
    plt.plot(t1, seno, t1, y1)
    plt.show()

    print('transfer function')
    print('+++++++++++++++++')
    print('       14        ')
    print('-----------------')
    print('  s^2 + 2s + 14  ')



if __name__ == '__main__':
    main()