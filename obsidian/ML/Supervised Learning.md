Regression Informally, a model that generates a numerical prediction. (In contrast, a [**classification model**](https://developers.google.com/machine-learning/glossary#classification_model) generates a class prediction.) For example, the following are all regression models:

- A model that predicts a certain house's value in Euros, such as 423,000.
- A model that predicts a certain tree's life expectancy in years, such as 23.2.
- A model that predicts the amount of rain in inches that will fall in a certain city over the next six hours, such as 0.18.

Two common types of regression models are:

- [**Linear regression**](https://developers.google.com/machine-learning/glossary#linear_regression), which finds the line that best fits label values to features.
- [**Logistic regression**](https://developers.google.com/machine-learning/glossary#logistic_regression), which generates a probability between 0.0 and 1.0 that a system typically then maps to a class prediction.

Not every model that outputs numerical predictions is a regression model. In some cases, a numeric prediction is really just a classification model that happens to have numeric class names. For example, a model that predicts a numeric postal code is a classification model, not a regression model.

PART of it

first come to DATA
data is  to source of every model important part is its size and diversity making predictions need lots of data from diverse thing(I dont know how to explain it ) lets say u wanna make a weither prediction if your data only contain degree and clodiness then the model might not be good enough to predict weither but feature count isnt enough to say that it will be good 10 years of data will produce a model then 1 year data since it contains larger diversity of weither through years 
large size of data and diversity is nice for data

Other parts are model are training model is the mathematical thing going around and training a model means giving labeled expamples to model and make it learn the connection between features and main label some features might be more important then others so picking features for a model also improtant

lest part is evaluating giving models features that are actually labeled but give it only features and evaluate its correctness 
with it lets model say its a a a b but actual is a a b b then it could  be %75 