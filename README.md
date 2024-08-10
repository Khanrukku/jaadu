# Jaadu - The Mood Lifter

**Jaadu** is a simple web application designed to boost your mood with motivational lines based on your current emotional state. Whether you're feeling happy, sad, or anything in between, Jaadu provides a quick and uplifting message to help you shift your perspective.

## Features

- **Mood-Based Uplifting Lines:** Enter your current mood to receive a relevant motivational line.
- **User-Friendly Interface:** Simple and intuitive design for easy navigation.
- **Instant Feedback:** Get an uplifting line immediately based on your mood input.

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Local Server:** Flask development server

## Installation

To set up and run Jaadu locally, follow these steps:

### 1. Clone the Repository

If you have a Git repository for Jaadu, clone it using:

```bash
git clone <repository-url>
cd jaadu-app
```
2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:

```bash

python -m venv venv
```
On Windows:

```bash

venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```
3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

4. Run the Flask App
Start the Flask development server:

```bash

python app.py
```
The app will be accessible at http://127.0.0.1:5000/.

Usage
Open your web browser and go to http://127.0.0.1:5000/.
Enter your current mood into the input field.
Click the "Get Uplifting Line" button.
Read the motivational line provided to lift your mood.
