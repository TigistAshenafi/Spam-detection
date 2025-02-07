Machine Learning project on
spam detection

 What is Spam?
Spam refers to unsolicited, irrelevant, or unwanted messages sent in bulk over digital communication platforms such as email, SMS, social media, and other online messaging services.
 
 Problem Definition:
Objective:
The goal of this project is to build a machine learning model capable of detecting spam messages in SMS data. The task involves classifying text messages as either "spam" or "ham" (non-spam). This is a binary supervised classification problem.

Significance: 
Spam detection is crucial for reducing cyber security risks, improving communication efficiency, and enhancing user experiences on email and messaging platforms.

Challenges:
-Handling imbalanced datasets (more ham than spam).
-Dealing with variations in spam patterns (e.g., phishing, promotional messages).
-Effectively processing textual data using natural language processing (NLP) techniques.
-Generalization issues: Model might not handle unseen patterns well.
 
 Data Acquisition
-Dataset Description:
The dataset used for this project contains SMS messages labeled as spam or ham.
Kaggle - Spam Text Message Classification
License and Terms: Assumed to be permissible for educational purposes.
 
-Data Structure:
Label: Categorical target variable (spam, ham).
Message: Text content of the SMS message.

 Exploratory Data Analysis (EDA)
Analyze class distributions (spam vs. non-spam).
Identify missing values, outliers, and patterns.
Visualizations: Bar charts for term frequency, word clouds, and correlation heatmaps.
 
 Data Preprocessing
-Text Processing:
Tokenization, removing stop words, and stemming.
-Feature Engineering:
I used the techniques TF-IDF Vectorizer to convert text data into numerical features.
-Data Transformation:
Vectorize text using TF-IDF or CountVectorizer.
Handle class imbalance with techniques like SMOTE if necessary.
-Train-Test Split:
Splitting the testing and training sets.

 Model Implementation & training
I choose the Random Forest classifier and the accuracy = 0.9777.
Split the dataset into training and testing sets.
Train the model, using hyperparameter tuning (grid search or randomized search) for optimal performance.

 Model Deployment 
I deploy the model using Flask on pythonanywhere wepsite.
https://tigist.pythonanywhere.com/.