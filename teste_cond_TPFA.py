import numpy as np
import sympy as sym

x=sym.symbols("x")
y=(x+2)**2
z=x**2 + 4*x + 4
d=sym.diff(y,x,0)

# n=10
# A=np.zeros((n,n),dtype=float)
# A[0,0]=1
# A[-1,-1]=1
# for i in range(1,n-1):
#     A[i,i]=-2
#     A[i,i+1]=1
#     A[i,i-1]=1
# I=np.eye(n)
# D=1/A[range(n),range(n)]
# J=D*I
# B=A[1:n-1,1:n-1]
# print(A)
# print(np.linalg.cond(A))
# print(B)
# print(np.linalg.cond(B))
#
# C=D*A
# print(C)
# print(np.linalg.cond(C))
