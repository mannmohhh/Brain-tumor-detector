from flask import Flask, render_template, request, send_from_directory
import os
import uuid
from roboflow_infer import run_inference  # Make sure this exists and works
import shutil

app = Flask(__name__)  # Fixed: __name__ instead of _name_

UPLOAD_FOLDER = os.path.join('static', 'results')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    result_filename = None
    uploaded_filename = None

    if request.method == "POST":
        file = request.files.get('image')  # Safer way
        if file and file.filename:
            filename = f"{uuid.uuid4().hex}_{file.filename}"
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)

            # Run inference and get result
            result_filename = f"result_{filename}"
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)

            try:
                _, _ = run_inference(image_path=upload_path, save_path=result_path)
            except Exception as e:
                print(f"[ERROR] Inference failed: {e}")
                result_filename = None

            uploaded_filename = filename

    return render_template("index.html", result_image=result_filename, original_image=uploaded_filename)

@app.route('/static/results/<filename>')
def send_result(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":  # Fixed: __name__ instead of _name_
    print("Flask is starting...")  # Debug print
    app.run(debug=True)
