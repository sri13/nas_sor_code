# -*- coding: utf-8 -*-
"""
ProcessIO file handles input and output for this program
Dependent on main program - mainSOR.py

Authors:
Niall Daly
Ronan Mc.Donagh
Srikanth Tiyyagura
"""
#import modules 
import numpy as np
import sys

def input(file_name="nas_Sor.in"):
    '''
        input function reads input file, does basic validations and returns
        dimension of matrix, Matrix A and Vector B of Linear equation form Ax=b
        
        Arguments:
            filename <optional> - file name or uses default file-nas_sor.in saved 
        in the same directory
        
        Return:
            dimension_n -  dimesion of the matrix (square matrix assumption)
            matrix_a - Matrix A from the file
            vector_b - Vector B from the file
    '''
    try:
#        print("File Name:",file_name)
        dimension_n = int(np.genfromtxt(file_name,max_rows=1))
#        print("Dimension n :",dimension_n)
        
        matrix_a = np.genfromtxt(file_name,skip_header=1,skip_footer=1)
#        print("Matrix A :",matrix_a, "Shape:",matrix_a.shape)        
        
        if(matrix_a.shape[0]!=dimension_n or matrix_a.shape[1]!=dimension_n):
            raise Exception('Incorrect File Format for A Matrix dimensions')
        
        vector_b=np.genfromtxt(file_name,skip_header=dimension_n+1)
#        print("Matrix B :",vector_b, "Shape:",vector_b.shape)
        if(vector_b.shape[0]!=dimension_n):
            raise Exception('Incorrect File Format for B Matrix Dimensions')
  
    except OSError:
        print("Input File : ",file_name," not found. ")
        sys.exit()
        
    except Exception as err:
        print(" Input File : ",file_name,"\n","Error: ",err.args[0])
        print(" Please check format of the file. ","\n","Accepted format :","\n\t" \
            " First Line should contain dimension of matrix - n","\n\t", \
            "Next n lines should contain matrix A - n * n ","\n\t",\
            "Last Line should contain matrix B with n rows")
        sys.exit()

    return (dimension_n,matrix_a,vector_b)
    

def output(stop_reason, max_it, num_it, x_tol, res_tol, matrix_x, file_name, \
            stop_cause='something has gone wrong'):
    '''
        output function writes results to the specified file
        Arguments:
            stop_reason - one of the reasons defined below
            max_it - max iterations defined
            num_it - current iteration number
            x_tol - X tolerance value
            res_tol - result tolerance value
            matrix_x - Matrix X values
            file_name - File name 
            stop_cause <optional> - if not below listed reason, use this field
        Return:
            None
    '''
    try:
        stop_reasons = {
        1 : "x Sequence convergence"
        ,2 : "Residual convergence"
        ,3 : "Max Iterations reached"
        ,4 : "X Sequence divergence"
        ,5 : "Zero on diagonal"
        ,6 : "Cannot proceed"
        }
            
#        print("Output File - ",file_name)
        
        header_line = "{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format("Stopping Reason", \
                    "Max num of Iterations","Number of Iterations", \
                    "Machine Epsilon","X Seq Tolerance","Residual Seq Tolerance")
        
        values_line = "{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format(stop_reasons[stop_reason] \
                , max_it, num_it, np.finfo(float).eps, x_tol, res_tol)

#       creates output file, if file doesn't exist in same folder        
        with open(file_name,'w+') as file:
        
            print(header_line)
            file.write(header_line+'\n')
            
            print(values_line)
            file.write(values_line+'\n')
        
            if stop_reason in (1,2,3):
                file.write(np.array_str(matrix_x)+'\n')
                print(matrix_x)
        
            if stop_reason ==6:
                file.write(stop_cause+'\n')
                print(stop_cause)
        
        file.closed
    
    except Exception as err:
        print("Output File - ",file_name," processing error. ",err.args)
        
    return

def to_csr_format(matrix_a):
    """
    to_csr_format reads a full line-by-line matrix and compresses into non-zero
    'rowstart' CSR format

    Arguments:
        matrix_a - matrix that need to be converted to csr form
    Return:
        csr_format_a - Array where row 1 - values, row 2 - columns, row 3 - rowstart
        
    """
    csr_format_a = []
    cols = []
    vals = []
    rowstart = []
    
    row_num = 1
    for each_row in matrix_a:
        col_num = 1
        rowstarted = False

        for val in each_row:            
            if val != 0:
                vals.append(val)
                cols.append(col_num)
                if rowstarted == False:
                    rowstart.append(len(vals))
                    rowstarted = True
            col_num+=1
        row_num+=1
    rowstart.append(len(vals)+1) #final value

    csr_format_a.append(vals)
    csr_format_a.append(cols)
    csr_format_a.append(rowstart)  

    return csr_format_a