from firebase import firebase
import datetime
import time
import serial

# Create the connection to our Firebase database - don't forget to change the URL!
FBConn = firebase.FirebaseApplication('https://vehicle-484ce.firebaseio.com/', None)

while True:
    # Ask the user to input a temperature
    temperature = int(input("What is the temperature? "))

    # Create a dictionary to store the data before sending to the database
    data_to_upload = {
        time.strftime("%Y-%m-%d %H:%M:%S"): temperature
    }

    # Post the data to the appropriate folder/branch within your database
    result = FBConn.post('/MyTestData/', data_to_upload)

    # Print the returned unique identifier
    print(result)

# Close the serial connection
ser.close()