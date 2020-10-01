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
            if entry_type in (float, np.float64):
                ltx += f"{entry:.5}"
            elif entry_type in (bool, np.bool_):
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
    
def print_math(equation):
    display(Math(equation))
    
def print_text(text):
    display(Math(r"\text{" + text + r"}"))
