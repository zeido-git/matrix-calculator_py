import numpy as np

def Amatrix(line,columns):
    A = np.zeros((line,columns))

    for i in range(0,line):
        while True:
            try:
                line_tmpr = [float(x) for x in input(f"set matrice line {i+1}:   ").split()]
            
                if len(line_tmpr) != columns:
                    while len(line_tmpr) != columns:
                            print(f"\npls enter {columns} values (separate the values with spaces)")
                            line_tmpr = [float(x) for x in input(f"\nset matrice line {i+1}:   ").split()]
                break            
            except ValueError:
                print("enter valid number")
                
        A[i,:] = line_tmpr

    return A

###############################################################################################################################################

def no_matrix():
    tmpr_action = tmpr_action = input("you dont have any matrix created\ndo you want to create one ? [Y/n]")
    while True:
        if tmpr_action == 'y' or tmpr_action == 'Y' or tmpr_action == 'yes' or tmpr_action == 'Yes':
            return 1
        elif tmpr_action == 'n' or tmpr_action == 'N' or tmpr_action == 'no' or tmpr_action == 'No':
            return 0
        else:
            tmpr_action = input("enter a valid option [Y/n]")

################################################################################################################################################

def setshape():
    while True:
        try: 
            line = int(input("how much lines your matrix have: "))
            break
        except ValueError:
            print("enter a valid number")
            continue
    while True:
        try: 
            columns = int(input("how much columns your matrix have: "))
            break
        except ValueError:
            print("enter a valid number")
            continue
    
    shape = [line,columns]
    return shape

###################################################################################################################################################


def SetBMatrix(matrix):
    print("you will set the Matrix B for matrix product \n\n(the line of matrix B need to be the same amount as the columns of matrix A)") 
    while True:
        shape = setshape()
        line = shape[0]
        columns = shape[1]
        if matrix.shape[1] != line:
            print(f"ERROR, the shape of ur matrix B are not compatible (A∈Ꮇ{matrix.shape[0]}*{matrix.shape[1]}; B∈Ꮇ{line}*{columns})")
            continue
        break

    b_matrix = Amatrix(line,columns)

    print(f"A ⊙ B =\n{matrix@b_matrix}")