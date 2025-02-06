

#
#
# UTILITY FUNCTION

def get_current_folder() -> str:
  # import os path namespace
  import os.path
  # get the absolute path from the current file we're in
  absolute_path = os.path.abspath(__file__)
  # get the folder of the absolute path
  return os.path.dirname(absolute_path)

# UTILITY FUNCTION
#
#




my_test_file_filepath = f"{get_current_folder()}/assets/test-file.txt"



print("") # spacing in the console
print("open file -> the unsafe way")

# open the file
my_file = open(my_test_file_filepath, "r")

# read the file line by line
for line in my_file:
  print(f' -> "{line}"')

# close the file
my_file.close() # important /!\






print("") # spacing in the console
print("open file -> the safe way")

# with syntax, auto-close the file at the end
with open(my_test_file_filepath, "r") as my_file:

  # read the file line by line
  for line in my_file:
    print(f' -> "{line}"')






print("") # spacing in the console
print("open file -> get all the lines")

# with syntax, auto-close the file at the end
with open(my_test_file_filepath, "r") as my_file:

  all_lines = my_file.readlines()

  # read the file line by line
  for line in all_lines:
    print(f' -> "{line}"')






print("") # spacing in the console
print("open file -> raw csv dataset")

my_dataset_filepath = f"{get_current_folder()}/assets/customers-100.csv"

# with syntax, auto-close the file at the end
with open(my_dataset_filepath, "r") as my_file:

  my_rows = []

  all_lines = my_file.readlines()

  for line in all_lines:
    # remove the unwanted return character
    line.strip('\n')
    # split by comma
    my_columns = line.split(',')
    # append it to the data
    my_rows.append(my_columns)

  # print(my_rows) # print a lot of things

  for index, value in enumerate(my_rows):
    # only print the first 5 rows
    if index > 5:
      break

    print(f"row #{index} -> {value}")











print("") # spacing in the console
print("write new file -> print")

my_logs_filepath = f"{get_current_folder()}/assets/my-logs.txt"

# with syntax, auto-close the file at the end
with open(my_logs_filepath, "w") as my_file:

  for index in range(1, 10):
    print(f"hello {index}", file=my_file) # <- notice the file=my_file








print("") # spacing in the console


