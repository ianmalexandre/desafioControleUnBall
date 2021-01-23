import numpy as np
import control as co 

class MotorDC:
    def __init__(self):
        self.A = np.array([[0.0, 1.0],
                           [-14.0, -2.0]])
        self.B = np.array([[0.0],
                           [1.0]])
        self.C = np.array([14.0, 0.0])
        self.D = 0.0
        self.state = np.array([[0.0],
                               [0.0]])

        self.sys = co.ss(self.A, self.B, self.C, self.D)

    def dead_zone(self, value):
        if (value < 0.2) and (value > -0.1):
            return 0.0
        return value
    
    def saturation(self, value):
        if (value > 2.0) or (value < -2.0):
            return 2.0
        return value

    def response(self, input):
        t = np.linspace(0, 1, 5000)
        # entrada, saida e estados
        t1, y1, states = co.forced_response(self.sys, t, input)

        return [t1, y1]
        
    # Tentativa nao sucedida risos
    # def response(self, input):
        
    #     #Realiza cálculo da saída do sistema
    #     x_dot = np.dot(self.A, self.state) + np.dot(self.B, input)
    #     y = np.dot(self.C, self.state)
        
    #     value = x_dot[0][0]
    #     # Salva valor de última resposta
    #     self.state[0] = x_dot[0]
    #     self.state[1] = np.array(input - (2*value) - (7*value**2))

    #     if (y > 1):
    #         print(x_dot)

    #     # Aspecto nao-linear
    #     y = self.dead_zone(y)
    #     y = self.saturation(y)

    #     return y

    # def vetor_response(self, vector_input):
    #     saida = np.zeros(len(vector_input))

    #     for i in range(len(vector_input)):
    #         saida[i] = self.response(vector_input[i])

    #     return saida


