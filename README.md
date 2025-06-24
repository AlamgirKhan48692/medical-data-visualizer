# 🩺 Medical Data Visualizer

This project performs **Exploratory Data Analysis (EDA)** and visualization on a medical examination dataset using Python. It includes data cleaning, transformation, and the creation of visualizations like a categorical plot and a heatmap.

> Part of the FreeCodeCamp Data Analysis with Python certification projects.

---

## 📁 Repository Contents

- `medical_data_visualizer.py`: Core script containing data cleaning and plotting logic.
- `Medical_Data_Visualizerrr.py`: Likely an earlier or alternate version of the main script.
- `main.py`: Script to execute the visualizer functions.
- `medical_examination.csv`: The dataset containing health metrics of patients.
- `catplot.png`: Output image showing categorical data comparisons.
- `heatmap.png`: Output image showing correlation heatmap.
- `__pycache__/`: Compiled Python cache files (auto-generated).

---

## 📊 Visualizations

### 1. Categorical Plot (`catplot.png`)
- Compares variables such as cholesterol, glucose, smoking, alcohol intake, etc.
- Shows count distribution grouped by cardiovascular disease presence.

### 2. Heatmap (`heatmap.png`)
- Displays the correlation matrix of numerical features.
- Highlights relationships between health metrics like BMI, blood pressure, and cholesterol.

---

## ⚙️ Requirements

Make sure you have the following libraries installed:

```bash
pip install pandas seaborn matplotlib


▶️ How to Run

Place the medical_examination.csv file in the same directory as your script.

Run the main file:

bash
Copy
Edit
python main.py
The script will:

Clean and process the data.

Generate catplot.png and heatmap.png as output.

📬 Contact
For feedback or contributions, feel free to fork the repo or open an issue.
