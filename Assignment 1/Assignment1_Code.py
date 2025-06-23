# QUESTION 3
x1 = [1, 1,5,2,7,9] # Label = 1
x2 = [1, -3,8,2,4,6] # Label = 0
w = [0, -1,0,0,0,0]

# First element in vector x must be 1.
# Length of w and x must be n+1 for neuron with n inputs.
def compute_output(w, x):
    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i] # Compute sum of weighted inputs
    
    print (z)
    if z < 0: # Apply step function
        return 0
    else:
        return 1

print ("Example 1: " + str (compute_output(w, x1)))
print ("Example 2: " + str (compute_output(w, x2)))







# QUESTION 5
x = [1, 1,0,0,0,0,0]
w = [0, -1,-1,-1,-1,-1,-1]
w[0] = (len (w)) / 2 - 1 # Set bias to half the size of the input (minus the bias)

# First element in vector x must be 1.
# Length of w and x must be n+1 for neuron with n inputs.
def compute_output(w, x):
    if len (w) != len (x):
      raise Exception("Weight and input vectors have different sizes")

    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i] # Compute sum of weighted inputs
    
    print (z)
    if z < 0: # Apply step function
        return 0
    else:
        return 1

print ("Output: " + str (compute_output(w, x)))