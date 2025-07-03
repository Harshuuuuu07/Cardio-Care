import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib


# Load and preprocess data
df = pd.read_csv("cardio_train.csv", sep=';')
df.drop('id', axis=1, inplace=True)
df['age'] = (df['age'] / 365).astype(int)

# Split features and target
x = df.drop('cardio', axis=1)
y = df['cardio']

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42, class_weight='balanced')
model.fit(x_train, y_train)

joblib.dump(model, 'cardio_model.pkl')
print("✅ Model saved as cardio_model.pkl")
