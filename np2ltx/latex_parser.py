import numpy as np
from IPython.display import display, Markdown, Math

def matrix2string(M, name):
    ltx = ""
    n, m = M.shape

    # Parse numpy matrix into latex
    for i in range(n):
        for j in range(m):
            entry = M[i,j]
            entry_type = type(entry)
            
            # format according to type
            if entry_type == float:
                ltx += f"{entry:1.4}"
            elif entry_type == bool:
                ltx += str(entry*1)
            else:
                ltx += str(entry)
                
            # next column or next row
            ltx += (" & " if j < m-1 else " \\\\ \n ")
    
    return f"""
            {name} = 
            \\begin{{bmatrix}} \n
            {ltx}
            \\end{{bmatrix}} \n
            """

def print_matrix(M, name):
    ltx = matrix2string(M, name)
    # Display results as latex with some padding
    display(Math(r"\\~\\" + ltx + r"\\~\\"))
    
    
