import pandas as pd

def create_dataframe():
    line = "*"*100

    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}

    print(line)

    # create Dataframe
    df = pd.DataFrame(data)
    print(f"Created DataFrame: \n{line}\n{df}\n")

    return df

def main():
    df = create_dataframe()

    quat1 = df['Salary'].quantile(0.25)  # 25th percentile
    quat3 = df['Salary'].quantile(0.75)  # 75th percentile
    IQR = quat3 - quat1

    lower_bound = quat1 - (1.5 * IQR)
    upper_bound = quat3 + (1.5 * IQR)

    outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
    print("Outliers:")
    print(outliers)

if __name__ == "__main__":
    main()


"""
Q1: Detect outliers in the 'Salary' column using the IQR method. data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]} 
"""