from flask import Flask, render_template_string
import os

app = Flask(__name__)

counter = 0

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Demo App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            text-align: center;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        h1 {
            color: #333;
            margin: 0 0 20px 0;
        }
        .counter {
            font-size: 48px;
            font-weight: bold;
            color: #667eea;
            margin: 20px 0;
        }
        .info {
            color: #666;
            font-size: 14px;
            margin-top: 20px;
            padding: 10px;
            background: #f0f0f0;
            border-radius: 5px;
        }
        .hostname {
            font-family: monospace;
            color: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Docker Demo App</h1>
        <p>Dobrodošli na Docker demonstraciju!</p>
        <div class="counter">{{ counter }}</div>
        <p>Pregledi stranice u ovom kontejneru</p>
        <div class="info">
            <strong>Hostname Kontejnera:</strong> <span class="hostname">{{ hostname }}</span><br>
            <strong>Okruženje:</strong> {{ env }}
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    global counter
    counter += 1
    hostname = os.getenv('HOSTNAME', 'nepoznat')
    env = os.getenv('APP_ENV', 'produkcija')
    return render_template_string(
        HTML_TEMPLATE, 
        counter=counter,
        hostname=hostname,
        env=env
    )

@app.route('/health')
def health():
    return {'status': 'zdravo'}, 200

if __name__ == '__main__':
    print("🚀 Pokretanje Docker Demo App-a...")
    print(f"   Pokrenuto na: http://0.0.0.0:5000")
    print(f"   Okruženje: {os.getenv('APP_ENV', 'produkcija')}")
    app.run(host='0.0.0.0', port=5000, debug=False)
