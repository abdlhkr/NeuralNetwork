import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

url = "NeuralNetwork\\datasets\\concrete+compressive+strength\\Concrete_Data.xls"
df = pd.read_excel(url)

print(df.columns)

X = [
    'Cement (component 1)(kg in a m^3 mixture)',
       'Blast Furnace Slag (component 2)(kg in a m^3 mixture)',
       'Fly Ash (component 3)(kg in a m^3 mixture)',
       'Water  (component 4)(kg in a m^3 mixture)',
       'Superplasticizer (component 5)(kg in a m^3 mixture)',
       'Coarse Aggregate  (component 6)(kg in a m^3 mixture)',
       'Fine Aggregate (component 7)(kg in a m^3 mixture)',
       'Age (day)',
]
X = df[X] #(1030, 8)
y = df[['Concrete compressive strength(MPa, megapascals) ']]



train_X, test_X, train_y, test_y = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

train_mean = train_X.mean()
train_std = train_X.std()

train_X = (train_X - train_mean) / train_std
test_X = (test_X - train_mean) / train_std

# burda normalizasyon yapmanın sebebi wx çarpımında x in 
# çok büyük değerler alması ve bu yüzden wx çarpımının çok 
# büyük değerler almasıdır.

# since we are predicting a we will have 1 output node 
# we have 8 features so we will have 8 input nodes
# I will use 2 hidden layers with 8 nodes each and relu activation function

def prepare_weights(layers):
    weights = []
    for i in range(len(layers)):
        if i == len(layers) - 1:
            break
        else:
            weights.append(np.random.rand(layers[i], layers[i+1]))
    return weights

def prepare_bias(layers):
    bias = []
    for i in range(len(layers)):
        if i == len(layers) - 1:
            break
        else:
            bias.append(np.random.rand(layers[i+1]))
    return bias

def relu(x):
    return np.maximum(0, x)


def forward_pass(X,weights,bias):
    z = np.dot(X, weights) + bias
    a = relu(z)
    return (z, a)

def output_layer(X,weights,bias):
    return np.dot(X, weights) + bias

weights = prepare_weights([8, 8, 8, 1])
bias = prepare_bias([8, 8, 8, 1])
for i in weights:
    print(i.shape)
for i in bias:
    print(i.shape)

layer_count = 3
z_values = []
a_values = []

for i in range(layer_count):
    if i == 0:
        result_tuple = forward_pass(train_X, weights[i], bias[i])
        z_values.append(result_tuple[0])
        a_values.append(result_tuple[1])
        a_1 = result_tuple[1]
    elif i == layer_count - 1:
        output = output_layer(a_1, weights[i],bias[i])
        break
    else:
        result_tuple = forward_pass(a_1, weights[i], bias[i])
        z_values.append(result_tuple[0])
        a_values.append(result_tuple[1])
        a_1 = result_tuple[1]



for i in z_values:
    print(i.shape)
for i in a_values:
    print(i.shape)