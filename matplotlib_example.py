# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 11 Group
# Date:         10 11 2023
import matplotlib.pyplot as plt
import numpy
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

#plot 1
f = 2
x = numpy.linspace(-2,2)
#print(x)
y = (1/(4*2))*x**2
y2 = (1/(4*6))*x**2
fig,ax = plt.subplots()
ax.plot(x,y,linewidth=2.0,label="f=2")
ax.plot(x,y2,linewidth=6.0,label="f=6")
ax.set_title("Parabola plots with varying focal length")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
#plt.show()
#plot 2
x = numpy.linspace(-4,4,25)
f = 2*x**3 + 3*x**2 - 11*x -6
fig2,ax2 = plt.subplots()
ax2.plot(x,f,"*y",markeredgecolor="black",markeredgewidth=0.4)
ax2.set_title("Plot of cubic polynomial")
ax2.set_xlabel("x values")
ax2.set_ylabel("y values")
#plt.show()
#plot 3
x = numpy.linspace(numpy.pi*-2,numpy.pi*2)
graph1 = numpy.cos(x)
graph2 = numpy.sin(x)
fig3,ax3 = plt.subplots(2,1)
fig3.suptitle("Plot of cos(x) and sin(x)")
ax3[0].plot(x,graph1,label="cos(x)",color="blue")
ax3[1].plot(x,graph2,label="sin(x)",color="red")
ax3[0].legend(loc="lower right")
ax3[1].legend(loc="upper right")
ax3[0].tick_params(axis="x",labelbottom=False)
ax3[0].set_yticks(numpy.arange(-1,1.01,1))
ax3[1].set_yticks(numpy.arange(-1,1.01,1))
ax3[0].set_ylabel("y=cos(x)")
ax3[1].set_ylabel("y=sin(x)")
ax3[0].grid()
ax3[1].grid()
plt.show()