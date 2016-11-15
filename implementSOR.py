# -*- coding: utf-8 -*-
"""



"""
import numpy as np

def get_euclid_norm(matrix):
    """
    this function accepts one vector
    the calling function should compute this vector as the difference of two vectors
    the standard Euclidean distance formula sqrt(x1^2+x2^2+....+xn^2) is applied
    """
    sum = 0
    for each_val in matrix:
        sum+=each_val**2
    return np.sqrt(sum)
 
def get_residual(A, x, b):
    """
    return the residual error Ax-b for an approximation of x
    input parameters should be numpy arrays
    this is not as simple as using numpy.dot because A is in CSR format 
    """
    adotx = []    
    for i in range(0,len(b)):
        adotx.append(0.0)    
    #i should really do a DOT function instead of coding it explicitly here and in SOR also
    for j in range (0, len(b)): 
        first_nz = A[1][(A[2][j]-1)] - 1 #pos of first non zero on row             
        for k in range(A[2][j]-1, A[2][j+1]-1):            
            adotx[j] = adotx[j] + A[0][k] * x[k - (A[2][j]-1) + first_nz]
    return get_euclid_norm(np.subtract(adotx, b))    

def get_x_seq(xold, xnew):
    """
    this function computes Euclidean distance between successive iterations of x
    input parameters should be numpy arrays
    """
    return get_euclid_norm(np.subtract(xnew, xold))

def chk_diverge(xold, xnew, A, b):
    """
    check if previous approx of x was closer than new approx of x
    """
    dist_old = get_residual(A, xold, b)
    dist_new = get_residual(A, xnew, b)
    if dist_old < dist_new:
        return True
    else:
        return False   

def chk_converge(A, xnew, b, xold, x_seq_tol, res_tol, flag):
    #checks both residual and x_seq for convergence 
    if flag == True:
        return -1 #required to enter sparse_sor loop
    elif get_residual(A, xnew, b) < res_tol:
        return 2 #dict value for this stopping reason
    elif get_x_seq(xold, xnew) < x_seq_tol:
        return 1
    elif chk_diverge(xold, xnew, A, b) == True:
        return 4
    return -1


    
def sparse_sor(matrix_a, vector_b, matrix_x, dimension_n, max_it=50, \
        x_tol=1e-13, res_tol=1e-13, w=1.25 ):
   
    num_it = 1
    stop_reason = 6 #something has gone wrong if this does not get overwritten later
    matrix_x_last_it = np.array([0.0])
    matrix_x_new = np.array(matrix_x)
    matrix_a_np = np.array(matrix_a)
    vector_b_np = np.array(vector_b)
    
    flag = True #required to enter while loop first time only
    
    while num_it <= max_it and \
        chk_converge(matrix_a_np, matrix_x_new, vector_b_np, matrix_x_last_it, 
                     x_tol, res_tol, flag) == -1:

        flag = False        
        matrix_x_last_it = np.array(matrix_x_new[:])
        for i in range(0,len(vector_b)):
            sum = 0
            first_nz = matrix_a_np[1][(matrix_a_np[2][i]-1)] - 1 #pos of first non zero on row
            for j in range(matrix_a_np[2][i]-1, matrix_a_np[2][i+1]-1):
                sum = sum + matrix_a_np[0][j] * matrix_x_new[j - \
                            (matrix_a_np[2][i]-1) + first_nz]
                if matrix_a_np[1][j] == i+1:
                    d = matrix_a[0][j]
            matrix_x_new[i] = matrix_x_new[i] + w * (vector_b_np[i] - sum) / d   
        num_it+=1
    conv = chk_converge(matrix_a_np, matrix_x_new, vector_b_np, matrix_x_last_it, \
                    x_tol, res_tol, False)
    if num_it-1 == max_it:
        stop_reason = 3
    elif conv != -1:
        stop_reason = conv
#    processIO.output(err.args[1], max_it, num_it, x_tol, res_tol, matrix_x, output_filename,err.args[0])           
#    set_output(stop_reason, max_it, num_it-1, x_tol, res_tol,matrix_x_new, )
    return (stop_reason, max_it, num_it-1, matrix_x_new )
    
def dense_SOR(matrix_a,vector_b,dimension_n,max_iteration,w,matrix_x):
    print("Dense SOR Calculation")
    it_counter=0
    while(it_counter<=max_iteration):
        for row_counter in range(dimension_n):
            sum=0.0
            for col_counter in range(dimension_n):
                sum = sum + matrix_a[row_counter,col_counter]*matrix_x[col_counter]
            matrix_x[row_counter]=matrix_x[row_counter]+w*(vector_b[row_counter]-sum) \
                                                /matrix_a[row_counter,row_counter]
#        print("Iteration: ",it_counter,"\n","X:",matrix_x)    
        it_counter+=1
    return
