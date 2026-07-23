learning rate : it determines how much each weight change for each iteration if your loss 3 and Learning Rate N = 0.1 then each parameter will change -(the valeu of it  * 0.3) Lets say you are working with lexicons positive or negative word values and x1 is positive word lets say 3 then your w1 weight will dicreese by 0.9

İMPORTANT : you can't give a large value it will bounce between gradient and never found the best ALSO you shouldn't give it a small calue unless u wanna make trainnig infinite 

Batch Size : it refers to how many example will be used before updating the weights and bias there two common method 

**Stochastic gradient descent (SGD)**: Stochastic gradient descent uses only a single example (a batch size of one) per iteration. Given enough iterations, SGD works but is very noisy. "Noise" refers to variations during training that cause the loss to increase rather than decrease during an iteration. The term "stochastic" indicates that the one example comprising each batch is chosen at random. My example above is this one 

**Mini-batch stochastic gradient descent (mini-batch SGD)**: Mini-batch stochastic gradient descent is a compromise between full-batch and SGD. For N  number of data points, the batch size can be any number greater than 1 and less than N . The model chooses the examples included in each batch at random, averages their gradients, and then updates the weights and bias once per iteration.

Epochs : During training, an epoch means that the model has processed every example in the training set _once_. For example, given a training set with 1,000 examples and a mini-batch size of 100 examples, it will take the model 10 iterations to complete one epoch.

Training typically requires many epochs. That is, the system needs to process every example in the training set multiple times.

The number of epochs is a hyperparameter you set before the model begins training. In many cases, you'll need to experiment with how many epochs it takes for the model to converge. In general, more epochs produces a better model, but also takes more time to train.

The following table describes how batch size and epochs relate to the number of times a model updates its parameters.

| Batch type                             | When weights and bias updates occur                                                                                                                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Full batch                             | After the model looks at all the examples in the dataset. For instance, if a dataset contains 1,000 examples and the model trains for 20 epochs, the model updates the weights and bias 20 times, once per epoch.         |
| Stochastic gradient descent            | After the model looks at a single example from the dataset. For instance, if a dataset contains 1,000 examples and trains for 20 epochs, the model updates the weights and bias 20,000 times.                             |
| Mini-batch stochastic gradient descent | After the model looks at the examples in each batch. For instance, if a dataset contains 1,000 examples, and the batch size is 100, and the model trains for 20 epochs, the model updates the weights and bias 200 times. |