import pandas as pd
import numpy as np
from sklearn import datasets, linear_model

def predict_salaries(employee_dataframe):
    print "dataframe: "
    print employee_dataframe

    df = employee_dataframe.dropna()

    ethnicities = df['ethnicity'].unique()
    print(ethnicities)
    df['ethnicities_num'] = map(lambda x: np.where(ethnicities==x)[0][0], df['ethnicity'])

    genders = df['gender'].unique()
    print(genders)
    df['genders_num'] = map(lambda x: np.where(genders == x)[0][0], df['gender'])

    roles = df['role'].unique()
    print(roles)
    df['roles_num'] = map(lambda x: np.where(roles == x)[0][0], df['role'])

    results = df['salary'].values

    df = df.drop(['ethnicity', 'gender', 'role', 'salary'], axis=1)

    print df

    train_data = df.values

    print(train_data)

    trainer = linear_model.LinearRegression()
    trainer.fit(train_data, results)

    print('Coefficients: \n', trainer.coef_)

    print("Residual sum of squares: %.2f"
          % np.mean((trainer.predict(train_data) - results) ** 2))

    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % trainer.score(train_data, results))
