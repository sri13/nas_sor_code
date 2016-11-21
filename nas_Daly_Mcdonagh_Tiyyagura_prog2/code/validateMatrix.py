# -*- coding: utf-8 -*-
"""
ValidateMatrix checks various matrix conditions
Dependent on main program - mainSOR.py

Authors:
Niall Daly
Ronan Mc.Donagh
Srikanth Tiyyagura
"""
#import modules
import numpy as np


def non_zero_diagonal_check(matrix_a,dimension_n):
    '''
    Checks for any zero entries on the diagonal
    Arguments:
        matrix_a - matrix to perform the check
        dimension_n - size of the matrix
    Return:
        True - if no zeros found
        False - if any zero found on diagonal
    '''
    for counter in range(dimension_n):
        if(matrix_a[counter,counter]==0.0):
            return False
    return True
    
    
def det_check(matrix_a):
    '''
    Non Zero determinant Check for matrix 
    Arguments:
        matrix_a - matrix to perform the check
    Return:
        True - if determinant is not zero 
        False - if determinant is zero 
    '''    
    if(np.linalg.det(matrix_a)==0.0):
        return False
    return True
    
def row_diagonally_dominant(matrix_a,dimension_n):
    '''
    Row Diagonally dominant means any one absolute diagonal value should be 
    greater than sum of absolute row values
    Arguments:
        matrix_a - matrix to perform the check
        dimension_n - size of the matrix
    Return:
        True - if an entry that match condition found 
        False - if an entry is not found 
    '''        
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
    '''
    Column Diagonally dominant means any one absolute diagonal value should be 
    greater than sum of absolute column values
    Arguments:
        matrix_a - matrix to perform the check
        dimension_n - size of the matrix
    Return:
        True - if an entry that match condition found 
        False - if an entry is not found 
    '''
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
    '''
    Diagonally dominant is a sufficient condition for convergence, however,
    it wont be sufficient condition to disprove a matrix, so checking 
    spectral radius < 1
    
    value w=1 would be a check for Gauss Seidel convergence
    for over relaxation w will be slightly over 1, probably close to 1.25  

    Arguments:
        matrix_a - matrix to perform the check
        w <optional> - estimate 
    Return:
        True - if spectral radius less than one 
        False - if radius is more or equal to one 
    '''
    
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

    matrix_c = np.dot(np.linalg.inv(matrix_d+matrix_wl), (matrix_dw - (matrix_wu)))
        
#    print("C Eig Val:",np.linalg.eigvals(matrix_c))  
#    print("CTC Eig Val:",np.linalg.eigvals(np.dot(matrix_c,matrix_c.transpose())))  

    #spectral radius is maximum eigenvalue in absolute terms
    radius=np.absolute(np.linalg.eigvals(matrix_c)).max()
        
#    radius=np.linalg.eigvals(matrix_c).max()
#    print(radius)
    
    if radius < 1:
        return True
        
    return False
