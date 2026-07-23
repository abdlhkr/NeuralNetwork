Let's say you have a logistic regression model for spam-email detection that predicts a value between 0 and 1, representing the probability that a given email is spam. A prediction of 0.50 signifies a 50% likelihood that the email is spam, a prediction of 0.75 signifies a 75% likelihood that the email is spam, and so on.

You'd like to deploy this model in an email application to filter spam into a separate mail folder. But to do so, you need to convert the model's raw numerical output (e.g., `0.75`) into one of two categories: "spam" or "not spam."

To make this conversion, you choose a threshold probability, called a [**classification threshold**](https://developers.google.com/machine-learning/glossary#classification-threshold). Examples with a probability above the threshold value are then assigned to the [**positive class**](https://developers.google.com/machine-learning/glossary#positive_class), the class you are testing for (here, `spam`). Examples with a lower probability are assigned to the [**negative class**](https://developers.google.com/machine-learning/glossary#negative_class), the alternative class (here, `not spam`).

![[Pasted image 20260721161856.png]]

the total of each row gives predicted positive, predicted negative
and total of each column gives actual positive and negative values

When the total of actual positives is not close to the total of actual negatives, the dataset is [**imbalanced**](https://developers.google.com/machine-learning/glossary#class_imbalanced_data_set). An instance of an imbalanced dataset might be a set of thousands of photos of clouds, where the rare cloud type you are interested in, say, volutus clouds, only appears a few times.

## Why the dataset matters when choosing a classification threshold

A classification model usually produces a **probability**, not a final class.

For example:

```
Probability of fraud = 0.72
```

A threshold converts this probability into a prediction:

```
If probability ≥ threshold → Positive
If probability < threshold → Negative
```

The default threshold is often **0.50**, but 0.50 is not automatically the best choice.

### 1. Class distribution affects threshold selection

Suppose a dataset contains:

- 99% normal transactions
- 1% fraudulent transactions

This is an **imbalanced dataset**.

A model could predict every transaction as normal and still achieve 99% accuracy. Therefore, accuracy would be misleading.

In such datasets, metrics such as **precision, recall, F1-score, and PR-AUC** are usually more useful.

The threshold should be chosen using a **validation dataset** whose class distribution is similar to real-world data.

Do not select the threshold using the test set. The test set should only be used for the final evaluation.

---

### 2. The dataset must represent real-world conditions

Threshold selection depends heavily on the data used during evaluation.

The validation dataset should represent:

- The real positive-negative ratio
- Different user groups or customer types
- Difficult and unusual examples
- Recent real-world data
- Possible noise or missing values

For example, if fraud is much more common in the validation dataset than in production, the selected threshold may not work well after deployment.

---

### 3. Different thresholds create different trade-offs

Lowering the threshold usually causes:

- More positive predictions
- Higher recall
- More false positives
- Lower precision

Increasing the threshold usually causes:

- Fewer positive predictions
- Higher precision
- More false negatives
- Lower recall

For example:

|Threshold|Precision|Recall|
|---|---|---|
|0.30|0.55|0.94|
|0.50|0.73|0.81|
|0.70|0.90|0.52|

There is no universally correct threshold. The correct threshold depends on the business problem and the cost of errors.

---

## How to decide which metric to use

### Recall

Recall=TPTP+FNRecall = \frac{TP}{TP+FN}Recall=TP+FNTP​

Recall answers:

> Of all actual positive cases, how many did the model detect?

Use recall when **missing a positive case is dangerous or expensive**.

Examples:

- Cancer detection
- Fraud detection
- Fire or security alarms
- Detecting defective products
- Identifying dangerous content

In these problems, false negatives are especially costly.

---

### Precision

Precision=TPTP+FPPrecision = \frac{TP}{TP+FP}Precision=TP+FPTP​

Precision answers:

> Of all cases predicted as positive, how many were actually positive?

Use precision when **false alarms are expensive or harmful**.

Examples:

- Automatically blocking bank accounts
- Marking legitimate emails as spam
- Recommending legal action
- Automatically rejecting job applications
- Sending expensive investigation teams

In these problems, false positives are especially costly.

---

### F1-score

F1=2×Precision×RecallPrecision+RecallF1 = 2 \times \frac{Precision \times Recall}{Precision+Recall}F1=2×Precision+RecallPrecision×Recall​

F1-score balances precision and recall.

Use it when:

- Both false positives and false negatives matter
- The dataset is imbalanced
- You want one summary metric
- Precision and recall are similarly important

However, F1 assumes that precision and recall are equally important. In many real applications, this assumption is not correct.

---

### F-beta score

The F-beta score allows you to give more importance to precision or recall.

Fβ=(1+β2)Precision×Recallβ2Precision+RecallF_\beta = (1+\beta^2)\frac{Precision \times Recall}{\beta^2 Precision + Recall}Fβ​=(1+β2)β2Precision+RecallPrecision×Recall​

- **F2-score** gives more importance to recall
- **F0.5-score** gives more importance to precision

For example, in cancer screening, F2 may be more appropriate because recall is more important.

---

### Accuracy

Accuracy=TP+TNTP+TN+FP+FNAccuracy = \frac{TP+TN}{TP+TN+FP+FN}Accuracy=TP+TN+FP+FNTP+TN​

Accuracy is useful when:

- Classes are relatively balanced
- False positives and false negatives have similar costs

Accuracy can be misleading in heavily imbalanced datasets.

---

### ROC-AUC

ROC-AUC evaluates how well the model separates positive and negative classes across all thresholds.

It is useful for:

- Comparing models
- Measuring general ranking ability
- Evaluating performance across many thresholds

However, with highly imbalanced datasets, ROC-AUC can sometimes look good even when positive-class performance is weak.

---

### PR-AUC

PR-AUC summarizes the precision-recall relationship across thresholds.

It is especially useful when:

- The positive class is rare
- The dataset is highly imbalanced
- Positive-case detection is the main concern

For fraud detection, disease detection, or anomaly detection, PR-AUC is often more informative than ROC-AUC.

---

## A practical threshold-selection process

A good workflow is:

1. Train the model on the training set.
2. Generate probabilities on the validation set.
3. Calculate precision and recall for many thresholds.
4. Define the business cost of false positives and false negatives.
5. Choose the threshold that satisfies the required objective.
6. Evaluate the final model once on the test set.
7. Monitor the threshold after deployment because data distributions may change.

For example, you may choose:

- The threshold with the highest F1-score
- The highest precision while recall remains above 90%
- The highest recall while precision remains above 70%
- The threshold with the lowest total business cost



recall Recall, **gerçekte pozitif olanların ne kadarını bulduğunu** gösterir.

	Recall=  TP / TP + FN

	Precission = TP / TP + FP

Precission = Precision, modelin pozitif dediği örneklerin ne kadarının gerçekten pozitif olduğunu gösterir.

## ROC and AUC Summary

A classification model usually produces a probability score. A **threshold** converts this score into a positive or negative prediction.

The **ROC curve** evaluates the model across many different thresholds. It plots:

- **True Positive Rate (TPR)** on the y-axis
    
- **False Positive Rate (FPR)** on the x-axis
    

### True Positive Rate

TPR is the same as recall:

[  
TPR = Recall = \frac{TP}{TP+FN}  
]

It measures the percentage of actual positive cases correctly detected by the model.

### False Positive Rate

[  
FPR = \frac{FP}{FP+TN}  
]

It measures the percentage of actual negative cases incorrectly classified as positive.

When the threshold is lowered, the model predicts more positive cases. This usually increases both TPR and FPR. When the threshold is increased, the model becomes more selective, so both TPR and FPR usually decrease.

The ideal point on the ROC curve is:

[  
(FPR,TPR)=(0,1)  
]

This means the model detects every positive case without producing any false positives.

## AUC

**AUC means Area Under the ROC Curve.**

It summarizes the model's ability to separate positive and negative classes across all thresholds.

AUC can also be interpreted as:

> The probability that the model gives a randomly selected positive example a higher score than a randomly selected negative example.

Typical interpretations:

- **AUC = 1.0:** Perfect separation
    
- **AUC = 0.5:** Random prediction
    
- **AUC < 0.5:** The model may be ranking the classes in the wrong direction
    

AUC does not directly select the best threshold. It mainly evaluates the model's overall ranking ability. The final threshold should be chosen according to the cost of false positives and false negatives.

For example:

- Use a lower threshold when missing a positive case is dangerous, such as disease detection.
    
- Use a higher threshold when false alarms are expensive, such as automatically blocking bank accounts.
    

For highly imbalanced datasets, the **Precision-Recall curve** may be more informative than the ROC curve because ROC-AUC can appear strong even when precision is low.

## Prediction Bias Summary

**Prediction bias** measures whether a model’s predictions are systematically higher or lower than the actual positive rate.

Prediction Bias=Average Prediction−Average Ground Truth\text{Prediction Bias} = \text{Average Prediction} - \text{Average Ground Truth}Prediction Bias=Average Prediction−Average Ground Truth

For binary classification:

- Positive label = `1`
- Negative label = `0`

The average ground truth is therefore the actual percentage of positive examples in the dataset.

### Interpretation

- **Prediction bias = 0:** The model predicts the overall positive rate correctly.
- **Positive prediction bias:** The model predicts too many positive cases.
- **Negative prediction bias:** The model predicts too few positive cases.

Example:

- Actual spam rate: `5%`
- Model’s average spam prediction: `20%`

0.20−0.05=0.150.20-0.05=0.150.20−0.05=0.15

The prediction bias is `+0.15`, meaning the model overestimates the positive class.

A prediction bias close to zero does **not** prove that the model is accurate. The model may predict the correct total number of positive cases while selecting the wrong individual examples.

Possible causes of prediction bias include:

- Biased or noisy training data
- Excessive regularization
- Bugs in the training pipeline
- Missing or weak features
- Differences between training data and real-world data

Prediction bias is mainly a quick diagnostic check. It should be used together with metrics such as precision, recall, accuracy, ROC-AUC, and calibration.