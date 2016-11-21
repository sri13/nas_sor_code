# -*- coding: utf-8 -*-
"""
All test cases in the NAS Programming assignment are tested here.
Output of execution will be printed on screen on this program execution

How to execute: 
    In Verbose mode - details tests and output
    python automatedTests.py -v 
    In general mode - displays only failed tests
    python automatedTests.py

Authors:
Niall Daly
Ronan Mc.Donagh
Srikanth Tiyyagura
"""

import mainSOR
import sys

def automated_tests():
    '''
    List of all test cases are mentioned below for test
    Agruments:
        None
    Return:
        None
        
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Residual convergence           50                             30                             2.220446049250313e-16          1e-13                          1e-13                         
    [ 1.  2. -2.]

    >>> sys.argv[1] = 'input_files_test_cases/nas_sor_zero_diagonal.in'
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Zero on diagonal               50                             0                              2.220446049250313e-16          1e-13                          1e-13                         
    
    >>> sys.argv[1]='input_files_test_cases/nas_diag_dominant.in'
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    x Sequence convergence         50                             34                             2.220446049250313e-16          1e-13                          1e-13                         
    [ 0.1696  0.2496  0.2496  0.1696]
    
    >>> sys.argv[1]='input_files_test_cases/nas_eigen_val_lt1.in'
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Max Iterations reached         50                             50                             2.220446049250313e-16          1e-13                          1e-13                         
    [ 19.99999908  -9.66666619]

    >>> sys.argv[1]='input_files_test_cases/nas_eigen_val_grt1.in'
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Cannot proceed                 50                             0                              2.220446049250313e-16          1e-13                          1e-13                         
    Spectral radius check failed for Matrix A.
    
    >>> sys.argv[1]='input_files_test_cases/nas_positive_semi_def.in'
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Max Iterations reached         50                             50                             2.220446049250313e-16          1e-13                          1e-13                         
    [ 6.  5.  3.]
    
    >>> sys.argv[1]='input_files_test_cases/nas_large_sparse_matrix_1000.in'
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Cannot proceed                 50                             0                              2.220446049250313e-16          1e-13                          1e-13                         
    Spectral radius check failed for Matrix A.

    >>> sys.argv[1]='input_files_test_cases/nas_ill_condition_matrix.in'
    >>> mainSOR.main()
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Cannot proceed                 50                             0                              2.220446049250313e-16          1e-13                          1e-13                         
    Spectral radius check failed for Matrix A.

    '''
     
    return
    
    
if __name__ == "__main__":
    import doctest
    if(len(sys.argv) > 1):
        sys.argv[1]='nas_Sor.in'
        doctest.testmod(verbose=True)
    else:
        sys.argv.append('nas_Sor.in')
        doctest.testmod(verbose=False)
    
            
    
