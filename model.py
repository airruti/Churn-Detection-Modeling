from prometheus_client import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score, classification_report, accuracy_score, confusion_matrix
import pandas as pd
from imblearn.over_sampling import SMOTE

def logisticReg(file):
    data = pd.read_csv(file)
    y = data["Churn"]
    x = data.drop(columns=["Churn"])

    oversample = SMOTE()
    x, y = oversample.fit_resample(x, y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.9)

    model = LogisticRegression()
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    model.fit(x_train, y_train)

    y_prediction = model.predict(x_test)
    print(y_prediction)
    print(classification_report(y_test, y_prediction, digits=6))
    report = pd.DataFrame(classification_report(y_test, y_prediction, digits=6, output_dict=True)).transpose()
    print(confusion_matrix(y_test, y_prediction))
    return report