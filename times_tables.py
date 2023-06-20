import pandas as pd

times_table = []
for i in range(1, 10):
    row = [i * j for j in range(1, 10)]
    times_table.append(row)

df = pd.DataFrame(
    times_table,
    index = [str(i) for i in range(1,10)],
    columns = [str(i) for i in range(1, 10)]
    )

print(df)