from numpy import pi, sin, arange, zeros

def vetor_degrau():
    entrada = zeros(5000)
    for i in range(5000):
        entrada[i] = 1 if i > 2500 else 0

    return entrada


def vetor_rampa():
    entrada = arange(0, 1, 1/5000)

    return entrada


def vetor_seno():

    entrada = [i * pi / 5000 for i in range(5000)]

    resposta = sin(entrada)

    return resposta

