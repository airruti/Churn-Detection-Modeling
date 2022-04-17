from asyncio.windows_events import NULL
from prometheus_client import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import precision_score, roc_curve, roc_auc_score, classification_report, accuracy_score, confusion_matrix
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

def k_fold(file):
    data = pd.read_csv(file)
    drops = ["Churn", "Kaseya Market Segment_- None -",
     "Kaseya Market Segment_End User", "Kaseya Market Segment_Financial Services", "Kaseya Market Segment_General Business",
      "Kaseya Market Segment_Government", "Kaseya Market Segment_Healthcare", "Kaseya Market Segment_Hospitality",
       "Kaseya Market Segment_Retail", "Kaseya Market Segment_Software Vendor", "Account Currency_AU",
        "Account Currency_SA", "reputation_to_date", "Connect 2019"]
    y = data["Churn"]
    x = data.drop(columns=drops)
    scores = []

    oversample = SMOTE()
    x, y = oversample.fit_resample(x, y)

    kf = StratifiedKFold(n_splits =5, shuffle=True, random_state=45)
    conf_matrix = NULL
    i = 1
    for train_index, test_index in kf.split(x, y):
        print("{} of KFold {}".format(i, kf.n_splits))
        x_train, x_test = x.loc[train_index], x.loc[test_index]
        y_train, y_test = y.loc[train_index], y.loc[test_index]

        model = LogisticRegression(max_iter=1000)
        print("Shape: ", x_train.shape, x_test.shape, y_train.shape, y_test.shape)
        model.fit(x_train, y_train)

        y_prediction = model.predict(x_test)
        print("Prediction: ", y_prediction)
        score = roc_auc_score(y_test, y_prediction)
        scores.append(score)
        # print('ROC AUC score: ', score)
        # print()
        #print(classification_report(y_test, y_prediction, digits=6))
        report = pd.DataFrame(classification_report(y_test, y_prediction, digits=6, output_dict=True)).transpose()
        conf_matrix = confusion_matrix(y_test, y_prediction)
        print(conf_matrix)
        print()
        i += 1
    avg = sum(scores)/len(scores)
    print(classification_report(y_test, y_prediction, digits=6))
    print('Average ROC AUC Score: ', avg)
    print("Precision: " ,precision_score(y_true=y_test, y_pred=y_prediction, average="binary"))

    return [report, conf_matrix]


# def feature_imp(file):
#     data = pd.read_csv("C:/Users/shuss/Desktop/combined.csv")
#     drops = ["Churn", "Kaseya Market Segment_- None -",
#         "Kaseya Market Segment_End User", "Kaseya Market Segment_Financial Services", "Kaseya Market Segment_General Business",
#         "Kaseya Market Segment_Government", "Kaseya Market Segment_Healthcare", "Kaseya Market Segment_Hospitality",
#         "Kaseya Market Segment_Retail", "Kaseya Market Segment_Software Vendor", "Account Currency_AU",
#         "Account Currency_SA", "reputation_to_date", "Connect 2019"]
#     y = data["Churn"]
#     x = data.drop(columns=drops)
#     model = ExtraTreesClassifier()
#     model.fit(x,y)
#     importances = pd.Series(model.feature_importances_,index =x.columns)
#     return importances



# def logistic_reg(file):
#     data = pd.read_csv(file)
#     y = data["Churn"]
#     x = data.drop(columns=["Churn"])

#     oversample = SMOTE()
#     x, y = oversample.fit_resample(x, y)

#     x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.8)

#     model = LogisticRegression()
#     print('train and test shapes:')
#     print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
#     model.fit(x_train, y_train)

#     y_prediction = model.predict(x_test)
#     print('y_prediction:')
#     print(y_prediction)
#     print()
#     # score = roc_auc_score(y_test, y_prediction)
#     # print('ROC AUC score: ', score)
#     print(classification_report(y_test, y_prediction, digits=6))
#     report = pd.DataFrame(classification_report(y_test, y_prediction, digits=6, output_dict=True)).transpose()
#     confusion_matrix = confusion_matrix(y_test, y_prediction)
#     print(confusion_matrix)
#     return report



