import pandas as pd
import numpy as np

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

    df = df.drop(['ethnicity', 'gender', 'role'], axis=1)

    print df

    train_data = df.values

    print(train_data)

    # print employees
    # for employee in employees:
    #     print employee.age
    #     print employee.ethnicity
    #     print employee.gender
    #     print "the end"


# ethnicity
# gender
# age
# years_experience
# role
# salary