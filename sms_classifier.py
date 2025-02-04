import joblib

model = joblib.load("RandomForest.joblib")  
tfidf = joblib.load("tfidf_vectorizer.joblib")

def classify_sms(sms_message):
    sms_vectorized = tfidf.transform([sms_message]) 
    prediction = model.predict(sms_vectorized)[0]
    return "ham" if prediction == 0 else "spam"


