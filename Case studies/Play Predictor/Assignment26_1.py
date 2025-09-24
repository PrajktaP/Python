import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def split_data(x, y, test_size):
    line = "*"*100

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size, random_state = 42)

    print(line)
    print(x_train.shape)
    print(x_test.shape)
    print(y_train.shape)
    print(y_test.shape)
    print(line)

    return x_train, x_test, y_train, y_test

def label_encode(df):
    # label encoding and transforming columns
    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df["Whether"] = le_weather.fit_transform(df["Whether"])
    df["Temperature"] = le_temp.fit_transform(df["Temperature"])
    df["Play"] = le_play.fit_transform(df["Play"])

    return le_weather, le_temp, le_play

def display_dimensions(x, y):
    print(x.shape)
    print(y.shape)

def find_best_k(x_train, y_train, x_test, y_test):
    line = "*"*100
    accuracy_scores = []
    k_range = range(1, 16)

    best_k = 0
    best_accuracy = 0

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors = k)

        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

        print(f"Accuracy when k = {k} is: {accuracy}")

        accuracy_scores.append(accuracy)

    print(line)
    print(accuracy_scores)
    print(line)

    print(f"Best value of k: {best_k}")
    print(f"Best accuracy score: {best_accuracy}")

def CheckAccuracy(x, y, test_size=0.5):
    x_train, x_test, y_train, y_test = split_data(x, y, test_size)
    find_best_k(x_train, y_train, x_test, y_test)

def play_predictor_knn(datafilepath):
    line = "*"*100

    df = pd.read_csv(datafilepath)

    print(f"PlayPredictor Dataset: \n{df.head()}\n\n{line}\n")
    print(f"Dimensions of Dataset: \n{df.shape}\n\n{line}\n")

    #################################################################################
    # Clean, Prepare and Manipulate data
    # As we want to use the above data into machine learning application we have prepare
    # that in the format which is accepted by the algorithms.
    # As our dataset contains two features as Wether and Temperature. We have to replace
    # each string field into numeric constants by using LabelEncoder from processing module
    # of sklearn.
    #################################################################################
    df.drop(columns = ['Unnamed: 0'], inplace=True)

    # Update: get encoders and transform columns
    le_weather, le_temp, le_play = label_encode(df)
    print(f"PlayPredictor Dataset after label encoding: \n{df.head()}\n\n{line}\n")

    x = df[["Whether", "Temperature"]]
    y = df["Play"]
    display_dimensions(x, y)

    #################################################################################
    # Step 3:
    # Train Data
    # Now we want to train our data for that we have to select the Machine learning algorithm.
    # For that we select K Nearest Neighbour algorithm.
    # use fit method for training purpose. For training use whole dataset.
    #################################################################################
    model = KNeighborsClassifier(n_neighbors = 3)
    model.fit(x, y)

    print(f"Model trained with KNeighborsClassifier with n_neighbors=3\n\n{line}\n")

    #################################################################################
    # Step 4:
    # Test Data
    # After successful training now we can test our trained data by passing some value of
    # wether and temperature.
    # As we are using KNN algorithm use value of K as 3.
    # After providing the values check the result and display on screen.
    # Result may be Yes or No.
    #################################################################################
    sample_values = pd.DataFrame({
        "Whether": ["Sunny"],
        "Temperature": ["Cool"]
    })
    # Transform sample values using fitted encoders
    sample_values["Whether"] = le_weather.transform(sample_values["Whether"])
    sample_values["Temperature"] = le_temp.transform(sample_values["Temperature"])
    # predict test data
    prediction = model.predict(sample_values)
    prediction_label = le_play.inverse_transform(prediction)

    print(f"Result for {sample_values[['Whether', 'Temperature']].values}: {prediction_label[0]}")
    # ----------- test the trained and tested model using sample data end -----------

    #################################################################################
    # Step 5:
    # Calculate Accuracy
    # Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
    # For calculating the accuracy divide the dataset into two equal parts as Training data and
    # Testing data.
    # Calculate Accuracy by changing value of K.
    #################################################################################
    print("Splitting dataset into train and test sets")
    CheckAccuracy(x, y, 0.5)

def main():
    play_predictor_knn("PlayPredictor.csv")

if __name__ == "__main__":
    main()