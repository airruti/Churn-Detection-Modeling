from asyncio.windows_events import NULL
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score, classification_report, accuracy_score, confusion_matrix
import pandas as pd

class report:

    def __init__(self, report = NULL):
        self._report = report

    def get_report(self):
        return self._report

    def set_report(self, report):
        self._report = report

classReport = report()       


def logisticReg(file):
    data = pd.read_csv(file)
    y = data["Churn"]
    x = data.drop(columns="Churn")
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.7)
    model = LogisticRegression()
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    model.fit(x_train, y_train)
    y_prediction = model.predict(x_test)
    print(y_prediction)
    print(classification_report(y_test, y_prediction, digits=6))
    report = pd.DataFrame(classification_report(y_test, y_prediction, digits=6, output_dict=True)).transpose()
    classReport.set_report(report)
    print(confusion_matrix(y_test, y_prediction))
    df3 = pd.DataFrame(confusion_matrix(y_test, y_prediction))
    return df3