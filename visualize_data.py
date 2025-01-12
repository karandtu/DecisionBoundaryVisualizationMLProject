import matplotlib.pyplot as plt
import numpy as np
from generate_data import generate_random_data


def plot_random_generated_data():
     """
     Plot the data points and the decision boundary for:
     y= (X[:,0] + X[:,1] >0).astype(int)
     """
     X,y = generate_random_data()

#Plot the data points
     plt.scatter(X[y==0][:,0],X[y==0][:,1],color="blue",label="Class 0(y=0)")
     plt.scatter(X[y==1][:,0],X[y==1][:,1],color="red",label="Class 1(y=1)")


#Plot the decision boundary
     #creates an evenly spaced values between start X[:,0].min() and X[:,0].max()
     #We do -1 to extend beyond minimum and +1 to extend beyond maximum for better visuals.
     # #so we perform extra slight stretch to base our better visual results.
     x_vals = np.linspace(X[:,0].min()-1,X[:,0].max()+1,100)
     #e.g. if x_vals = [0.1,-1.5,0.4,1.4,3.5], then y_vals = [-(0.1),-(-1.5),-0.4,-1.4,-3.5]
     #y_vals=[0.1,1.5,-0.4,-1.4,-3.5], so y_vals would be negating all of whats in x_vals.
     y_vals = -x_vals
     plt.legend()
     plt.grid(True)
     plt.show()

if __name__ == '__main__':
    plot_random_generated_data()







