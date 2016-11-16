# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 00:16:28 2016

@author: sk
"""

import mainSOR
import sys

def automated_tests():
    '''
    >>> mainSOR.main()
    Output File -  nas_Sor.out
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Residual convergence           50                             30                             2.220446049250313e-16          1e-13                          1e-13                         
    [ 1.  2. -2.]

    >>> sys.argv.append('nas_Sor.in.err')
    >>> mainSOR.main()
    Output File -  nas_Sor.out
    Stopping Reason                Max num of Iterations          Number of Iterations           Machine Epsilon                X Seq Tolerance                Residual Seq Tolerance        
    Cannot proceed                 50                             0                              2.220446049250313e-16          1e-13                          1e-13                         
    Matrix A wont converge as it is not row / column diagonally dominant.

    '''
     
    return
    

    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)