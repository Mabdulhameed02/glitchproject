from flask import Flask, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {
        'image1': 'C:/Users/Admin/AppData/Local/Programs/Python/Python312/dataprintfolder/templates/img/image1.jpg',
        'image2': 'C:/Users/Admin/AppData/Local/Programs/Python/Python312/dataprintfolder/templates/img/image2.jpg',
        'image3': 'C:/Users/Admin/AppData/Local/Programs/Python/Python312/dataprintfolder/templates/img/image3.jpg',
        'image4': 'C:/Users/Admin/AppData/Local/Programs/Python/Python312/dataprintfolder/templates/img/image4.jpg',
        'weight': 1223.47,
        'rfid': '1234567890'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
