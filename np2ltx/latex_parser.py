import numpy as np
from IPython.display import display, Markdown, Math

fprecision = 3
cprecision = 1


def matrix2string(M, name):
    # get dimensions
    dim = M.ndim
    if dim < 2:
        ltx = parse_1d(M)
    elif dim > 2:
        raise ValueError("Matrix must have dimension less then 3")
    else:
        ltx = parse_2d(M)
    return f"""
            {name} = 
            \\begin{{bmatrix}} \n
            {ltx}
            \\end{{bmatrix}}
            """

def parse_1d(M):
    # Parse numpy matrix into latex
    ltx = ""
    n = M.shape[0]
    if n == 0:
        ltx = r"0"
    for i in range(n):
            ltx += parse_entry(M[i])
            ltx += " \\\\ \n "    
    return ltx


def parse_2d(M):
    # Parse numpy matrix into latex
    ltx = ""
    n, m = M.shape
    for i in range(n):
        for j in range(m):
            ltx += parse_entry(M[i,j])
            # next column or next row
            ltx += (" & " if j < m-1 else " \\\\ \n ")
    return ltx

def parse_entry(entry):
    # format according to type
    entry_type = type(entry)
    if entry_type in (float, np.float64):
        return parse_float(entry, fprecision)
    elif entry_type in (bool, np.bool_):
        return str(entry*1)
    elif entry_type == np.complex128:
        return parse_imag(entry)
    return str(entry)

def parse_imag(entry):
    if entry.imag == 0:
        return parse_float(entry.real,fprecision)
    else:
        im = parse_float(entry.imag, cprecision)
        re = parse_float(entry.real, cprecision)
        return f"{re} + i{im}"

def parse_float(entry, precision):
    if round(entry, 4).is_integer():
        return f"{entry:.0f}"
    else:
        return f"{entry:.{precision}f}"

def print_matrix(M, name):
    ltx = matrix2string(M, name)
    # Display results as latex with some padding
    display(Math(r"\\~\\" + ltx + r"\\~\\"))
    
def print_math(equation):
    display(Math(equation))
    
def print_text(text):
    display(Math(r"\text{" + text + r"}"))
