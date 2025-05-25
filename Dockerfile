FROM python:3.10.3-slim-bullseye

WORKDIR /app

COPY . .

# Create virtual environment and install dependencies in one step
RUN pip install langchain flask flask-cors langchain-google-genai dotenv

EXPOSE 5007

# Run the app using the virtual environment
CMD ["python", "agent.py"]

