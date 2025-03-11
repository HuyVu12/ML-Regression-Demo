import numpy as np

def calc_model(theta_arg, x_in, y_in):
    theta_arg = theta_arg.split()
    m = len(x_in)
    n = len(theta_arg)
    x = np.zeros((m, n))
    y = np.array(y_in).reshape((m, 1))
    for ti in range(len(theta_arg)):
        for i in range(len(x)):
            x[i][ti] = x_in[i]**float(theta_arg[ti]) 
    theta = np.linalg.pinv(x.T @ x) @ x.T @ y
    return theta
def predict(theta_arg, theta, x_in):
    y = 0
    theta_arg = theta_arg.split()
    for i in range(len(theta)):
        y += x_in**float(theta_arg[i]) * theta[i]
    return y
if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]
    theta_arg = '0 2 3'
    print(calc_model(theta_arg, x, y))
