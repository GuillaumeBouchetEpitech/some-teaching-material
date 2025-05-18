

#
#
# UTILITY FUNCTION

def _get_current_folder() -> str:
  # import os path namespace
  import os.path
  # get the absolute path from the current file we're in
  absolute_path = os.path.abspath(__file__)
  # get the folder of the absolute path
  return os.path.dirname(absolute_path)

# UTILITY FUNCTION
#
#



# to run in a terminal -> 'pip install pandas'
import pandas

csv_filepath = f"{_get_current_folder()}/02-pre-process-data.csv"


# df -> means "data frame"
df = pandas.read_csv(csv_filepath)


print()
print("#")
print("# RAW DATAFRAME")
print("#")
print()

print(df)





print()
print("#")
print("# RAW DATA")
print("#")
print()

# take all the rows, take all the columns except the last column one
X = df.iloc[:,:-1].values # will contains the values of the columns 'Country', 'Age', 'Salary'

# take all the rows, take only the last column
y = df.iloc[:, -1].values # will contains the values of the column 'Purchased'

print("X (inputs)")
print(X)
# [['France' 44.0 72000.0]
#  ['Spain' 27.0 48000.0]
#  ['Germany' 30.0 54000.0]
#  ['Spain' 38.0 61000.0]
#  ['Germany' 40.0 nan]  <------ missing value for the salary (nan -> 'Not A Number')
#  ['France' 35.0 58000.0]
#  ['Spain' nan 52000.0]  <------ missing value for the age (nan -> 'Not A Number')
#  ['France' 48.0 79000.0]
#  ['Germany' 50.0 83000.0]
#  ['France' 37.0 67000.0]]

print() # spacing

print("y (outputs)")
print(y)
# ['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes']

print() # spacing

#
#
#
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE

print()
print("#")
print("# FIXING INPUT DATA")
print("#")
print()

import numpy as np
from sklearn.impute import SimpleImputer

# replace all the NaN with the average (mean) value of the column
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3]) # all the rows, but only take the columns 'Age' + 'Salary'
X[:, 1:3] = imputer.transform(X[:, 1:3]) # all the rows, but only take the columns 'Age' + 'Salary'
# only the columns 'Age' + 'Salary' got modified


print("X (inputs)")
print(X)# [['France' 44.0 72000.0]
#  ['Spain' 27.0 48000.0]
#  ['Germany' 30.0 54000.0]
#  ['Spain' 38.0 61000.0]
#  ['Germany' 40.0 63777.77777777778]  <------ missing value for the salary is now fixed
#  ['France' 35.0 58000.0]
#  ['Spain' 38.77777777777778 52000.0]  <------ missing value for the age is now fixed
#  ['France' 48.0 79000.0]
#  ['Germany' 50.0 83000.0]
#  ['France' 37.0 67000.0]]

print() # spacing

print("y (outputs)")
print(y)
# ['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes']

print() # spacing

# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
#
#
#
