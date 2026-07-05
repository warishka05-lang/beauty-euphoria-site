from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import json, os, secrets, uuid
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')
BOOKINGS_FILE = os.path.join(os.path.dirname(__file__), 'bookings.json')
IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(IMAGES_DIR, exist_ok=True)
ALLOWED_EXT = {'png','jpg','jpeg','webp','gif'}
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN', 'change-me-secret-token')

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(default, f, ensure_ascii=False, indent=2)
        return default
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def check_auth(req):
    token = req.headers.get('Authorization', '').replace('Bearer ', '')
    return token == ADMIN_TOKEN

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/admin.html')
def serve_admin():
    return send_from_directory('.', 'admin.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = load_json(DATA_FILE, {})
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def update_data():
    if not check_auth(request):
        return jsonify({'error': 'Unauthorized'}), 401
    new_data = request.get_json()
    save_json(DATA_FILE, new_data)
    return jsonify({'status': 'ok'})

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    if not check_auth(request):
        return jsonify({'error': 'Unauthorized'}), 401
    bookings = load_json(BOOKINGS_FILE, [])
    return jsonify(bookings)

@app.route('/api/bookings', methods=['POST'])
def add_booking():
    booking = request.get_json()
    booking['createdAt'] = datetime.utcnow().isoformat()
    bookings = load_json(BOOKINGS_FILE, [])
    bookings.append(booking)
    save_json(BOOKINGS_FILE, bookings)
    return jsonify({'status': 'ok'})

@app.route('/api/bookings/clear', methods=['POST'])
def clear_bookings():
    if not check_auth(request):
        return jsonify({'error': 'Unauthorized'}), 401
    save_json(BOOKINGS_FILE, [])
    return jsonify({'status': 'ok'})

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGES_DIR, filename)

@app.route('/api/upload', methods=['POST'])
def upload_image():
    if not check_auth(request):
        return jsonify({'error': 'Unauthorized'}), 401
    if 'file' not in request.files:
        return jsonify({'error': 'Brak pliku'}), 400
    file = request.files['file']
    ext = file.filename.rsplit('.', 1)[-1].lower() if '.' in file.filename else ''
    if ext not in ALLOWED_EXT:
        return jsonify({'error': 'Niedozwolony format pliku'}), 400
    filename = secure_filename(f"{uuid.uuid4().hex}.{ext}")
    file.save(os.path.join(IMAGES_DIR, filename))
    return jsonify({'url': f'/images/{filename}'})

@app.route('/api/login', methods=['POST'])
def login():
    body = request.get_json() or {}
    password = body.get('password', '')
    if password == os.environ.get('ADMIN_PASSWORD', 'euphoria2026'):
        return jsonify({'token': ADMIN_TOKEN})
    return jsonify({'error': 'Nieprawidlowe haslo'}), 401

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print('=' * 50)
    print('Beauty Euphoria - serwer wystartowal!')
    print('Strona:       http://localhost:' + str(port))
    print('Panel admina: http://localhost:' + str(port) + '/admin.html')
    print('Haslo admina domyslnie: euphoria2026')
    print('=' * 50)
    app.run(host='0.0.0.0', port=port, debug=False)
