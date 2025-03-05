# Doodle Classifier with CNN and Flask

This repository contains a Convolutional Neural Network (CNN) based doodle classifier, trained to recognize 10 different doodle classes: star, shoe, piano, house, popsicle, tshirt, umbrella, duck, airplane, and windmill. The model is deployed as a web application using Flask, allowing users to upload their doodles and receive predictions.

## Project Structure

doodle-classifier/

├── app.py          # Flask application

├── keras.h5        # Saved model weights and architecture

├── templates/      # HTML templates for the web application

│   └── index.html

├── static/         # Static files (CSS, JavaScript, images)

│   └── style.css

│   └── sketch.js

│   └── jquery-1.3.2.min.js

└── README.md

## Model Training
The CNN model was trained using a dataset of doodles. The trained model weights are saved in models/doodle_classifier.h5.

## Running the Application
To run the Flask application, execute the following command:

run flask

The application will start running on http://127.0.0.1:5000/. Open this URL in your web browser.

## Using the Application
Open the web application in your browser.

You will see an interface to upload a doodle image.

Draw image of a doodle (star, shoe, piano, house, popsicle, tshirt, umbrella, duck, airplane, or windmill).

Click the "Predict" button.

The application will display the predicted class of the doodle.

## Model Details
Model Architecture: Convolutional Neural Network (CNN)

Classes: star, shoe, piano, house, popsicle, tshirt, umbrella, duck, airplane, windmill

Frameworks: Tensorflow, Keras, Flask

## Future Improvements

Improve model accuracy by using a larger and more diverse dataset.

Implement real-time doodle recognition.

Add more classes to the classifier.

Implement better error handling and user feedback.

Deploy the application on a cloud platform for wider accessibility.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.   

License
Feel free to use the application and don't forget to give credits

