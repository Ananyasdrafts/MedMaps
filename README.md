# MedMaps

Welcome to the MedMaps repository! This project aims to track patients' heart rate, diabetes, and drug intake to predict necessary safety checkups before it's too late. Additionally, it features a drug-drug interaction checker and optical character recognition (OCR).

## Features

### Health Monitoring and Prediction
- **Input:** Patient heart rate, diabetes status, and insulin intake.
- **Output:** Predicts when a safety checkup is needed.
- **Model:** Utilizes LSTMs and Attention Mechanisms for accurate tracking and prediction.

### Drug-Drug Interaction Checker
- **Input:** Two medication names.
- **Output:** Information on potential interactions and side effects.

### Optical Character Recognition (OCR)
- **Input:** Text from medical prescriptions.
- **Output:** Extracted and analyzed data for monitoring and prediction.

## Repository Structure

- **Diabetestrack/**: Contains the code for training and utilizing the LSTMs and Attention Mechanisms for health tracking and prediction.
  - `train_model.ipynb`: Notebook containing the models (LSTM with attention mechanism, autoencoder) as well as script for making health predictions based on data.
  - `README.md`: Details about relevant datasets.
- **Frontend/**: Contains the code for the user interface of the app.
- **heart-health-tracker/**: Contains alternative code for health tracking, specifically applied to heart health monitoring.
  - `medmap.ipynb`: Script for running the alternate health tracking code.
  - `README.md`: Details about relevant datasets.
- **Datasets/**: Folder containing relevant datasets.
- **API.py**: API endpoint for the model and the interaction checker.
- **DDI/**: Contains the code for the drug-drug interaction checker.
  - `DDI.py`: Script for checking interactions between two medications.
  - `README.md`: Details about relevant datasets.
- **OCR/**: Contains the code for the OCR functionality.
- **requirements.txt**: Lists all the necessary libraries and dependencies required for the project, ensuring a smooth setup and consistent environment.

## Prerequisites

- Python 3.x
- Required libraries in `requirements.txt`

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

## Contributing

We welcome contributions to enhance the functionality and features of this app. To contribute, please fork the repository, create a new branch, make your changes, and submit a pull request.

## Contact

For any questions or suggestions, please open an issue in this repository or contact the project maintainers at either ananyag1019@gmail.com or tanishqatojo23@gmail.com.

Thank you for using MedMaps! We hope it helps you manage your health safely and effectively.

