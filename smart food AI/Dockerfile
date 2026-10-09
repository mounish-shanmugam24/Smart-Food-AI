# Use Python 3.12 for 2026 compatibility
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Cloud Run expects the app to listen on the port provided by the $PORT variable
ENV PORT=8080

# Run Streamlit and force it to use the Cloud Run port
CMD ["sh", "-c", "streamlit run app.py --server.port=${PORT} --server.address=0.0.0.0 --server.enableCORS=false"]