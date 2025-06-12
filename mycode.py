import pandas as pd
import os

# create a sample  DataFrame
data = {
    'Name':['Gaurav','Tejas','Pratik'],
    'Age':[25,24,26],
    'City':['New York','LA','Mumbai']
}

df = pd.DataFrame(data)

# add new rows to df for v2
new_row_loc = {'Name':'GF1','Age':20,'City':'City1'}
df.loc[len(df.index)] = new_row_loc



data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

# define the file path
file_path = os.path.join(data_dir,"sample_data.csv")

# save the dataframe to csv
df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")