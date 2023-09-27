from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for a sample page
@app.route('/samplepage')
def sample():
    return render_template('samplepage.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json  # Assuming the data is sent as JSON
    result = {'message': 'Data received and processed successfully'}
    return jsonify(result)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
