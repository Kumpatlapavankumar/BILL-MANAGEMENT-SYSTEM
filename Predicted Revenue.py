import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load your CSV file (assuming it's named 'sales_data.csv')
data = pd.read_csv('E:\sales_data.csv')

# Preprocess the data if necessary (e.g., convert date strings to datetime)
data['Date'] = pd.to_datetime(data['Date'])

# Specify your features (X) and target variable (y)
features = ['Day', 'Month', 'Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price']
X = data[features]
y = data['Revenue']

# Define which features are categorical
categorical_features = ['Month']

# Create a preprocessor to handle categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'
)

# Create a pipeline with preprocessing and the linear regression model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model.fit(X_train, y_train)

# Use the model to make revenue predictions
revenue_predictions = model.predict(X_test)

# Display the predictions
for i, prediction in enumerate(revenue_predictions):
    print(f"Sample {i + 1} - Predicted Revenue: ${prediction:.2f}")

# You can further evaluate the model's performance with metrics like R-squared, Mean Absolute Error, etc.
