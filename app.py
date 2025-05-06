# app.py
from flask import Flask, request, jsonify
from scraper import scrape_cfe_receipt

app = Flask(__name__)

@app.route('/')
def index():
    return 'CFE Receipt Scraper API'

@app.route('/api/receipt', methods=['POST'])
def get_receipt():
    data = request.get_json()
    rpu = data.get('rpu')
    if not rpu:
        return jsonify({'error': 'Missing RPU number'}), 400

    try:
        receipt_data = scrape_cfe_receipt(rpu)
        return jsonify({'success': True, 'data': receipt_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

