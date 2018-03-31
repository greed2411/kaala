from sklearn.externals import joblib
import numpy as np

classifier = joblib.load('kaala-model.pkl')

def result(readings):
    return classifier.predict_proba(np.asarray(readings).reshape(1, -1)).tolist()[0]