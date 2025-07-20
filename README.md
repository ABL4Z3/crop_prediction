# Smart Crop Recommender

This project is a Smart Crop Recommender system that predicts the most suitable crop to grow based on soil and weather conditions. It consists of a FastAPI backend that serves a machine learning model for crop prediction and a Streamlit frontend that provides an interactive user interface.

## Features

- Input soil nutrient levels (Nitrogen, Phosphorus, Potassium)
- Input weather conditions (Temperature, Humidity, Rainfall)
- Input soil pH value
- Predict the best crop to grow based on the inputs using a pre-trained machine learning model
- Interactive web interface using Streamlit

## Project Structure

- `main.py`: FastAPI backend application exposing the `/predict` endpoint for crop prediction.
- `streamlit_app.py`: Streamlit frontend application for user input and displaying prediction results.
- `best_model_pipeline.pkl`: Pre-trained machine learning model pipeline used for prediction.
- `patients.json`: (Not currently used) JSON file possibly for patient data management.
- `myenv/`: Python virtual environment directory containing dependencies.

## Installation

1. Clone the repository.

2. Create and activate a Python virtual environment (optional but recommended):

```bash
python -m venv myenv
# On Windows
myenv\Scripts\activate
# On Unix or MacOS
source myenv/bin/activate
```

3. Install required dependencies:

```bash
pip install fastapi uvicorn streamlit pandas scikit-learn requests
```

## Running the Backend API

Start the FastAPI server by running:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Running the Streamlit Frontend

In a separate terminal (with the virtual environment activated), run:

```bash
streamlit run streamlit_app.py
```

This will open the Streamlit app in your default web browser.

## Usage

1. Use the sliders in the Streamlit app to input soil and weather parameters.
2. Click the "Predict Crop Suitability" button.
3. The app will send the data to the FastAPI backend and display the predicted crop.

## Notes

- Ensure the FastAPI backend is running before using the Streamlit frontend.
- The model file `best_model_pipeline.pkl` must be present in the project root directory.
- The current API only supports the `/predict` endpoint for crop prediction.

## License

This project is provided as-is without any warranty.
