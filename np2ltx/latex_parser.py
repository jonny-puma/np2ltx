def printMatrix(M, name):
    R_ltx = ""
    n, m = M.shape

    # Parse numpy matrix into latex
    for i in range(n):
        for j in range(m):
            R_ltx += f"{M[i,j]:1.4}" + (" & " if j < m-1 else "\\\\\n")

    # Display results as latex with some padding
    display(Math(
        fr"""
        \\~\\
        {name} = 
        \begin{{bmatrix}}
        {R_ltx}
        \end{{bmatrix}}
        \\~\\
        """))
