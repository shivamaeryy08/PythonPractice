import pandas

student_dict = {
    'student': ['shiv', 'sqwev', 'mew'],
    'score': [86.324, 546, .456]

}

student_df = pandas.DataFrame(student_dict)
# loop throiugh data frame

# for (key, value) in student_df.items():
#     print(value)

# loop through rowsa of a data_frame

for (index, row) in student_df.iterrows():
    print(row.student)
