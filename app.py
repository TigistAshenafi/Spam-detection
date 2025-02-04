from flask import Flask, request, jsonify, render_template 
from sms_classifier import classify_sms 

app = Flask(__name__, static_folder='public')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_endpoint():
    try:
        data = request.get_json()
        sms_message = data.get('sms')
        if not sms_message:
            return jsonify({'error': 'No SMS message provided'}), 400

        prediction = classify_sms(sms_message)
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)

