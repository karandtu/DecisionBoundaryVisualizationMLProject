import numpy as np

def generate_random_data(n_samples=100,seed=42):
      """
      Generate random synthetic 2D data and assign labels based on the condition
      y= (X[:,0] + X[:,1] >0).astype(int)
      """

      np.random.seed(seed)
      X=np.random.randn(n_samples,2)
      y=(X[:,0] + X[:,1] >0).astype(int)
      return X,y


if __name__ == '__main__':
    X, y = generate_random_data()
    print("Generated data")
    print(f"Features : (X[:,5]")
    print(f"Labels : (y[:,5])")




