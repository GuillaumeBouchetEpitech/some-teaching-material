

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

#
#
#
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE

print()
print("#")
print("# ENCODING OUTPUT DATA")
print("#")
print()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print("X (inputs)")
print(X)
# [[1.0 0.0 0.0 44.0 72000.0]
#  [0.0 0.0 1.0 27.0 48000.0]
#  [0.0 1.0 0.0 30.0 54000.0]
#  [0.0 0.0 1.0 38.0 61000.0]
#  [0.0 1.0 0.0 40.0 nan]
#  [1.0 0.0 0.0 35.0 58000.0]
#  [0.0 0.0 1.0 nan 52000.0]
#  [1.0 0.0 0.0 48.0 79000.0]
#  [0.0 1.0 0.0 50.0 83000.0]
#  [1.0 0.0 0.0 37.0 67000.0]]

print() # spacing

# Purchase column now encoded into 1 columns
print("y (outputs)")
print(y)
# [0 1 0 0 1 1 0 1 0 1]

print() # spacing

# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
# NEW STUFF HERE -  NEW STUFF HERE -  NEW STUFF HERE
#
#
#
