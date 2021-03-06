# -*- coding: utf-8 -*-
"""
MainSOR program connects remaning modules and serves as a start point

How to Execute:
python mainSOR.py <input_file_name_optional> <output_file_name_optional>

Authors:
Niall Daly
Ronan Mc.Donagh
Srikanth Tiyyagura
"""

#import modules
import sys
import processIO
import implementSOR
import validateMatrix

def main():
    
    try: 
        #Input Processing from input file
        if(len(sys.argv) >= 2):
            [dimension_n,matrix_a,vector_b] = processIO.input(sys.argv[1])
        else:
            [dimension_n,matrix_a,vector_b]=processIO.input()        
        
        #Constants
        max_it = 50
        num_it = 0
        w=1.25
        x_tol=1e-13
        res_tol=1e-13
        matrix_x = processIO.np.zeros(dimension_n)
        
        #Output processing
        if(len(sys.argv) >=3):
            output_filename = sys.argv[2]
        else:
            output_filename = "nas_Sor.out" 
        
        #checks on Matrix A and Vector B 
        if(not validateMatrix.non_zero_diagonal_check(matrix_a,dimension_n)):
            raise Exception("Determinant check failed for Matrix A.",5)
    
        if(not validateMatrix.det_check(matrix_a)):
            raise Exception("Determinant check failed for Matrix A.",6)
            
        if((not validateMatrix.col_diagonally_dominant(matrix_a,dimension_n)) and \
            (not validateMatrix.row_diagonally_dominant(matrix_a,dimension_n))):
#            If matrix is diagonally dominant, then no need to check spectral radius check
                if(not validateMatrix.spectral_radius_convergence_check(matrix_a)):
                    raise Exception("Spectral radius check failed for Matrix A.",6)
                
        #Dense SOR Calculation
#       implementSOR.dense_SOR(matrix_a,vector_b,dimension_n,max_it,w,matrix_x)
        
        #Sparse SOR Calculation
        csr_matrix_a = processIO.to_csr_format(matrix_a)
        
        [stop_reason, max_it, num_it, matrix_x ] = implementSOR.sparse_sor(csr_matrix_a, \
        vector_b, matrix_x, dimension_n, max_it, x_tol, res_tol, w )
        
        processIO.output(stop_reason, max_it, num_it, x_tol, res_tol, matrix_x,\
                output_filename)           
    
    except Exception as err:
#        print("Error occured: ",err.args[0],err.args[1])
        processIO.output(err.args[1], max_it, num_it, x_tol, res_tol, matrix_x, \
            output_filename,err.args[0])
            
    return


if __name__ == "__main__":
    main()