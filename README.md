# Parkinson Disease Detection Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Welcome to the **Parkinson Disease Detection Using Machine Learning** project! This application leverages machine learning to predict the presence of Parkinson’s disease based on voice features, offering both manual data entry and Excel file upload options for convenience. Built with Python, Flask, and a Random Forest Classifier, this tool is designed for early detection screening and educational purposes.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Training the Model](#training-the-model)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Dual Input Support**: Enter data manually (22 voice features) or upload an Excel file with multiple records.
- **Machine Learning Prediction**: Uses a trained Random Forest Classifier for high-accuracy Parkinson’s detection.
- **Real-time Results**: Instant predictions with detailed feedback (Healthy or Parkinson’s Detected).
- **User-friendly Interface**: Styled with Tailwind CSS for a modern, responsive design.
- **File Handling**: Supports `.xlsx` files with the required 22 feature columns.

## Installation

### Prerequisites
- Python 3.x
- Git (for cloning the repository)
- pip (Python package manager)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/alphah-dev/parkinson-disease-detection-using-ml.git
   cd parkinson-disease-detection-using-ml
   ```
2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Prepare the Dataset** *(Optional: If retraining the model)*
   - Download the Parkinson’s dataset from the UCI Machine Learning Repository.
   - Save it as `parkinsons_data` in the root directory.

## Usage

### Running Locally

#### Train the Model (Optional)
Run the training script to generate or update the model and scaler:
```bash
python parkinson_ml.py
```
This creates `parkinsons_model.pkl` and `scaler.pkl`.

#### Start the Flask App
```bash
python app.py
```

#### Access the App
- Open your browser and go to `http://127.0.0.1:5000/`
- **Manual Entry**: Fill in the 22 voice feature fields and click "Predict."
- **File Upload**: Upload an Excel file (e.g., `test_data.xlsx`) with the 22 columns and click "Predict."

### Sample Excel File Format
The Excel file should have the following columns:
```
MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz), MDVP:Jitter(%), MDVP:Jitter(Abs),
MDVP:RAP, MDVP:PPQ, Jitter:DDP, MDVP:Shimmer, MDVP:Shimmer(dB),
Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA, NHR, HNR,
RPDE, DFA, spread1, spread2, D2, PPE
```
Example rows are provided in `test_data.xlsx`.

## File Structure
```
Parkinson_Disease_Detection_Using_AI/
├── app.py                  # Flask application with prediction logic
├── parkinson_ml.py         # Script to train the machine learning model
├── parkinsons_model.pkl    # Trained Random Forest model
├── parkinsons_data         # UCI dataset (optional for training)
├── parkinsons_names        # Additional dataset metadata (optional)
├── requirements.txt        # Python dependencies
├── scaler.pkl              # Scaler for feature preprocessing
├── templates/              # HTML templates
│   └── index.html          # Frontend interface
├── test_data.xlsx          # Sample test data
├── test_data1.xlsx         # Additional test data
├── test_data2.xlsx         # Additional test data
├── .gitignore              # Git ignore file
├── Procfile                # Deployment configuration
```

## Training the Model
The model is pre-trained and saved as `parkinsons_model.pkl`. To retrain:

1. Ensure `parkinsons_data` is present.
2. Run:
   ```bash
   python parkinson_ml.py
   ```
   This generates new `.pkl` files.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Contact
- **Author**: alphah-dev
- **Email**: katiyarh76@gmail.com  
- **GitHub**: [https://github.com/alphah-dev](https://github.com/alphah-dev)

