import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,4,9,16]) #by  default it takes y as its input and autometically generates  x values.
# but when you give 2 values it takes it as (x,y) values
plt.ylabel("y axis") # naming axises
plt.xlabel("x axis")
plt.show()
plt.plot([1,2,3,4],[1,16,24,32],'ro') # here ro means it will print data as red dots, rs means red squares,
#  g^ means green triangles, 'r--' stands for red dashed lines and by default it is a blue line.
plt.show()