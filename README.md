# Tumor Detection Web App Using Roboflow

## https://drive.google.com/file/d/1AkVuUaSz5gext71qNSJ5qCoMB2abehkB/view

## Overview

This project is a Flask-based web application that lets users upload medical images, like CT scans, and runs tumor detection on them using a custom-trained Roboflow model. The app processes the image, highlights detected tumors, and displays the results in the browser.

## Technology Stack

* *Flask*: Lightweight Python web framework managing the backend and web routes.
* *OpenCV*: Used for loading images, drawing bounding boxes around detected tumors, and saving the output images.
* *Roboflow Inference API*: Powers the tumor detection with a custom machine learning model hosted on Roboflow.
* *UUID*: Generates unique filenames to prevent file clashes during uploads.
* *Jinja2 Templates*: Dynamically renders results on the frontend.
* *Python 3.10+*: Modern Python features ensure reliable and clean code.

## How It Works

1. User uploads a medical image through the website.
2. Flask saves the image with a unique name in a designated static folder.
3. The saved image is sent to the Roboflow model for inference via a local inference module.
4. The model returns tumor predictions, which are drawn on the image using OpenCV.
5. The annotated image is saved and shown to the user on the webpage.

## Setup Instructions (with commands)

1. *Clone the repository:*

   bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   

2. *Create and activate a Python virtual environment:*

   On Windows:

   bash
   python -m venv venv
   venv\Scripts\activate
   

   On macOS/Linux:

   bash
   python3 -m venv venv
   source venv/bin/activate
   

3. *Install dependencies:*

   bash
   pip install -r requirements.txt
   

4. *Run the Flask app:*

   bash
   python app.py
   

5. *Open your browser and go to:*

   
   http://127.0.0.1:5000/
   

## Important Notes

* The app runs inference on the CPU by default to ensure it works on most machines.
* All uploaded images and their processed results are stored inside the static/results directory.
* You can customize the deployed model by updating the model ID and API key in the inference script.

## Social Impact and Ethical Considerations

This kind of AI-powered tumor detection tech can revolutionize early cancer diagnosis by making advanced imaging analysis accessible to more people, especially in areas lacking expert radiologists. Early detection can drastically improve patient outcomes and reduce healthcare costs.

That said, it’s vital to stay cautious: AI models aren’t perfect. False positives or negatives can lead to anxiety or missed diagnoses. This app should not replace medical professionals but serve as a supportive tool. Privacy of patient data is paramount and must be rigorously protected. Transparency about the model’s accuracy and limits is essential to build trust.

When responsibly developed and deployed, AI diagnostic tools like this could genuinely transform healthcare—making it faster, fairer, and more accessible worldwide.


![image](https://github.com/user-attachments/assets/e9a7e76e-03f3-4af7-a385-ff91b1030392)

