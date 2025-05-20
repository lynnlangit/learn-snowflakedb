import snowflake.snowpark as snowpark
import tensorflow as tf
import numpy as np

def create_mnist_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def main(session: snowpark.Session):
    print("Starting MNIST TensorFlow example...")

    print("Loading MNIST data using tf.keras.datasets.mnist.load_data()...")
    print("Note: For production Snowflake, data should be in tables or stages.")
    (x_train, y_train_raw), (x_test, y_test_raw) = tf.keras.datasets.mnist.load_data()

    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = np.expand_dims(x_train, -1) 
    x_test = np.expand_dims(x_test, -1)

    y_train = tf.keras.utils.to_categorical(y_train_raw, num_classes=10)
    y_test = tf.keras.utils.to_categorical(y_test_raw, num_classes=10)

    print(f"x_train shape: {x_train.shape}")
    print(f"y_train shape: {y_train.shape}")

    print("Creating and training the TensorFlow model...")
    model = create_mnist_model()
    model.summary() 

    model.fit(x_train, y_train, epochs=5, validation_split=0.1)
    print("Evaluating the model...")
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")

    # In Snowflake, you might save to a stage or use Snowpark ML Model Registry
    # model.save('mnist_model.h5') # Standard Keras way
    print("Placeholder: Logic to save the trained model (e.g., to a Snowflake stage or model registry).")

    return f"Successfully executed MNIST TensorFlow example. Test Accuracy: {accuracy:.4f}"

# Entry point for local execution (requires Snowflake connection params)
if __name__ == "__main__":
#     # This part is for local testing and might need adjustment
#     # based on how you set up your Snowflake connection.
#     # Create a dummy Snowpark session for local run if needed,
#     # or connect to a real Snowflake instance.
print("Running main() for local testing (Snowflake session might be mocked or need configuration)...")   

        def __init__(self):
            self.query_history = []
        def sql(self, query):
            self.query_history.append(query)
            print(f"MockSession: Executed SQL: {query}")
            # Potentially return a mock DataFrame if your code uses it extensively
            return None 
