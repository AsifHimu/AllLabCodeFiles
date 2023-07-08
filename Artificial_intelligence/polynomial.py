import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow import keras
import tensorflow as tf

x = np.arange(-10,10, .01)
#print(x)
y = 3*x**3 + 7*x**2 - 12*x + 2
#print(y)
model = keras.Sequential([
    keras.layers.Dense(32, input_shape=(1,),activation='relu'),
    keras.layers.Dense(64,activation='relu'),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(1),
])
#model.summary()
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x, y, epochs=100)
a = np.array([-3,-2,-1,0,1,2,3])
b = 3*a**3 + 7*a**2 - 12*a + 2
#print(b)
model.predict(a)
out = model.predict(a)
i = 0
print("Input"+"   "+"Predicted"+"  "+"Actual")
for idx in range(-3,4):
  print("x = {}, y = {res:.2f},  b =".format(idx, res=out[i][0]),b[i])
  i += 1