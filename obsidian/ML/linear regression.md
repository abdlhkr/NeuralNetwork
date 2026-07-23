in lineer regression we have our properties wich is x1,x2...xn
and for each property we try to create best lineer equation wich is y = mx + b ml it's y' = b + w1 * x1
	this equation is same as mx + b  , b is same w is the slope and x1 is feature value 

![Figure 2. Data points with a best fit line drawn through them representing the model.](https://developers.google.com/static/machine-learning/crash-course/linear-regression/images/car-data-points-with-model.png)

Loss :
loss is the differences between our prediction and actual value since lineer regression is a  supervised machile learning model we  actually know the labels then loss always count as absoute differences between points if our predictment 5 and actual value is 1 then loss is |1 - 5| = 4 there different kind of losses for training model in logistic regression 

| Loss type                                                                                                                  | Definition                                                                                           | Equation                                                |
| -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **[L1 loss](https://developers.google.com/machine-learning/glossary#l1-loss)**                                             | The sum of the absolute values of the difference between the predicted values and the actual values. | ∑ \|Actual value - Predicted value\|                    |
| **[Mean absolute error (MAE)](https://developers.google.com/machine-learning/glossary#mean-absolute-error-mae)**           | The average of L1 losses across a set of _N_ examples.                                               | 1 / n ∑ \|Actual Value - Predicted Value\|              |
| **[L2 loss](https://developers.google.com/machine-learning/glossary#l2-loss)**                                             | The sum of the squared difference between the predicted values and the actual values.                | ∑ (Actual Value - predicted value)**2                   |
| **[Mean squared error (MSE)](https://developers.google.com/machine-learning/glossary#mean-squared-error-mse)**             | The average of L2 losses across a set of _N_ examples.                                               | 1 / N (actual value  - predicted valıe ) ** 2           |
| **[Root mean squared error (RMSE)](https://developers.google.com/machine-learning/glossary#root-mean-squared-error-rmse)** | The square root of the mean squared error (MSE).                                                     | squareroot(1 / n ∑ (actual value - predicted value)**2) |


When choosing the best loss function, consider how you want the model to treat outliers. For instance, MSE moves the model more toward the outliers, while MAE doesn't. L2 loss incurs a much higher penalty for an outlier than L1 loss.  For example, the following images show a model trained using MAE and a model trained using MSE. The red line represents a fully trained model that will be used to make predictions. The outliers are closer to the model trained with MSE than to the model trained with MAE.

![Figure 9. The model is tilted more toward the outliers.](https://developers.google.com/static/machine-learning/crash-course/linear-regression/images/model-mse.png)

**Figure 9**. MSE loss moves the model closer to the outliers.

![Figure 10. The model is tilted further away from the outliers.](https://developers.google.com/static/machine-learning/crash-course/linear-regression/images/model-mae.png)

**Figure 10**. MAE loss keeps the model farther from the outliers.

Note the relationship between the model and the data:

- **MSE**. The model is closer to the outliers but further away from most of the other data points.
    
- **MAE**. The model is further away from the outliers but closer to most of the other data points

from this line I will be repeating cross entropy loss from cs124


that's used for logistic regression
σ(x)=1 /  1+e ^−x1​ sigmoid function takes an input and turns it into a number between 0 and 1 
![[Pasted image 20260712180145.png]]

y =  label real  value 
y ' =  predicted value 
formula = L(y,y^​)=−[y * log(y^​)+(1−y) * log(1 − y^​)]
lets say real answer is 1  then secon part of the equation wich is 
(1−y) * log(1 − y^​) = 0 since 1 - y = 1 - 1 = 0 and loss is 
		LOSS = y * log(y^​) wich is log (predicted value)

if the answer is 0 then first part of the equation y * log(y^​) = 0
and the loss is 
	 LOSS = (1−y) * log(1 − y^​) wich is log(1-predicted value)

![[Pasted image 20260712181631.png]]

Gradient Descent: Find the gradient of the loss
function at the current point and move in the
opposite direction.
![[Pasted image 20260712181849.png]]

![[Pasted image 20260712182002.png]]


![[Pasted image 20260712182058.png]]


![[Pasted image 20260712182336.png]]

![[Pasted image 20260712182351.png]]

![[Pasted image 20260712182403.png]]

if u are reading this just watch https://youtu.be/TDOCw0L-qz0?si=CK9WSP7cXu814_Uk and next 2 videos its awsome 