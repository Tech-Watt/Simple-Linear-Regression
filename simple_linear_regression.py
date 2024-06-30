import numpy as np 

x = np.array([1,2,3,4])
y = np.array([2,4,6])

def gradient(x1,y1,x2,y2):
    return  ((y2-y1)/(x2-x1))

def y_intercept(gradient,x,y):
    return (gradient*x - y)

gradient_value = gradient(1,2,2,4)
print(f'Gradient value is: {gradient_value}')

y_intercept_value = y_intercept(gradient_value,1,2)
print(f'Y_interceptvalue is {y_intercept_value}')

def linear_equation(gradient_value,y_intercept_value,x):
    return gradient_value*x + y_intercept_value

result = linear_equation(gradient_value,y_intercept_value,5)
print(f'Predicted value is: {result}')