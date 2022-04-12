from prometheus_client import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import roc_curve, roc_auc_score, classification_report, accuracy_score, confusion_matrix
import pandas as pd
from imblearn.over_sampling import SMOTE

def k_fold(file):
    data = pd.read_csv(file)
    drops = ["Churn", "Kaseya Market Segment_- None -", "Kaseya Market Segment_Channel", "Kaseya Market Segment_Education",
     "Kaseya Market Segment_End User", "Kaseya Market Segment_Financial Services", "Kaseya Market Segment_General Business",
      "Kaseya Market Segment_Government", "Kaseya Market Segment_Healthcare", "Kaseya Market Segment_Hospitality",
       "Kaseya Market Segment_Retail", "Kaseya Market Segment_Software Vendor", "Account Currency_AU",
        "Account Currency_EU", "Account Currency_SA"]
    y = data["Churn"]
    x = data.drop(columns=drops)
    scores = []

    oversample = SMOTE()
    x, y = oversample.fit_resample(x, y)

    kf = StratifiedKFold(n_splits =5, shuffle=True, random_state=45)

    i = 1
    for train_index, test_index in kf.split(x, y):
        print("{} of KFold {}".format(i, kf.n_splits))
        x_train, x_test = x.loc[train_index], x.loc[test_index]
        y_train, y_test = y.loc[train_index], y.loc[test_index]

        model = LogisticRegression(max_iter=1000)
        print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
        model.fit(x_train, y_train)

        y_prediction = model.predict(x_test)
        print(y_prediction)
        print()
        score = roc_auc_score(y_test, y_prediction)
        scores.append(score)
        # print('ROC AUC score: ', score)
        # print()
        #print(classification_report(y_test, y_prediction, digits=6))
        report = pd.DataFrame(classification_report(y_test, y_prediction, digits=6, output_dict=True)).transpose()
        print(confusion_matrix(y_test, y_prediction))
        print()
        i += 1
    avg = sum(scores)/len(scores)

    print('Average ROC AUC Score: ', avg)

    return report

def logistic_reg(file):
    data = pd.read_csv(file)
    y = data["Churn"]
    x = data.drop(columns=["Churn"])

    oversample = SMOTE()
    x, y = oversample.fit_resample(x, y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.8)

    model = LogisticRegression()
    print('train and test shapes:')
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    model.fit(x_train, y_train)

    y_prediction = model.predict(x_test)
    print('y_prediction:')
    print(y_prediction)
    print()
    # score = roc_auc_score(y_test, y_prediction)
    # print('ROC AUC score: ', score)
    print(classification_report(y_test, y_prediction, digits=6))
    report = pd.DataFrame(classification_report(y_test, y_prediction, digits=6, output_dict=True)).transpose()
    print(confusion_matrix(y_test, y_prediction))

    return report