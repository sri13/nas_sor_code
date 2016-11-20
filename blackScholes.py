# -*- coding: utf-8 -*-
"""
How to Execute:
python blackScholes.py

Authors:
Niall Daly
Ronan Mc.Donagh
Srikanth Tiyyagura
"""


from math import ceil
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import implementSOR
import processIO

def put_Black_Scholes(X=10, N=100, M=150, T=30, std=0.3, r=0.02, X_to_Smax = 0.5):
    """
    European put options
    T must be measured in days
    r must be an annual rate of return
    X_to_Smax is the ratio of X to SMax, must obey 0 < x_to_smax <= 1
    X_to_Smax determines how many zero values are in b initially
    """
    k = T / (M * 250) #assuming 250 trading days a year
    A = set_A(N, k, std, r) #A stays constant throughout
    alignment = set_alignment(X, k, r, std) #add this constant to b[0] at every timestep
    b = init_b(X, N, X_to_Smax, alignment) #first value of b at timestep M-1
#    print(b)

    #Prepare stock price, timestep axes (x and y axes in the wireframe)    
    S_axis = []
    T_axis = []
    S_current_row = []
    for j in range(1, N):
        S_current_row.append((X * j) / (X_to_Smax * N))    
    for k in range(1, M):
        T_range = []
        for l in range(1, N):
            T_range.append(M - k)
        T_axis.append(np.array(T_range))
        S_axis.append(np.array(S_current_row))
#    print(S_axis)
#    print(T_axis)

    """
    Calculate option values using SOR
    The option value at this timestep is set to b for next timestep
    This is the z-axis in the wireframe
    """    
    
    Value_axis = []
    for i in range(0, M-1):
        [stop_reason, max_it, num_it, b ] = implementSOR.sparse_sor(A, b,np.zeros(len(b)),len(b))
        Value_axis.append(b) #add calculated value pre-alignment
        b[0]+=alignment #this is vector b for the next timestep
#    print(Value_axis)       
    
#plot this in matplotlib as a 3d wireframe
    fig1 = plt.figure()
    fig1.suptitle('Put Option for X='+str(X)+', N='+str(N)+', M='+str(M)+', T='+str(T)+', std='+str(std)+', r='+str(r))
    wire = fig1.add_subplot(111, projection='3d')
    wire.plot_wireframe(S_axis, T_axis, Value_axis)
    
    wire.set_xlabel('Share price')
    wire.set_ylabel('Time steps up until maturity')
    wire.set_zlabel('Value of option')
    plt.savefig('black_scholes_merton.png')        
    plt.show()
    
def set_A(N, k, std, r):
    A=[]
    for i in range(0, N-1):
        A_row = []        
        for j in range(0, N-1):
            if i==j:
                A_row.append(1 + (k * r) + (k * (std**2) * ((i+1)**2)))
            elif i==j+1:
                A_row.append(-0.5 * (i + 1) * k * (((i + 1) * (std**2 )) - r))
            elif i==j-1:
                A_row.append(-0.5 * (i + 1) * k * (((i + 1) * (std**2 )) + r)) 
            else:
                A_row.append(0)
        A.append(A_row)
#    print(to_csr(A))
    return processIO.to_csr_format(A)


def set_alignment(X, k, r, std):
    return 0.5 * k * X * ((std**2) - r)


def init_b(X, N, X_to_Smax, alignment):
    b = []
    N_threshold = ceil(N * X_to_Smax) #value of N where S = X
    for i in range(0, N_threshold):
        b.append(X - ((i + 1) * X / N_threshold))
    b[0]+=alignment
    for j in range(N_threshold, N-1):
        b.append(0)
    return b


#put_Black_Scholes() #low value of k = T/M  
put_Black_Scholes(M=30) #high value of k = T/M
