import numpy as np

def inputDebogger(Input,lastOption):
    while True:
        while True:
            try:
                Input = int(input(""))
                break
            except ValueError:
                print("enter a valid option")
        if int(Input) > 0 and int(Input) <= lastOption:
            return Input
        else:
            print("enter a valid option")

##########################################################################################################################################
def See_Determinant(Matrix,det):
    if Matrix.shape[0] == Matrix.shape[1] :
        det = np.linalg.det(Matrix)
        print(f"determinant = {det}")

    else :
        print(f"your matrix shape have to be a square to find a determinant (current shape: {Matrix.shape[0]} x {Matrix.shape[1]})")


############################################################################################################################################

def See_MatrixRank(matrix,matrixRank):
    matrixRank = np.linalg.matrix_rank(matrix)
    print(f"rank = {matrixRank}")


#############################################################################################################################################

def See_MatrixInverse(matrix):

    if matrix.shape[0] == matrix.shape[1]:
        
        det = np.linalg.det(matrix)
        if det != 0:
            matrix_inverse = np.linalg.inv(matrix)
            print(f"Matrix inverse = \n{matrix_inverse}")
        else:
            print("you matrix can't be inversed (cause --> determinant = 0)")

    else:
        print("you matrix can't be inversed (cause --> not an square matrix)")

#################################################################################################################################################

def See_Comatrix(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        det = np.linalg.det(matrix)
        
        if det != 0:
            comatrix = (det*np.linalg.inv(matrix)).T 
            print(f"comatrix = \n {comatrix}")

        if det == 0:
            print("can't find comatrix (cause --> determinant = 0)")
    
    else:
        print("can't find comatrix (cause --> not a square matrix)")

#################################################################################################################################################

def ScalarOperation(matrix):                    
    MainMenuSO()                   
    actionSO = 0
    actionSO = inputDebogger(actionSO,6)

    if actionSO == 1:
        Multiplication(matrix)

    if actionSO == 2:
        Dvision(matrix)

    elif actionSO == 3:
        Addition(matrix)

    elif actionSO == 4:
        Subtraction(matrix)

    elif actionSO == 5:
        Exponant(matrix)
    
    elif actionSO == 6:
        return
        
    
# # # # # # # # # #  # #  # # # 

def MainMenuSO():
    print("\n{-select a operation-}")
    print("|>--[1] Multiplication")
    print("|>--[2] Division")
    print("|>--[3] Addition")
    print("|>--[4] Subtraction")
    print("|>--[5] Exponant") 
    print("|>--[6] Main Menu")

# # # # # # # # # # #  # # #  #

def Multiplication(matrix):
    while True:
        try:
            scalar = float(input("S = Matrix X "))
            break
        except ValueError:
            print("enter a valid value")

    print(f"\n s = \n{matrix*scalar}")


# # # # # # # # # # #  # # #  #

def Dvision(matrix):

    while True:
            try:
                scalar = float(input("y = "))
                break
            except ValueError:
                print("enter a valid value")

    actionD = 0

    print("\n\nselect an operation order:")
    print(f"[1.] S = {scalar} / matrix")
    if scalar != 0:
        print(f"[2.] S = matrix / {scalar}")
        actionD = inputDebogger(actionD,2)
    
    else:
        actionD = inputDebogger(actionD,1)

    if actionD == 1:
        print(f"S = {scalar} / matrix\nS = \n{scalar / matrix}")
    elif actionD == 2:
        print(f"S = matrix / {scalar}\nS = \n{matrix / scalar}")
    
    

    


# # # # # # # # # # #  # # #  #

def Addition(matrix):
    
    while True:
        try:
            scalar = float(input("choose your scalar :"))
            break
        except ValueError:
            print("enter a valid option")

    print(f"\nmatrix + {scalar} =\n{matrix+scalar}")

# # # # # # # # # # #  # # #  #

def Subtraction(matrix):
    scalar = float(input("enter a scalar: "))
    print("  select an operation order: ")
    print(f" [1]. S = matrix - ({scalar})")
    print(f" [2]. S = {scalar} - matrix")

    actionSub = 0
    actionSub = inputDebogger(actionSub,2)
    
    if actionSub == 1:
        print(f"S = \n{matrix - scalar}")
    
    elif actionSub == 2:
        print(f"S = \n {scalar - matrix}")

# # # # # # # # # # #  # # #  #

def  Exponant(matrix):
    while True:
        try:
            scalar = float(input("(only positive integer are allowed the float number will be rounded)\nenter a exponant : "))
            if scalar < 0 :
                print("only postive integer are allowed")
                continue
            break
        except ValueError:
            print("only postive integer are allowed")
    print(f"matrix^{scalar} = \n{matrix**int(scalar)}")

###########################################################################################################################