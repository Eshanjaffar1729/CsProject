from matplotlib import pyplot as plt
import openpyxl
import math

def reverse(x):
    z = []
    for i in range(len(x)-1,-1,-1):
        z.append(x[i])
    return z

def average(x):
    ans = 0
    for elems in x:
        ans += elems
    return ans/len(x)

#opening Excel sheet and creating an Excel Object
path = "v.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

#defining Some useful variables and lists
X = []
Y = []
l = []
n=100
MA =[]

for i in range(2,n+2):
    X.append(i)

for i in range(2,n+2):
    cell_obj = sheet_obj.cell(row = i, column = 2)
    Y.append(cell_obj.value)

Y = reverse(Y)

for i in range(0,n):
    ra = []
    if i<5:
        MA.append(Y[i])
    else:
        for j in range(i-4,i+1):
            ra.append(Y[j])
        MA.append(average(ra))
    ra=[]

fig, ax = plt.subplots()
ax.plot(X,Y)
ax.plot(X,MA,color="green")
fig.show()


