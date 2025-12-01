import numpy as np
data=np.array([33,34,35,120,36,32,200])
Q1=np.percentile(data,25);Q3=np.percentile(data,75)
IQR=Q3-Q1
l=Q1-1.5*IQR;u=Q3+1.5*IQR
clean=[x for x in data if l<=x<=u]\print(clean)