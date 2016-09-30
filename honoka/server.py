from init import app
from config import TEST

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=TEST)
