
# Hangyman App

This is a well-known game called hangman, hope you enjoy playing it!

## Running Locally

1. **Install dependencies:**
   ```bash
   pip install flask

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to `http://127.0.0.1:8080`.

## Deploying to Google Cloud Run

1. **Build the Docker image:**
   ```bash
   docker build -t .
   ```

2. **Push the image to Google Container Registry (GCR):**
   ```bash
   docker push gcr.io/your-gcp-project-id/hangyman
   ```

3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy --image gcr.io/your-gcp-project-id/hangyman --platform managed
   ```
