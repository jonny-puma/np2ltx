import numpy as np
from IPython.display import display, Markdown, Math

def matrix2string(M, name):
    ltx = ""
    n, m = M.shape

    # Parse numpy matrix into latex
    for i in range(n):
        for j in range(m):
            ltx += f"{M[i,j]:1.4}" + (" & " if j < m-1 else " \\ \n ")
    
    return fr"""
            {name} = 
            \begin{{bmatrix}}
            {ltx}
            \end{{bmatrix}}
            """

def printMatrix(M, name):
    ltx = matrix2string(M, name)

    # Display results as latex with some padding
    display(Math("\\~\\" + ltx + "\\~\\"))
    
    
