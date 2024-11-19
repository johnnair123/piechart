
import matplotlib.pyplot as plt
dict={"java":22.2,"Python":17.6,"PHP":8.8,"JavaScript":8,"C#":7.7,"C++":6.7}
x=dict.keys()
y=dict.values()
plt.title("popularity of programming language")
plt.pie(y,labels=x,shadow=True,radius=0.6)
plt.show()