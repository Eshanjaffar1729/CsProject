from matplotlib import pyplot as plt
import openpyxl
import math

#opening Excel sheet and creating an Excel Object
path = "v.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

#defining Some useful variables and lists
X = []
Y = []
l = []
n = 100
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
        MA.append(sigma_x(ra)/5)
    ra=[]

fig, ax = plt.subplots()
ax.plot(X,Y)
ax.plot(X,MA,color="green")
fig.show()

