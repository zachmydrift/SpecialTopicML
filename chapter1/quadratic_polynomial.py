import math
import matplotlib.pyplot as plt
import numpy as np

class quadratic_polynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def descriminant():
        return(self.b**2 - 4*self.a*self.c >= 0)

    def general_formula(self):
        if(self.descriminant):
            sol1 = (-self.b + math.sqrt(self.b**2 - 4*self.a*self.c >= 0))/2*self.a
            sol2 = (-self.b - math.sqrt(self.b**2 - 4*self.a*self.c >= 0))/2*self.a
            print("The equation has two real solution {} and {} \n".format(sol1, sol2))
        else:
            print("The equation has non real solution \n")

    def vertex_formula(self):
            h=0
            k=0
            if(self.b**2-4*self.a*self.c>=0):
                D = math.sqrt(self.b**2-4*self.a*self.c)
                h = -self.b/(2*self.a)
                k = -D/(4*self.a)
            return h, k

    def plot_function(self):
        # 100 linearly spaced number
        x=np.linspace(-20,20,100)
        y=self.a*x**2 + self.b*x + self.c
        #setting the axes at the center
        fig = plt.figure()
        ax=fig.add_subplot(1,1,1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('center')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.plot(x,y,'r')

    def evaluation(self, x_values):
        y_values = np.zeros(len(x_values))
        for i in range(len(y_values)):
            y_values[i] = self.a*math.pow(x_values[i],2)+self.b*x_values[i]+self.c
            return y_values

   