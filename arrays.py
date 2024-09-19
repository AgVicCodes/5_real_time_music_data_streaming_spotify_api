import numpy as np
import pandas as pd


data = {
    'id': [1, 2, 3],
    'values': [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
}

df = pd.DataFrame(data)
print(df)

df_exploded = df.explode('values')
print(df_exploded)

df['first_value'] = df['values'].apply(lambda x: x[0] if len(x) > 0 else None)
print(df)

df['sum_values'] = df['values'].apply(sum)
print(df)

df['numpy_array'] = df['values'].apply(np.array)
print(df)