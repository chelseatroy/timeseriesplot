import pandas as pd
import numpy as np
from sklearn import datasets, preprocessing, linear_model

def predict_salaries(employee_dataframe):
    print "dataframe: "
    print employee_dataframe

    df = employee_dataframe.dropna()

    df['age_std'] = preprocessing.scale(df['age'])
    df['years_experience_std'] = preprocessing.scale(df['years_experience'])

    ethnicities = df['ethnicity'].unique()
    df['ethnicities_num'] = map(lambda x: np.where(ethnicities==x)[0][0], df['ethnicity'])

    genders = df['gender'].unique()
    df['genders_num'] = map(lambda x: np.where(genders == x)[0][0], df['gender'])

    roles = df['role'].unique()
    df['roles_num'] = map(lambda x: np.where(roles == x)[0][0], df['role'])

    train_y = df['salary'].values

    df = df.drop(['ethnicity', 'gender', 'role', 'salary'], axis=1)
    df = df[['ethnicities_num', 'genders_num', 'roles_num', 'age_std', 'years_experience_std']]

    print df

    train_x = df.values

    trainer = linear_model.Lasso(alpha = 0.1)
    trainer.fit(train_x, train_y)

    print('Coefficients: \n', trainer.coef_)

    print("Residual sum of squares: %.2f"
          % np.mean((trainer.predict(train_x) - train_y) ** 2))

    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % trainer.score(train_x, train_y))
