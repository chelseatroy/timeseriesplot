import pandas as pd
import numpy as np

def predict_salaries(employee_dataframe):
    print "dataframe: "
    print employee_dataframe

    df = employee_dataframe.dropna()

    ethnicities = df['ethnicity'].unique()
    print(ethnicities)
    df['ethnicities_num'] = map(lambda x: np.where(ethnicities==x)[0][0], df['ethnicity'])
    print df



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