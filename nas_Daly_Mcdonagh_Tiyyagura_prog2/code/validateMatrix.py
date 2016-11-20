# -*- coding: utf-8 -*-
"""

"""
import numpy as np


def non_zero_diagonal_check(matrix_a,dimension_n):
    for counter in range(dimension_n):
        if(matrix_a[counter,counter]==0.0):
            return False
    return True
    
    
def det_check(matrix_a):
    if(np.linalg.det(matrix_a)==0.0):
        return False
    return True
    
def row_diagonally_dominant(matrix_a,dimension_n):
    for row_counter in range(dimension_n):
        sum = 0
        for col_counter in range(dimension_n):
            if(row_counter != col_counter):
                sum += abs(matrix_a[row_counter,col_counter])
#        print("Row Sum: ",sum,"Diag Value:",matrix_a[row_counter,row_counter])
        if (abs(matrix_a[row_counter,row_counter])> sum):
            return True
    return False

def col_diagonally_dominant(matrix_a,dimension_n):
    for col_counter in range(dimension_n):
        sum = 0
        for row_counter in range(dimension_n):
            if(row_counter != col_counter):
                sum += abs(matrix_a[row_counter,col_counter])
#        print("Col Sum: ",sum,"Diag Value:",matrix_a[col_counter,col_counter])
        if (abs(matrix_a[col_counter,col_counter])> sum):
            return True
    return False

def spectral_radius_convergence_check(matrix_a, w=1.25):
    #value w=1 would be a check for Gauss Seidel convergence
    #for over relaxation w will be slightly over 1, probably close to 1.25  
    
    matrix_l=np.tril(matrix_a, k=-1)
    matrix_u=np.triu(matrix_a, k=1)
    matrix_d=np.diag(np.diag(matrix_a))

#    print(matrix_l, matrix_u, matrix_d)
    matrix_wl=w*matrix_l
    matrix_wu=w*matrix_u
    matrix_dw=(1-w)*matrix_d
    
#    print(np.linalg.inv(matrix_d+matrix_l) * -1)
#    print(matrix_wl, matrix_wu, matrix_dw)        

#    matrix_c = np.dot(-np.linalg.inv(matrix_d+matrix_l), matrix_u)
#    print("matrix_c :",matrix_c)

    matrix_c = np.dot(np.linalg.inv(matrix_d+matrix_wl), (matrix_dw - (w * matrix_u)))
        
#    print("C Eig Val:",np.linalg.eigvals(matrix_c))  

#    print("CTC Eig Val:",np.linalg.eigvals(np.dot(matrix_c,matrix_c.transpose())))  

    #spectral radius is maximum eigenvalue in absolute terms
    radius=np.absolute(np.linalg.eigvals(matrix_c)).max()
        
#    radius=np.linalg.eigvals(matrix_c).max()
#    print(radius)
    
    if radius < 1:
        return True
        
    return False
