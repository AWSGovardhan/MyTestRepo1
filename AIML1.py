import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Load and preprocess the dataset (for example, the CIFAR-10 dataset)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalize pixel values

# Create a simple CNN model using Keras
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)  # Output layer with 10 classes (CIFAR-10 has 10 classes)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Load an image using OpenCV for prediction
image_path = 'path_to_image.jpg'
image = cv2.imread(image_path)
image = cv2.resize(image, (32, 32))  # Resize the image to match the model's input size
image = np.expand_dims(image, axis=0)  # Add batch dimension

# Make a prediction
predictions = model.predict(image)
predicted_class = np.argmax(predictions)

# Print the predicted class
print(f'Predicted Class: {predicted_class}')
