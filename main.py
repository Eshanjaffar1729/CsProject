from matplotlib import pyplot as plt
import  mysql.connector 
import math
import LoadingData

def average(x):
    ans = 0
    for elems in x:
        ans += elems
    return ans/len(x)

db = mysql.connector.connect(host="localhost",user="root",passwd="27182818284590",database="stock1")
mc = db.cursor()




#defining Some useful variables and lists
X = []
Y = []
l = []
n=100
MA =[]

for i in range(1,n+1):
    X.append(i)

mc.execute("select val from price")
val = mc.fetchall()


for i in range(0,n):
    Y.append(int(val[i][0]))



for i in range(0,n):
    ra = []
    if i<5:
        MA.append(Y[i])
    else:
        for j in range(i-4,i+1):
            ra.append(Y[j])
        MA.append(average(ra))
    ra=[]


mc.execute("alter table price add column pred NUMERIC(7,2)")
for i in range(1,n+1):
    prediction = MA[i-1]
    mc.execute("update price set pred={} where Dnum={}".format(prediction,i))
db.commit()

fig, ax = plt.subplots()
ax.plot(X,Y)
ax.plot(X,MA,color="green")
fig.show()

