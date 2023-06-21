import pandas as pd

#this function creates the multiplication table 1-n, where n is the input
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

while True:
    #tells user to input a number for the times table
    query = int(input("Choose any integer greater than 0: "))

    if query > 0:
        print(times_table(query))
        break

    #makes user try again and input a new number
    else:
        print(f"Try again. {query} is not greater than 0")