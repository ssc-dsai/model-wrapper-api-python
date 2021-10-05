# Model Wrapper API

API Wrapper for Machine Learning Models

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- Python 3

### Installing
Clone the repository:
```
git clone https://gitlab.com/dsa8/model-wrapper-api.git
cd model-wrapper-api
```

Optionally (**recommended**), create and activate conda environment:
```
conda create -n modelapi python=3.6  
conda activate modelapi
```
OR

```
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

Modify the .env.example file with secrets and save as `.env`.


## Running
You can now run the model locally:
```
cd src
uvicorn main:app --reload
```