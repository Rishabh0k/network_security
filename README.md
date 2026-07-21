# Network Security

This project is a phishing detection application that uses a machine learning model to classify network/website data as phishing or legitimate. It covers the full pipeline — data ingestion into MongoDB, data validation, model training with experiment tracking, and a web app for serving predictions.

## Features

- **Data Ingestion**: Pushes raw data into MongoDB for centralized storage (`push_data.py`).
- **Data Validation**: Validates incoming data against a defined schema before training (`data_schema/`).
- **Model Training**: Trains a phishing detection model and tracks experiments with MLflow, hosted remotely on DagsHub (`mlflow.db`).
- **Prediction Web App**: Accepts input data and returns phishing/legitimate predictions through a simple web interface (`app.py`, `templates/`).
- **Containerized Deployment**: Packaged with Docker for easy, reproducible deployment.

## How It Works

The application consists of a data/training pipeline and a web app for inference.

1. **Data Ingestion**: `push_data.py` reads the source dataset and pushes it into a MongoDB collection.
2. **Data Validation**: Incoming data is checked against the schema in `data_schema/` to catch missing columns, wrong types, or drift before training.
3. **Training Pipeline**: `main.py` pulls validated data, trains the model, and logs metrics/artifacts to MLflow. The trained model is saved to `final_model/`.
4. **Inference**: `app.py` loads the trained model and exposes a web interface (`templates/`) where a user can submit data and get a prediction.
5. **Prediction Output**: Results are saved to `prediction_output/` for review.

## Technology Stack

- **Language**: Python
- **Database**: MongoDB
- **Experiment Tracking**: MLflow + [DagsHub](https://dagshub.com/) (remote MLflow tracking server & data/model versioning)
- **Web Framework**: [Flask / FastAPI — confirm which]
- **Deployment**: Docker

## File Structure

```
network_security/
├── data_schema/          # Schema definitions used to validate incoming data
├── network_data/          # Raw/source data
├── networksecurity/       # Core package (pipeline components: ingestion, validation, training, etc.)
├── valid_data/             # Data that has passed validation
├── final_model/            # Trained model artifacts
├── prediction_output/      # Saved prediction results
├── templates/               # HTML templates for the web app
├── app.py                   # Backend entry point (serves the web app / API)
├── main.py                  # Training pipeline entry point
├── push_data.py              # Pushes source data into MongoDB
├── test_mongodb.py           # Script to test the MongoDB connection
├── Dockerfile                # Container definition for deployment
├── requirements.txt
└── setup.py
```

- **`networksecurity/`**: Contains the core pipeline logic — data ingestion, validation, transformation, model training, and prediction components.
- **`app.py`**: The entry point for the backend. Serves the web interface and handles prediction requests.
- **`main.py`**: Runs the end-to-end training pipeline, from data ingestion through to saving the final model.
- **`push_data.py`**: Loads the source dataset and pushes it to MongoDB.
- **`data_schema/`**: Defines the expected structure of the input data, used during validation.

## Setup and Usage

To run this project, you need a MongoDB instance and Python installed.

### Backend Setup

1. Ensure you have Python and pip installed.
2. Clone the repository and navigate into it:
   ```bash
   git clone https://github.com/Rishabh0k/network_security.git
   cd network_security
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root with your MongoDB connection string and DagsHub/MLflow credentials:
   ```
   MONGO_DB_URL=https://cloud.mongodb.com/v2/673dbdd329478f4e9c4d934a#/overview
   MLFLOW_TRACKING_URI=https://dagshub.com/officialrishabh013/network_security/experiments
   MLFLOW_TRACKING_USERNAME=https://dagshub.com/officialrishabh013
   ```

### Push Data to MongoDB

```bash
python push_data.py
```

### Run the Training Pipeline

```bash
python main.py
```

### Run the Web App

```bash
python app.py
```

Once running, open your browser and navigate to the URL provided (e.g., `http://127.0.0.1:8000`).

### Run with Docker

```bash
docker build -t network-security .
docker run -p 8000:8000 network-security
```

## Dataset

The model is trained on the **UCI Phishing Websites dataset** (`phisingData.csv`), which contains **11,055 records** and **31 columns**: 30 URL and website-based features plus a binary target.

Each row represents a website, described by features extracted from its URL and page properties, such as:

- `having_IP_Address`, `URL_Length`, `Shortining_Service`, `having_At_Symbol`, `Prefix_Suffix`
- `having_Sub_Domain`, `SSLfinal_State`, `Domain_registeration_length`, `HTTPS_token`
- `Request_URL`, `URL_of_Anchor`, `Links_in_tags`, `SFH`, `Abnormal_URL`, `age_of_domain`
- `DNSRecord`, `web_traffic`, `Page_Rank`, `Google_Index`, `Links_pointing_to_page`, and more

All features are encoded numerically as `-1`, `0`, or `1` (representing suspicious, neutral, or legitimate signals respectively).

**Target variable — `Result`:**
- `1` → Phishing website (6,157 records)
- `-1` → Legitimate website (4,898 records)

## Model Performance

https://dagshub.com/officialrishabh013/network_security/experiments#/experiment/m_bcf2865d99a04434b5e65bc9e92cb5ed

## Future Improvements

- [ ] CI/CD pipeline for automated retraining
- [ ] Cloud deployment (AWS / GCP / Azure)
- [ ] API documentation
- [ ] Unit tests

## Author

**Rishabh0k**
[GitHub](https://github.com/Rishabh0k)