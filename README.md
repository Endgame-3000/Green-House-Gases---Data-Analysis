# Django CSV Data Analysis and Visualization Web App

This Django web application allows users to upload CSV files, perform basic data analysis using pandas, and visualize the data using matplotlib.

## Features

- **File Upload**: Upload CSV files.
- **Data Processing**: Display first few rows, summary statistics, and handle missing values.
- **Data Visualization**: Generate and display histograms for numerical columns.
- **User Interface**: Simple and user-friendly interface using Django templates.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/Endgame-3000/Green-House-Gases---Data-Analysis.git
cd Green-House-Gases---Data-Analysis
```

### Step 2: Set Up a Virtual Environment

Create and activate a virtual environment to manage project dependencies.

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS and Linux

```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Django Project

Make sure the Django settings are configured correctly, especially the `ALLOWED_HOSTS` and static files settings.

```python
# myproject/settings.py

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### Step 5: Apply Database Migrations

Run the following command to apply the database migrations.

```bash
python manage.py migrate
```

### Step 6: Collect Static Files

Collect static files to the `STATIC_ROOT` directory.

```bash
python manage.py collectstatic
```

When prompted with `Are you sure you want to do this?`, type `yes` and press Enter.

### Step 7: Run the Development Server

Start the Django development server.

```bash
python manage.py runserver
```

### Step 8: Access the Application

Open your web browser and navigate to `http://127.0.0.1:8000/dataapp/upload/`.

### Step 9: Upload a CSV File

Use the provided form to upload a CSV file and view the data analysis and visualizations. 

## Sample CSV File

A sample CSV file (`sample_data.csv`) is provided in the repository for testing purposes. 


