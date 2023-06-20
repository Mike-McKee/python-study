# import pandas as pd

# times_table = []
# for i in range(1, 10):
#     row = [i * j for j in range(1, 10)]
#     times_table.append(row)

# df = pd.DataFrame(
#     times_table,
#     index = [str(i) for i in range(1,10)],
#     columns = [str(i) for i in range(1, 10)]
#     )

# print(df)

import pandas as pd

def times_table(num_of_rows):

    data = []
    
    for i in range(1,num_of_rows + 1):
        row = [i * j for j in range(1, num_of_rows + 1)]
        data.append(row)
    
    df = pd.DataFrame(
        data,
        index = [str(i) for i in range(1, num_of_rows + 1)],
        columns = [str(i) for i in range(1, num_of_rows + 1)]
    )

    return df

query = int(input("Choose any integer greater than 0: "))

# have to fix this and add a while statement so that the sequence repeats until a valid number is entered
# while status == True:
#     status = True

#     if query > 0:
#         print(times_table(query))
#         status = False
    
#     else:
#         print(f"Try again. {query}")

print(times_table(query))