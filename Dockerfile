FROM python:3.10.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application files and model to the container
COPY app.py .
COPY utils/onnx_runtime.py utils/
COPY models/CNN_Model_Sign_Language_best.onnx models/

# Expose the port on which your Streamlit app runs (default is 8501)
EXPOSE 8501

# Run the StreamSign application when the container starts
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
