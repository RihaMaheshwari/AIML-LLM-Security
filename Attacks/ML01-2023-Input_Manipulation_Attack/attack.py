# ML01:2023 - Input Manipulation Attack
# This attack is a type of adversarial attack that aims to manipulate the input data to cause the machine learning model to make incorrect predictions.

# Demo - https://jagskap.blogspot.com/2025/02/input-manipulation-attacks-on-ml-models.html

import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load the pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Specify the correct path to your image
img_path = 'uploads/umbrella.jpg'

# Load and preprocess the image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Convert img_array to a tf.Tensor
img_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)

# Set the target for the attack (e.g., the original label of the image)
target_label = 1  # Example: targeting class 1 (cat)

with tf.GradientTape() as tape:
    tape.watch(img_tensor)  # Watch the tensor
    predictions = model(img_tensor)
    # Adjust target shape to match predictions: target should be (batch_size, 1)
    target_tensor = tf.convert_to_tensor([target_label], dtype=tf.int64)
    loss = tf.keras.losses.sparse_categorical_crossentropy(target_tensor, predictions)

# Calculate the gradients of the loss w.r.t the input image
gradients = tape.gradient(loss, img_tensor)

# Generate the adversarial image
epsilon = 0.1  # Adjust epsilon for intensity
adversarial_image = img_tensor + epsilon * tf.sign(gradients)

# Save the adversarial image
adversarial_image = np.squeeze(adversarial_image.numpy(), axis=0)
adversarial_image = tf.keras.preprocessing.image.array_to_img(adversarial_image)
adversarial_image.save('adversarial_image.jpg')
