# Churn Detection Modeling -- Web App <Created Spring 2022>

Authors: Jose Iturria, Jairo Adarmes Arias, Eddy Garcia, Josue Daniel Prendes, Marcus Bedeau, Cecilia Gervasoni Latorre, Syed Hussain, Rey Jairus Marasigan, Katerin Marinas Delgado, Ernesto Vilches Martinez

Product Owner: Lina Sokol

---
### Project Structure
The following tree structure will be useful to visualize how the project is structured:

```

├── Churn-Detection-Modeling

│   └── Model.py
│   └── displayData.py
│   └── data_cleaning.py
│   └── CSV Files
│   └── Icon

```

All the functionality lies in the original folder, as each .py files contains the code for a particular unit.

Model.py holds the k-fold logistic regression with smote function.
displayData.py holds all the streamlit UI code
data_cleaning.py is where we perform the data filtering on thhe original csv files. 

Having everything in one folder will allow us to easily import modules across the entire project, as we see when we use the model in our UI.

To use this churn model, you muist install the following dependencies: 

```

pip3 install pandas
pip3 install streamlit
pip3 install sklearn
pip3 install altair
pip3 install seaborn
pip3 install matplotlib
pip3 install statsmodels
pip3 install imblearn

```

Afterwards, clone this github repository using

```

git clone https://github.com/airruti/Churn-Detection-Modeling.git (note, this is a PRIVATE repo)

```

Once downloaded, simply navigate to the project directory on your terminal, and type:

```

streamlit run displayData.py

```

This will open a new webpage on the local machine, and the application will run!
