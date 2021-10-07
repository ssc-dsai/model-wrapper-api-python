# Model API Wrapper

Model API Wrapper, like the name suggest, is an API template that wraps a Machine Learning model. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3 / Anaconda

### Installing
Clone the repository:
```
git clone https://gitlab.com/dsa8/model-wrapper-api.git
cd model-wrapper-api
```

Optionally (**recommended**), create and activate conda environment:
```
conda create -n modelapi  
conda activate modelapi
```

Install requirements:
```
pip install -r requirements.txt
```

Modify the .env.example file with secrets and save as `.env` in the root directory.

### Using the API Wrapper

To use this API you only need to modify the Model class in src/model.py

The class requires 3 things:
- A model property to store the active model
- A init method to activate/load the model
- A run method for your prediction code

FastAPI recommends that you use types to validate your requests.
Examples are already in src/model.py

## Running
You can now run the model locally:
```
cd src
uvicorn main:app --reload
```

By default, this will start the server on port 8000.


### Running unit tests
TODO

### TODO
- Testing code
- CI/CD Pipeline
- Add logger for monitoring