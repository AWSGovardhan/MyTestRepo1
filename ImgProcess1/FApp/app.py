from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This serves the HTML UI

@app.route('/process_data', methods=['POST'])
def process_data():
    # This route receives data from the UI, processes it, and sends a response
    data = request.json  # Assuming you send JSON data from the frontend
    # Process the data and interact with the backend
    result = {"message": "Data processed successfully!"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
