import pandas as pd
import numpy as np
from sklearn import datasets, preprocessing, linear_model
import operator

def predict_salaries(employee_dataframe):
    df = employee_dataframe.dropna()

    #Pre-processing
    df['age_std'] = preprocessing.scale(df['age'])
    df['years_experience_std'] = preprocessing.scale(df['years_experience'])

    ethnicities = df['ethnicity'].unique()
    df['ethnicities_num'] = map(lambda x: np.where(ethnicities==x)[0][0], df['ethnicity'])
    df['ethnicities_num'] = preprocessing.scale(df['ethnicities_num'])

    genders = df['gender'].unique()
    df['genders_num'] = map(lambda x: np.where(genders == x)[0][0], df['gender'])
    df['genders_num'] = preprocessing.scale(df['genders_num'])

    roles = df['role'].unique()
    df['roles_num'] = map(lambda x: np.where(roles == x)[0][0], df['role'])
    df['roles_num'] = preprocessing.scale(df['roles_num'])

    train_y = df['salary'].values

    df = df.drop(['ethnicity', 'gender', 'role', 'salary'], axis=1)
    df = df[['ethnicities_num', 'genders_num', 'roles_num', 'age_std', 'years_experience_std']]

    train_x = df.values

    #Fitting the Model
    trainer = linear_model.Lasso(alpha = 0.1)
    trainer.fit(train_x, train_y)

    names = ['Ethnicity', 'Gender', 'Role', 'Age', "Years Experience"]

    coefficients = []
    total_weight = sum(abs(trainer.coef_))
    for coefficient in abs(trainer.coef_):
        coefficients.append(round((coefficient/total_weight)*100, 2))

    weights = dict(zip(names, coefficients))
    return list(reversed(sorted(weights.items(), key=operator.itemgetter(1))))

    #
    # print("Residual sum of squares: %.2f"
    #       % np.mean((trainer.predict(train_x) - train_y) ** 2))
    #
    # # Explained variance score: 1 is perfect prediction
    # print('Variance score: %.2f' % trainer.score(train_x, train_y))
