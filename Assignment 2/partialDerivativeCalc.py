import sys
from sympy import symbols, diff, parse_expr

print ("Welcome to the Python partial derivative tool! Press CTRL+C anytime to quit.")
print ()

numLoops = 0

while True:
    numLoops += 1
    print ("=====Function #" + str(numLoops) + "=====")
    print ()

    # Ask the user for the number of variables to be used in the function
    numVars = -1

    while numVars < 0:
        print ("How many variables should the function have?")
        numVars = int(input ())

        if numVars < 0:
            print ("The number of variables MUST be a non-negative number!")
        print ()

    # Generate the variables to be used in the function
    varNames = [f'x{i}' for i in range(1, numVars+1)]
    print ("Function variables generated! Their names are as follows:")
    for name in varNames:
        print (name)
    print ()

    # Ask user if they want to rename the variables
    print ("Would you like to rename the variables? (y/n)")
    renameChoice = str(input ())
    print ()

    if renameChoice == 'y' or renameChoice == 'Y':
        newVarNames = []

        for i in range(len(varNames)):
            validName = False

            while validName == False:
                print (f"Please enter the new name for variable {varNames[i]}:")
                newName = str(input ())

                if newName == 'e' or newName in newVarNames:
                    print ("Invalid variable name! Variables cannot be repeated and they cannot be named e.")
                else:
                    newVarNames.append (newName)
                    validName = True
        print ()
        varNames = newVarNames

        print ("Function variables renamed! Their new names are as follows:")
        for name in varNames:
            print (name)
    print ()
    funcSymbols = tuple(symbols(name) for name in varNames)

    # Ask the user to enter their function
    validExpr = False
    funcExpr = None

    while validExpr == False:
        validExpr = True

        print ("Please enter the expression for the function you'd like to differentiate.")
        print ("Note that multiplication MUST be explicit (enter 2*x*y instead of 2xy).")
        print ("Enter your expression below:")
        funcExprStr = str(input ())

        # Preprocess expression string
        funcExprStr = funcExprStr.replace('^', '**')

        # Check if the expression is blank
        if funcExprStr == '':
            validExpr = False

        # Check if the correct variables were used
        try:
            funcExpr = parse_expr (funcExprStr, local_dict={str(v): v for v in funcSymbols})
        except Exception as e:
            print ("There was an error with your entered expression! Please ensure that the proper variables and formatting was used.")
            print ("Your expression: " + funcExprStr)
            print ("Error message: " + e)
            validExpr = False
        print ()
    print(f"Your final function is: f({', '.join(varNames)}) = {str(funcExpr).replace ('**', '^')}")
    print ()
    
    # Differentiate the function with respect to each provided variable
    print ("Partial Derivatives:")
    for symbol in funcSymbols:
        partialDeriv = str(diff(funcExpr, symbol)).replace ('**', '^')
        print (f"With respect to {symbol}: {partialDeriv}")
    print ()

    # Ask user if they want to continue
    print ("Would you like to differentiate another function? (y/n)")
    contChoice = str(input ())

    if contChoice == 'n' or contChoice == 'N':
        print ("Quitting program...")
        sys.exit ()
    print ()