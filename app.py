from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline
import os

# Set UTF-8 environment variables
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define client application class
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Define routes
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    # Execute training
    os.system("python main.py")
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    # Decode image and make prediction
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    # Initialize client application
    clApp = ClientApp()
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)  # Listening on all network interfaces, port 5000
