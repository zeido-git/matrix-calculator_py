import numpy as np
from module.SetMatrix import Amatrix
from module.SetMatrix import no_matrix
from module.SetMatrix import setshape
from module.SetMatrix import SetBMatrix
from module.MatrixOperation import See_Determinant
from module.MatrixOperation import See_MatrixRank
from module.MatrixOperation import See_MatrixInverse
from module.MatrixOperation import See_Comatrix
from module.MatrixOperation import ScalarOperation


def main_menu():
    print("\n[===[==[=[=[-[_[Matrix Calculator]_]-]=]=]==]===]\n")
    print("1} Create matrix / Change matrix")
    print("2} See matrix")
    print("3} See matrix determinant")
    print("4} See matrix rank")
    print("5} See matrix inverse")
    print("6} See Comatrix")
    print("7} Do operations with scalars")
    print("8} Make a matrix product with another matrix")
    print("9} Exit")

A_matrix_shape = 0
have_matrix = False

while True:
    matrix_Determinant = 0
    matrix_Rank = 0

    action = 0
    main_menu()
    while True:
        while True:
            try :
                action = int(input("\n"))
                break
            except ValueError:
                print("enter a valid option")
        if action > 0 and action <=9:
            break
        else:
            continue
    
    if action == 1:
        A_matrix_shape = setshape()
        line = A_matrix_shape[0]
        columns = A_matrix_shape[1]
        A_Matrix = Amatrix(line,columns)
        have_matrix = True
        continue
    
    elif action == 2:
        if have_matrix == True:
            print(A_Matrix)
        else:
            action = no_matrix()

    elif action == 3:
        if have_matrix == True:
            See_Determinant(A_Matrix,matrix_Determinant)
        elif have_matrix == False:
            action = no_matrix()

    elif action == 4:
        if have_matrix == True:
            See_MatrixRank(A_Matrix,matrix_Rank)
        else:
            action = no_matrix()

    elif action == 5:
        if have_matrix == True:
            See_MatrixInverse(A_Matrix)
        else:
            action = no_matrix()

    elif action == 6:
        if have_matrix == True:
            See_Comatrix(A_Matrix)
        else:
            action = no_matrix()


    elif action == 7:
        if have_matrix == True:
            ScalarOperation(A_Matrix)
        else:
            action = no_matrix()

    
    elif action == 8:
        if have_matrix == True:
            SetBMatrix(A_Matrix)
        else: 
            action = no_matrix()


    if action == 1:
            A_matrix_shape = setshape()
            line = A_matrix_shape[0]
            columns = A_matrix_shape[1]
            A_Matrix = Amatrix(line,columns)
            have_matrix = True
            continue
    if action == 9:
        break
    