# Matrix Algebra

import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6,0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1, 4])
w = np.matrix([[1], [8], [0], [5]])

#1. Matrix Dimensions
print '1.1 A', A.shape
print '1.2 B', B.shape 
print '1.3 C', C.shape 
print '1.4 D', D.shape 
print '1.5 u', u.shape
print '1.6 w', w.shape

'''
answer:
1.1 A: 2x3
1.2 B: 2x2
1.3 C: 3x2
1.4 D: 2x3
1.5 u: 1x4
1.6 w: 4x1
'''

#2. Vector Operations
#It's easier to do this if we define u and v as arrays (vectors) instead of 1D matrices
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])

print '2.1', u+v
print '2.2', u-v
print '2.3', 6*u
print '2.4', np.dot(u, v)
print '2.5', np.linalg.norm(u)

'''
answer:
2.1: u+v = [6+3, 2+5, -3+-1, 5+4] = [9, 7, -4, 9]
2.2: u-v = [6-3, 2-5, -3--1, 5-4] = [3, -3, -2, 1]
2.3: alpha*u (where alpha = 6) = 6*[6, 2, -3, 5] = [36, 12, -18, 30]
2.4: u.v = [6*3+2*5+-3*-1+5*4] = [18+10+3+20] =51
2.5: ||u||= sqrt(6^2+2^2+(-3)^2+5^2) = sqrt(36+4+9+25) = sqrt(74)=8.6023..
'''

#3. Matrix Operations
#did not include codes for invalid operations (3.1, 3.5, 3.6)

print '3.2'
print A-C.transpose()
print '3.3'
print C.transpose() + 3*D
print '3.4'
print B*A
print '3.7'
print C*B
print '3.8'
print np.linalg.matrix_power(B, 4)
print '3.9'
print A*A.transpose()
print '3.10'
print D.transpose()*D
'''
answer:
3.1 A+C A and C have to have the same dimensions for this. Not defined
3.2 A-transpose(C) = [-4 -7 -3
                       3  6  4]
3.3 transpose(C)+ 3D = [14, 3, 3
                         2, 7, 9]

3.4 BA = [1-2, 2-7, 3-4; 0+2, 0+7, 0+4] =[ -1, -5, -1
                                            2,  7,  4]
3.5 B*transpose(A) : This will not work since # of columns in B must be the same as the number of rows in A-transposed.
    Not defined

3.6 B*C: again, this will not work because B is a 2x2 matrix and C is a 3x2 matrix
    Not defined
    
3.7 C*B = [5 -6
           9 -8
           6 -6]
           
3.8 B^4= B*B*B*B = [1, -4 
                    0, 1]
                    
3.9 A*transpose(A) = [14, 28
                      28, 69]

3.10 transpose(D)*D = [10, -4, 0
                       -4,  8, 8
                        0,  8, 10]


'''