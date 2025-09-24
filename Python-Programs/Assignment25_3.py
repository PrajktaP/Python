import pandas as pd
from sklearn.preprocessing import LabelEncoder

def create_dataframe():
    line = "*"*100

    data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']} 

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)
    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def apply_label_encoding(df, column):
    encoder = LabelEncoder()

    df[f"encoded_{column.lower()}"] = encoder.fit_transform(df['City'])

def main():
    line = "*"*100

    df = create_dataframe()

    print(line)
    print(f"Before applying encoding: \n{line}\n{df}\n")

    apply_label_encoding(df, 'City')

    print(line)
    print(f"After applying encoding: \n{line}\n{df}\n")

if __name__ == "__main__":
    main()


"""
Q3: Apply Label Encoding to a 'City' column. data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']} 
"""