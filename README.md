# Data Modeling In Machine Learning

**Data modeling in machine learning** is the process of **creating machine learning models capable of** predicting labels from features, tuning them for the business need, and validating it on holdout data. The output from data modeling is a trained model that can be used for **making predictions on new data points**.

![DSN](images/dsn_logo.png)

This repository houses the course materials from the classes I'm undertaking with the **DSN-UNIILORIN cohort 2** on data modeling.

Just for a quick overview of what's entailed in the course materials. 

In the course materials ([big_mart_checklist.ipynb](big_mart_checklist.ipynb) and [loan_prediction_checklist.ipynb](loan_prediction_checklist.ipynb)). We explore the checklist by [Aurélien Géron](https://www.oreilly.com/people/aurelien-geron/) in his book [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) to model data.

The first task we'll be undertaking is the regression task with the [Big Mart Sales Dataset](data/big_mart_sales_prediction.csv) to understand how we can model data in regression tasks. We'll then proceed to understand data modeling with classification tasks using the [Loan Prediction Dataset](data/loan_prediction.csv).

## The Data Modeling Checklist

### ➡ Prepare the Data

**Notes:**

- Work on copies of the data (keep the original dataset intact).
- Write functions for all data transformations you apply, for five reasons:
    - So you can easily prepare the data the next time you get a fresh dataset
    - So you can apply these transformations in future projects
    - To clean and prepare the test set
    - To clean and prepare new data instances once your solution is live
    - To make it easy to treat your preparation choices as hyperparameters

1. **Data cleaning**:
    - Fix or remove outliers (optional).
    - Fill in missing values (e.g., with zero, mean, median…) or drop their rows (or columns).
    
2. **Feature selection (optional)**:
    - Drop the attributes that provide no useful information for the task.
    
3. **Feature engineering, where appropriate**:
    - Discretize continuous features.
    - Decompose features (e.g., categorical, date/time, etc.).
    - Add promising transformations of features (e.g., log(x), sqrt(x), x2, etc.).
    - Aggregate features into promising new features.

4. **Feature scaling**:
    - Standardize or normalize features.

### ➡ Shortlist Promising Models

**Notes:**

- If the data is huge, you may want to sample smaller training sets so you can train many different models in a reasonable time (be aware that this penalizes complex models such as large neural nets or Random Forests).
- Once again, try to automate these steps as much as possible.

1. Train many quick-and-dirty models from different categories (e.g., linear, naive Bayes, SVM, Random Forest, neural net, etc.) using standard parameters.
2. Measure and compare their performance.
    - For each model, use N -fold cross-validation and compute the mean and standard deviation of the performance measure on the N folds.
3. Analyze the most significant variables for each algorithm.
4. Analyze the types of errors the models make.
    - What data would a human have used to avoid these errors?
5. Perform a quick round of feature selection and engineering.
6. Perform one or two more quick iterations of the five previous steps.
7. Shortlist the top three to five most promising models, preferring models that make different types of errors.

### ➡ Fine-Tune the System

**Notes:**

- You will want to use as much data as possible for this step, especially as you move toward the end of fine-tuning.
- As always, automate what you can.

1. Fine-tune the hyperparameters using cross-validation:
    - Treat your data transformation choices as hyperparameters, especially when you are not sure about them (e.g., if you’re not sure whether to replace missing values with zeros or with the median value, or to just drop the rows).
    - Unless there are very few hyperparameter values to explore, prefer random search over grid search. If training is very long, you may prefer a Bayesian optimization approach (e.g., using Gaussian process priors, as described by Jasper Snoek et al. ).
2. Try Ensemble methods. Combining your best models will often produce better performance than running them individually.
3. Once you are confident about your final model, measure its performance on the test set to estimate the generalization error.

### ➡ Present Your Solution

1. Document what you have done.
2. Create a nice presentation.
    - Make sure you highlight the big picture first.
3. Explain why your solution achieves the business objective.
4. Don’t forget to present interesting points you noticed along the way.
    - Describe what worked and what did not.
    - List your assumptions and your system’s limitations.
5. Ensure your key findings are communicated through beautiful visualizations or easy-to-remember statements (e.g., “the median income is the number-one predictor of housing prices”).

## Assignments and Tasks

There are multiple assignments and tasks present in the tutorial notebook. The emojis represented in black quotes stand for different things entirely.

**⁉** stand for research or reason finding. At any point you encounter this emoji, you're expected to answer the question and get the intuition behind it.

**🛠** stands for activities. The activities described here are all to be compiled and submitted to the class telegram page.

**📖** stands for resources. You're expected to follow up on every resource provided in this notebook to aid you in better understanding the task. I would be joking to tell you one single notebook would help you grasp the entirety of data modeling in machine learning.

---

Follow **Olalekan @**:

- [LinkedIn](https://www.linkedin.com/in/olalekan-ganiyu-747855199/)
- [Twitter](https://twitter.com/GM_Olalekan)
- [Medium](https://gmolalekan.medium.com/)
- [Kaggle](https://www.kaggle.com/ganiyuolalekan)
- [Github](https://github.com/ganiyuolalekan)
