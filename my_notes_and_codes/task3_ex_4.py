'''
Write a script to perform a rotation about the X-axis of a point (about the origin) in 3D space using linear algebra style with NumPy.
Use a point at (1,5,0) and rotation angles of 45°, 90° and 180° to test your code.
'''

import numpy as np

def rotation(x0,y0,z0,theta_deg):
    theta = np.radians(theta_deg)
    rot= np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]])
    x,y,z = rot @ [x0,y0,z0]
    print("\n*******************************************************************")
    print("\nThe resulting rotation of x0: {},y0: {},z0: {} around the".format(x0,y0,z0)\
    +" x-axis with an angle of {} degrees is:\n".format(theta_deg))
    print("x: {}\ny: {}\nz: {}".format(x,y,z))
    #print(y)
    #print(z)

def main():
    angles = [45,90,180]
    for angle in angles:
        rotation(1,5,0,angle)

if __name__ == "__main__":
    main()
