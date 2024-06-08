### Financial Data Analysis and Forecasting Platform

## Project Overview

The Financial Data Analysis and Forecasting Platform is designed to process large datasets of financial transactions, perform time series analysis and forecasting, and provide insights to users. This application leverages PySpark for data processing and analysis, FastAPI for serving insights through a RESTful API, and a React frontend for visualization. Docker is used for containerization, and Kubernetes is used for deployment on Azure.

## Key Features

- **Data Ingestion**: Read large datasets using PySpark.
- **Data Processing**: Perform transformations, analysis, and forecasting using PySpark.
- **API Service**: Serve processed data and forecasts through a RESTful API using FastAPI.
- **Frontend Visualization**: Visualize financial data and forecasts using a React-based frontend.
- **Cloud Infrastructure**: Deploy the application on Azure using Docker and Kubernetes.

## Tech Stack

### Backend

- **Python**: Programming language used for backend development.
- **PySpark**: For large-scale data processing and analysis.
- **FastAPI**: Web framework for building the RESTful API.
- **Pandas**: Data manipulation and analysis library.
- **Uvicorn**: ASGI server for serving FastAPI applications.
- **Docker**: For containerizing the backend application.

### Frontend

- **React**: JavaScript library for building user interfaces.
- **Axios**: For making HTTP requests from the frontend to the backend API.
- **Docker**: For containerizing the frontend application.

### Cloud Infrastructure

- **Kubernetes**: For orchestrating the deployment of containerized applications.
- **Azure**: Cloud platform for deploying the Kubernetes cluster.


## Setup Instructions

### Backend Setup

1. **Ensure you have Python and PySpark installed.**
2. **Create the necessary directories:**
   ```sh
   mkdir -p FinancialDataPlatform/backend/data
3. Place your input data in the data directory.
4. Navigate to the backend directory:

   cd FinancialDataPlatform/backend

5. Create and activate a virtual environment:

   python -m venv venv
source venv/bin/activate

On Windows use `venv\Scripts\activate`

6. Install the required packages:

   pip install -r requirements.txt
   
7. Run the data processing script:

  python data_processing.py

8. Run the FastAPI server:

  uvicorn main:app --host 0.0.0.0 --port 80

### Frontend Setup

Ensure you have Node.js and npm installed.
Navigate to the frontend directory:

cd FinancialDataPlatform/frontend

Install the dependencies:

npm install

Start the frontend development server:

npm start

### Docker Setup

1. Build the backend Docker image:

cd FinancialDataPlatform/backend
docker build -t financial-data-backend .

2. Build the frontend Docker image:

cd FinancialDataPlatform/frontend
docker build -t financial-data-frontend .

### Kubernetes Deployment

1. Create an Azure Kubernetes Service (AKS) cluster:

az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 3 --enable-addons monitoring --generate-ssh-keys

2. Get the AKS credentials:
   
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster

5. Deploy the backend and frontend services to Kubernetes:

kubectl apply -f FinancialDataPlatform/deployment/backend-deployment.yaml

kubectl apply -f FinancialDataPlatform/deployment/backend-service.yaml

kubectl apply -f FinancialDataPlatform/deployment/frontend-deployment.yaml

kubectl apply -f FinancialDataPlatform/deployment/frontend-service.yaml

6. Get the external IP of the frontend service:

kubectl get service financial-data-frontend-service

Access the application in your browser using the external IP address.

### Contributing 
If you would like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

### License
This project is open source and available under the MIT License.
