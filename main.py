import joblib
import tensorflow as tf
from sklearn.compose import ColumnTransformer

# Load the model
model = tf.keras.models.load_model('my_model.h5')

# Load the column transformer
column_transformer = joblib.load('my_column_transformer.joblib')



while True:
    A = float(input("Entrer A : "))
    scaled_A = column_transformer.transform(A)
    B = model.predict(scaled_A)
    print(f"B = {B}")
    c=input("---------------------To continue tap 1 to exit tap 0 :")
    if c == '0':
        break