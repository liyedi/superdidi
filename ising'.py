# a Monte Carlo simulation for 2-D Ising model 
# author:liyedi
# date:2019/4/27
import numpy as np
import matplotlib.pyplot as plt
import random
import math
#import time
N=60    # size of matrix
S=np.ones([N,N])  #array to store system
P=np.empty([N,N])  #the probility of inversion
x=np.zeros([N,N]) #x is the number of the point same as the s[i][j]
T=1.0#reduced unit J/kt
l=0.0
# calculate the probility
#x is the number of the point same as the s[i][j]
def init(S):
    for m in range (0,3600):
      i=random.randint(0,59)
      j=random.randint(0,59)
      S[i][j]=-S[i][j]
def prob(x):
    i=random.randint(0,59)
    j=random.randint(0,59)
    if i==59 and j==59:
        if S[i][j]==S[i-1][j]:
                  x[i][j]=x[i][j]+1
        if S[i][j]==S[0][j]:
                  x[i][j]=x[i][j]+1
        if S[i][j]==S[i][j-1]:
                  x[i][j]=x[i][j]+1 
        if S[i][j]==S[i][0]:
                  x[i][j]=x[i][j]+1
    elif i==59 and j!=59:
        if S[i][j]==S[i-1][j]:
                  x[i][j]=x[i][j]+1
        if S[i][j]==S[0][j]:
                  x[i][j]=x[i][j]+1
        if S[i][j]==S[i][j-1]:
                  x[i][j]=x[i][j]+1 
        if S[i][j]==S[i][j+1]:
                  x[i][j]=x[i][j]+1
                  
    elif i!=59 and j==59:
        if S[i][j]==S[i-1][j]:
                  x[i][j]=x[i][j]+1
        if S[i][j]==S[i+1][j]:
                  x[i][j]=x[i][j]+1
        if S[i][j]==S[i][j-1]:
                  x[i][j]=x[i][j]+1 
        if S[i][j]==S[i][0]:
                  x[i][j]=x[i][j]+1
                      
    else:   
        
       if S[i][j]==S[i-1][j]:
                  x[i][j]=x[i][j]+1
       if S[i][j]==S[i+1][j]:
                  x[i][j]=x[i][j]+1
       if S[i][j]==S[i][j-1]:
                  x[i][j]=x[i][j]+1 
       if S[i][j]==S[i][j+1]:
                  x[i][j]=x[i][j]+1  
      
    if x[i][j]<=2:
                  P[i][j]=1
    elif x[i][j]==3:
                  P[i][j]=math.exp(-4/T)
    else:
                  P[i][j]=math.exp(-8/T)  
# compare random num with probility
    a=random.uniform(0,1)
    #print a
    global l
    
    if P[i][j]>=a:
            S[i][j]=-S[i][j]
            l=l+1        
    P[i][j]=0
    x[i][j]=0
    return S
#calculate M                 
def mag(S):
     m=0
     for i in range (0,N):
          for j in range (0,N):
              m=m+S[i][j]
     return m/np.square(N)
#calculate energe
'''
def energe(S):
    
   ener=0
   for i in range(N):
        for j in range(N):            
            ener += -(S[(i+1)%N,j]+S[i,(j-1)%N]+S[(i-1)%N,j]+S[i,(j+1)%N])*S[i,j]/2.0
   return ener/(N*N)
   '''
def simulation(step):
    #step=100
    M=np.empty([2778])
    #E=np.empty([2778])
    a=np.arange(0,1000000,360)
    #a=np.linspace(0, step, step, endpoint=False)
    init(S)
    for n in range (0,step):
        prob(x)
        if n%360==0:
          M[n/360]=mag(S)
          #E[n/360]=energe(S)
    
    #mean=np.mean(M)
    #print("mean=",mean)
    '''
    plt.figure(figsize=(6,4))  
    plt.plot(a,E,color="red",linewidth=1)
    plt.xlabel("MCstep/N") 
    plt.ylabel("E/N")
    plt.title("2DIsing model") 
    '''
    plt.figure(figsize=(6,4))  
    plt.plot(a,M,color="black",linewidth=1) 
    plt.xlabel("MCstep/N") 
    plt.ylabel("M/N")
    plt.title("2DIsing model") 
    plt.legend()
    plt.show()
    print("accept rate= ",l/step)
    #print (l)
    
res=simulation(1000000)   
    
                 
           
    

