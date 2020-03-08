'''
Pendulun

d_d_theta = -g/l*sin(theta)+C*cos(theta)*sin(Omega*t)
'''
import numpy as np
from scipy.integrate import odeint
from math import *
import matplotlib.pyplot as plt

from IPython.display import display, clear_output
import time
def sys(theta, t, l, C, omega, g):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = -g/l*sin(theta1)+ C*cos(theta2)*sin(omega*t)

    dtheta_dt = [dtheta1_dt,dtheta2_dt]
    return dtheta_dt

def main():
    C = 2
    l = 10/100 #m
    t = np.linspace(0,100,2500)
    g = 9.81
    theta_0=np.array([0,0]).T
    omega = np.sqrt(g/l)#5


    theta = odeint(sys,theta_0,t,args = (l,C,omega,g))
    plt.plot(t,theta)
    print(theta)
    plt.legend(['theta','thetadot'])
    plt.title("Pendulum change through time with force in natural pendulum's frequency")
    plt.xlabel("time")
    plt.show()

    fig, ax = plt.subplots(figsize=(4,4))
    x=theta
'''    plt.show()
    for t_idx, tt in enumerate(t[:200]):

        x1 = + l * sin(x[t_idx, 0])
        y1 = - l * cos(x[t_idx, 0])

        x2 = x1 + l * sin(x[t_idx, 1])
        y2 = y1 - l * cos(x[t_idx, 1])

        ax.cla()
        ax.plot([0, x1], [0, y1], 'r.-')
        ax.plot([x1, x2], [y1, y2], 'b.-')
        ax.set_ylim([-1.5, 0.5])
        ax.set_xlim([1, -1])

        clear_output()
        display(fig)

        time.sleep(0.1)
'''
if __name__ == "__main__":
    main()
