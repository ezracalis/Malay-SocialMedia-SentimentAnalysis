# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy your Flask application and model file
COPY sentiment.py .
COPY 03_production_sentiment_model.pkl .

# Install any necessary Python libraries for your Flask app
RUN pip install flask joblib requests scikit-learn pandas numpy imbalanced-learn

# Expose the port your Flask app will run on
EXPOSE 8081

# Run the Flask app
CMD ["python", "sentiment.py"]
