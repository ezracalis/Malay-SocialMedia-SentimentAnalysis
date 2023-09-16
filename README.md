# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone Project - Malay Language Social Media Sentiment Analysis
---
### Introduction & Problem Statement

Sentiment analysis is a subfield of Natural Language Processing (NLP) that focuses on the detection of one's sentiment in text data. It is one of the most widely-used applications of NLP, and is important in a variety of areas including social media content, customer reviews, speech conversations, and news.

Sentiment analysis allows organisations and individuals to understand views on their actions, and themselves. For organisations and individuals who want to track public opinion on them (ie. reputation management), sentiment analysis is vital to help them filter through enormous amounts of unstructured information.

While research and development into sentiment analysis has been done quite comprehensively on major languages such as the English and Chinese languages, it has been really scarce for less popular languages such as Malay. As of today, there is only one well known Natural-Language-Toolkit library for Bahasa Melayu, which is [Malaya](https://malaya.readthedocs.io/en/stable/). In the library, there are a number of modules that can be used, including sentiment analysis.

However, the sentiment analysis model used in Malaya appears to be lexicon-based. While lexicon-based models are common (eg. VADER) and interpretable, it is limited when it comes to handling contextual understanding, as well as vocabulary gaps. For the latter, it is important that the list of words in the lexicon is varied and robust in order to detect the right sentiments in varied types of sentences.

However, diving into the [sentiment-specific lexicon](https://github.com/huseinzol05/malaysian-dataset/blob/master/lexicon/sentiment.json), it appears to be quite limited to formal Malay words, and is unlikely to be able to detect sentiments in texts which include slang or short-forms, which is very common in Malay social media.

Based on this, the problem statement for my capstone is:

**<center>Can we create an best-in-class classification model to identify sentiments in Malay social media comments?</center>**

The ideal outcome / goal is to create an sentiment analysis model for Bahasa Melayu that is reasonably accurate for social media comments. In this project, I will compare the accuracy of the Malaya model in detecting sentiments, and compare it to the accuracy of ChatGPT 3.5, which is an existing Large Language Model that is trained on Bahasa Melayu (albeit less so than on English). Whichever model performs better, will be used as a baseline to train our model on.

The primary audience will be individuals and organisations that wish to understand views of Malay-speakers on social media. These individuals and organisations will be primarily based in the Malay archipelago, which includes countries such as Malaysia, Indonesia, Singapore and Brunei, and has a combined population of close to 400 million people.

---

### Methodology

Our methodology is as follows:

1. Cleaning of Data
    1. Handling of null values
    2. Handling duplicated values
    3. Handling data types
    4. Handling of HTML-encoded entities
2. Feature Engineering
3. Establishing Ground Truth
    1. Labeling of Sample using Malaya
    2. Labeling of Sample using ChatGPT
    3. Manual Labeling of Sample
    4. Choosing of best labeling method
    5. Labling all comments
4. Exploratory Data Analysis 
5. Pre-Modeling
    1. Sastrawi Stemming
    2. Malay stop-word removal
    3. Train-test-split
    4. Creating Evaluation Functions
6. Modeling
    1. Model 1: TF-IDF vectorization + Multinomial Naive Bayes model
    2. Model 2: RandomOverSampler + TF-IDF vectorizer + Multinomial Naive Bayes model
    3. Model 3: SMOTE + TF-IDF vectorizer + Multinomial Naive Bayes model
    4. Model 4: Undersampling + TF-IDF vectorizer + Multinomial Naive Bayes model
    5. Model 5: RandomOverSampler + TF-IDF vectorizer + Random Forest model
    6. Model 6: RandomOverSampler + TF-IDF vectorizer + Logistic Regression model
    7. Model 7: RandomOverSampler + TF-IDF vectorizer + Support Vector Machine model (linear)
    8. Model 8: RandomOverSampler + TF-IDF vectorizer + AdaBoost Classifier Model
7. Conclusion and Future Works
8. Model Deployment
    1. Creating Flask API
    2. Creating Dockerfile
    3. Deploy to Google Cloud
    4. Host on Streamlit
---

### Model Evaluation

Based on all the models that we ran, we can say that most of the models performed quite similarly. However, in terms of scores, they mostly hover around F1 scores in the 60s to low 70s. The results are as follows:

| # | Model Type                      | Addressed Class Imbalance? | F1-Score                      | Review                          | Choose model? |
|---|---------------------------------|----------------------------|-------------------------------|---------------------------------|---------------|
| 1 | Multinomial Naive Bayes         | No                         | Train: 0.7282<br>Test: 0.6957 | Mildly decent.                  |               |
| 2 | Multinomial Naive Bayes         | ROS                        | Train: 0.7483<br>Test: 0.7005 | Improved on Model 1             |      ✓        |
| 3 | Multinomial Naive Bayes         | SMOTE                      | Train: 0.7442<br>Test: 0.6814 | Poorer test scores than Model 1 |               |
| 4 | Logistic Regression             | Undersampling              | Train: 0.6887<br>Test: 0.6308 | Poor scores.                    |               |
| 5 | Random Forest                   | ROS                        | Train: 0.7221<br>Test: 0.6228 | Poor scores and overfitted.     |               |
| 6 | Logistic Regression             | ROS                        | Train: 0.7208<br>Test: 0.6930 | Close to Multinomial NB         |               |
| 7 | Support Vector Machine (Linear) | ROS                        | Train: 0.7399<br>Test: 0.6927 | Close to Multinomial NB         |               |
| 8 | Adaboost Classifier             | ROS                        | Train: 0.9434<br>Test: 0.6735 | Very overfit                    |               |          

Overall, I would say that the Multinomial Naive Bayes (with RandomOverSampler) performed the best, although it is very close to the other scores. The main reason for choosing this model is that it has the best test scores, while not being overfitted.

---

### Recommendations and Next Steps

There are a few issues with this project that I feel could be addressed in order to create a better Sentiment Analysis classifier. Due to the challenging nature of Malay social media text, it was a challenge to improve the scores, even when inputing more comments. Given more time, I would:

1. Dive deeper to understand the intricacies of Malay social media text
    1. This would allow me to create a better stopword collection that is meant for Malay social media text.
    2. Similarly, understanding it deeper will allow us to build a lexicon-based sentiment analysis model as well that works well for social media text.
1. After which, get more data
    1. This would hopefully address the class-imbalance issue.
    2. Also, it would be beneficial to expand the project to having more classes (eg. emotion analysis); however, it will require much more data for each class.