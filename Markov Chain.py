# coding: utf-8

#Libraries
import scipy.stats as stat
import numpy as np
from __future__ import division
import math
import matplotlib.pyplot as plt
%matplotlib inline

# Question 1

# Part A

# Intial distribution is px0 = (1 0 0 0 0)

# Part B

#The value of the process are stored in a list X
#The list of songs
Songs=[1,2,3,4,5]
#Start of the Markov chain
X=[0]
#Start of the time
t=0
#The music playlist
Playlist=[]
#while loop - the Markov chain did not reach 5 we go on
while X[t]<5:
    #Incrementation of time
    t=t+1
    #List of played songs
    Playlist.append(np.random.choice(Songs))
    #The number of unique songs played
    X.append(len(np.unique(Playlist)))
#Printing the path of the Markov chain
print X
#Printing the number of steps
print len(X)-1

# Part C
Songs=[1,2,3,4,5]
Paths=[]
#Number of paths to generate
PathNumber=10000
for k in range(0,PathNumber,1):
    #Start of the Markov chain
    X=[0]
    #Startn of the time
    t=0
    #TMusic playlist
    Playlist=[]
    #while loop - the Markov chain did not reach 5 we go on
    while X[t]<5:
        #Incrementation of time
        t=t+1
        #List of played songs
        Playlist.append(np.random.choice(Songs))
        #We look at the number of unique song played
        X.append(len(np.unique(Playlist)))
Paths.append(X)

# Part D

#Function for the mean of N
def MeanT(Paths):
    SampleT=[]
    for element in Paths:
        #The sample of Tau values
        SampleT.append(len(element)-1)
    #Return the sample mean
    return np.mean(SampleT)

#The sample mean for the generated paths
print MeanT(Paths)

# Part E

#Function for the expected value of N
def PMFT(Paths, t):
    is_t=[]
    for element in Paths:
        #Creating a list of boolean to count the number of times that T=t
        is_t.append((len(element)-1)==t)
    #We return the mean to get a MC approximation of the probability
    return np.mean(is_t)
#Printing the value for t = sample mean for the generated paths
#For this process t = 13
print PMFT(Paths,13)

# Part F

#Array of the value for t
tValues=range(0,50,1)
#Array of the value for the PMF
PMFValues = [PMFT(Paths,t) for t in range(0,50,1)]

plt.plot(tValues, PMFValues)
plt.title("PMF of T")
plt.xlabel("t")
plt.ylabel("PMF(t)")
plt.show()