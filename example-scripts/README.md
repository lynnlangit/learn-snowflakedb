# Running the MNIST TensorFlow Example in Snowflake

How to run the `mnist.py` script, which uses TensorFlow for the MNIST handwritten digit recognition task, within a Snowflake environment.

## Prerequisites

1.  **Snowpark for Python**: Ensure your Snowflake account and client environment are set up for Snowpark. You'll need the `snowflake-snowpark-python` library.
2.  **TensorFlow**: The Python environment within Snowflake where this script will run must have TensorFlow installed.
    *   When creating a Stored Procedure or User-Defined Function (UDF), you can specify TensorFlow in the `packages` or `imports` clause, typically from the Snowflake Anaconda channel.
3.  **MNIST Dataset**:
    *   **Option A (Using `tf.keras.datasets.mnist.load_data()` - Recommended for initial setup/dev)**: The `mnist.py` script currently uses `tf.keras.datasets.mnist.load_data()`. For this to work within a Snowflake Stored Procedure, the Snowflake environment needs outbound internet access to download the dataset. This might be restricted by default. The first time it runs, it will download the data to a temporary location accessible by the Python environment.
    *   **Option B (Loading from Snowflake Stage/Table - Recommended for Production)**: For production or environments without internet access, it's best to pre-load the MNIST dataset (e.g., as CSV or Parquet files) into a Snowflake stage. You would then modify `mnist.py` to read from this stage using Snowpark DataFrames and convert the data into the format expected by TensorFlow. The placeholder function `load_mnist_data_from_snowflake` in `mnist.py` illustrates where this logic would go.
4.  **Permissions**: Ensure the Snowflake role used has the necessary permissions to create stored procedures, use the warehouse, and access any stages/tables if using Option B for data.

## Running `mnist.py` in Snowflake

The most common way to run such a script in Snowflake is by deploying it as a Stored Procedure.

### 1. Packaging and Dependencies

When creating the Stored Procedure, you need to specify `tensorflow` and `numpy` as package dependencies. Snowflake will attempt to resolve these from its Anaconda channel.

### 2. Creating the Stored Procedure

Here's an example of how you might create a stored procedure from `mnist.py`. You would typically run this DDL from a Snowflake worksheet or a SnowSQL client.

```sql
CREATE OR REPLACE PROCEDURE PY_MNIST_TENSORFLOW_EXAMPLE()
RETURNS STRING
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'  -- Or your desired Python version supported by Snowpark
PACKAGES = ('snowflake-snowpark-python', 'tensorflow', 'numpy')
HANDLER = 'mnist.main'
AS
$$
# Ensure mnist.py is uploaded to a stage, or paste its content here.
# If pasting, you might need to adjust imports if mnist.py calls other local files.
# For simplicity, this example assumes mnist.py will be provided inline
# or through an import from a stage.

# Option 1: Upload mnist.py to a stage (e.g., '@mystage')
# IMPORTS = ('@mystage/mnist.py')
# Then the AS section would be empty if the handler is correctly pointing.

# Option 2: Paste the content of mnist.py directly here:
import snowflake.snowpark as snowpark
import tensorflow as tf
import numpy as np

# ... (Paste the entire content of mnist.py here, from imports to the end,
#      excluding the if __name__ == "__main__": block if it exists and is not needed for SP execution)
#      Make sure the main function is defined as per the HANDLER.

# [Pasted content of mnist.py would go here]
# For this example, let's assume the mnist.py code provided previously is pasted here.
# Ensure the main function signature matches what Snowpark expects for a Stored Proc handler.
# The mnist.py example has main(session: snowpark.Session) which is correct.

# --- Start of pasted mnist.py content ---
# Note: This is a conceptual guide. In practice, you'd use IMPORTS or ensure the code is correctly formatted.
# For brevity, only a snippet of the mnist.py structure is shown here. Refer to the actual file.

# def main(session: snowpark.Session): ...
# def create_mnist_model(): ...
# [The actual Python code from mnist.py]
# --- End of pasted mnist.py content ---
# The actual Python code from mnist.py should be included here if not using IMPORTS.

# The following is a direct copy of the relevant parts from the current mnist.py for illustration
# In a real scenario, manage this code properly via staging or ensure it's within the $$ quotes.

def create_mnist_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def main(session: snowpark.Session):
    print("Starting MNIST TensorFlow example inside Snowflake Stored Procedure...")

    print("Loading MNIST data using tf.keras.datasets.mnist.load_data()...")
    print("Note: Ensure Snowflake environment has internet access for download, or use staged data.")
    (x_train, y_train_raw), (x_test, y_test_raw) = tf.keras.datasets.mnist.load_data()

    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    # Reshape for models expecting channel dimension if using CNN, or ensure Flatten handles it.
    # For the current MLP, Flatten input_shape=(28,28) is fine. If using Conv2D, expand_dims is needed.
    # x_train = np.expand_dims(x_train, -1) 
    # x_test = np.expand_dims(x_test, -1)

    y_train = tf.keras.utils.to_categorical(y_train_raw, num_classes=10)
    y_test = tf.keras.utils.to_categorical(y_test_raw, num_classes=10)

    print(f"x_train shape: {x_train.shape}")
    print(f"y_train shape: {y_train.shape}")

    print("Creating and training the TensorFlow model...")
    model = create_mnist_model()
    model.summary()

    model.fit(x_train, y_train, epochs=5, validation_split=0.1) # Consider reducing epochs for SP limits

    print("Evaluating the model...")
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")

    print("Placeholder: Logic to save the trained model (e.g., to a Snowflake stage or model registry).")

    return f"Successfully executed MNIST TensorFlow example from SP. Test Accuracy: {accuracy:.4f}"

$$;

-- Note on using IMPORTS:
-- 1. Upload mnist.py to a named stage:
--    PUT file:///path/to/your/local/example-notebooks/mnist.py @your_stage_name/mnist_py_dir/ AUTO_COMPRESS=FALSE OVERWRITE=TRUE;
-- 2. Then modify the CREATE PROCEDURE statement:
--    IMPORTS = ('@your_stage_name/mnist_py_dir/mnist.py')
--    HANDLER = 'mnist_py_dir.mnist.main' 
--    And the AS $$ $$ block would be empty.
```

### 3. Calling the Stored Procedure

Once created, you can call the stored procedure:

```sql
CALL PY_MNIST_TENSORFLOW_EXAMPLE();
```

The output (return value and anything printed to stdout by the Python script) can be viewed in your Snowflake client or query history.

## Considerations

*   **Execution Time**: Training neural networks can be time-consuming. Stored Procedures have time limits. For larger models or more epochs, consider:
    *   Reducing epochs/batch size for execution within SP limits.
    *   Using Snowpark-optimized warehouses.
    *   For very long training jobs, Snowflake's support for external functions or more specialized ML platforms integrated with Snowflake might be more suitable.
*   **Resource Limits**: Be mindful of memory and CPU limits for the warehouse running the stored procedure. TensorFlow can be resource-intensive.
*   **Logging and Debugging**: Use `print()` statements in your Python code for logging. These will appear in the query profile/results.
*   **Alternative: Snowpark ML (Generally Available)**: For more integrated ML workflows, explore [Snowpark ML](https://docs.snowflake.com/en/developer-guide/snowpark-ml/index). It provides tools for preprocessing, training (including distributed training for some model types), and model management that might streamline TensorFlow usage in Snowflake.

This guide provides a starting point. Adapt it based on your specific Snowflake setup and requirements.
```
