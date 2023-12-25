import numpy as np
def level3(m):
    # Solving problem using Absobing Markov Chain
    absorb, nonabsorb = states(m)
    if 0 in absorb:
        return [1] + [0]*len(absorb[1:]) + [1] # [1, 0, ..., 0, 1]
    
    m = np.matrix(m, dtype = float)[nonabsorb, :] # Convert m to matrix
    P = m/m.sum(1) # Probability matrix
    common = np.prod(m.sum(1)) # Common denominator
    R, Q = P[:, absorb], P[:, nonabsorb]
    I = np.identity(len(Q))
    F = (I-Q)**(-1) # Fundamental matrix
    FR = (F[0]*R)*(common/np.linalg.det(F))
    return convert(FR)

# Determine absorbing and nonabsorbing states (rows) for later
def states(m):
    absorb, nonabsorb = [],[]
    for index,row in enumerate(m):
        if sum(row):
            nonabsorb.append(index)
        else:
            absorb.append(index)
    return absorb, nonabsorb
    
# Convert probability matrix to final array
def convert(m):
    # Matrix --> Array
    m = m.round().astype(int).A1
    # Find gcd
    gcd = np.gcd.reduce(m)
    # Append sum of elements (unsimplified denominator)
    m = np.append(m, m.sum()) 
    # Divide final result by gcd to simplify
    return (m/gcd).astype(int)
