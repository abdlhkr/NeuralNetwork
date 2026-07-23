againts lineer regression logistic regression calculates a possiblty for given setuations like spam or not 
![[Pasted image 20260713143405.png]]

Sigmoid function takes any number as an imput and gives a result between 0-1 this type of models called logistic functions

### Transforming linear output using the sigmoid function

The following equation represents the linear component of a logistic regression model:

![[Pasted image 20260713143848.png]]

where:

- _z_ is the output of the linear equation, also called the [**log odds**](https://developers.google.com/machine-learning/glossary#log-odds).
- _b_ is the bias.
- The _w_ values are the model's learned weights.
- The _x_ values are the feature values for a particular example.

To obtain the logistic regression prediction, the _z_ value is then passed to the sigmoid function, yielding a value (a probability) between 0 and 1:

![[Pasted image 20260713143904.png]]

where:

- _y'_ is the output of the logistic regression model.
- _e_ is [Euler's number](https://wikipedia.org/wiki/E_\(mathematical_constant\)): a mathematical constant ≈ 2.71828.
- _z_ is the linear output (as calculated in the preceding equation).

**Click here to learn more about log-odds**

Figure 2 illustrates how linear output is transformed to logistic regression output using these calculations.

Logistic loss : thats the loss I use in cs124 it's easy use log for prevent numerical underflow (it occured because )

![[Pasted image 20260713144532.png]]

- - is for negative liklyhood 