from flask import Flask, jsonify
from datetime import datetime
import platform, socket

app = Flask(__name__)

START_TIME = datetime.now()

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Lab 🚀</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .card {
            background: rgba(255,255,255,0.07);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 24px;
            padding: 48px 56px;
            max-width: 600px;
            width: 90%;
            text-align: center;
            box-shadow: 0 25px 50px rgba(0,0,0,0.4);
        }
        .emoji { font-size: 64px; margin-bottom: 16px; }
        h1 { font-size: 2.4rem; font-weight: 700; margin-bottom: 8px; }
        .subtitle {
            color: rgba(255,255,255,0.6);
            font-size: 1rem;
            margin-bottom: 36px;
        }
        .badges {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-bottom: 36px;
        }
        .badge {
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 999px;
            padding: 6px 16px;
            font-size: 0.82rem;
            font-weight: 500;
        }
        .badge.green { background: rgba(52,211,153,0.2); border-color: #34d399; color: #34d399; }
        .badge.blue  { background: rgba(96,165,250,0.2); border-color: #60a5fa; color: #60a5fa; }
        .badge.pink  { background: rgba(244,114,182,0.2); border-color: #f472b6; color: #f472b6; }
        .routes {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 32px;
        }
        .route {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 14px;
            text-decoration: none;
            color: white;
            transition: all 0.2s;
        }
        .route:hover {
            background: rgba(255,255,255,0.13);
            transform: translateY(-2px);
        }
        .route .method {
            font-size: 0.7rem;
            font-weight: 700;
            color: #34d399;
            letter-spacing: 1px;
            margin-bottom: 4px;
        }
        .route .path { font-size: 0.95rem; font-weight: 600; }
        .route .desc { font-size: 0.75rem; color: rgba(255,255,255,0.5); margin-top: 2px; }
        .footer { font-size: 0.78rem; color: rgba(255,255,255,0.35); margin-top: 8px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="emoji">☁️</div>
        <h1>Cloud Lab</h1>
        <p class="subtitle">Aplicație Python Flask deployată cu Docker, Kubernetes și Google Cloud CI/CD</p>
        <div class="badges">
            <span class="badge green">● Running</span>
            <span class="badge blue">Python Flask</span>
            <span class="badge blue">Docker</span>
            <span class="badge blue">Kubernetes</span>
            <span class="badge pink">Google Cloud Run</span>
        </div>
        <div class="routes">
            <a href="/health" class="route">
                <div class="method">GET</div>
                <div class="path">/health</div>
                <div class="desc">Status aplicație</div>
            </a>
            <a href="/info" class="route">
                <div class="method">GET</div>
                <div class="path">/info</div>
                <div class="desc">Info sistem</div>
            </a>
            <a href="/time" class="route">
                <div class="method">GET</div>
                <div class="path">/time</div>
                <div class="desc">Data și ora curentă</div>
            </a>
            <a href="/echo?msg=salut" class="route">
                <div class="method">GET</div>
                <div class="path">/echo</div>
                <div class="desc">Echo mesaj (?msg=)</div>
            </a>
        </div>
        <div class="footer">UTM · Facultatea FCIM · Aplicații Cloud · 2026</div>
    </div>
</body>
</html>
'''

@app.route('/health')
def health():
    uptime = str(datetime.now() - START_TIME).split('.')[0]
    return jsonify({
        'status': 'ok',
        'uptime': uptime,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/info')
def info():
    return jsonify({
        'app': 'Cloud Lab',
        'version': '2.0',
        'python': platform.python_version(),
        'platform': platform.system(),
        'hostname': socket.gethostname(),
        'stack': ['Python', 'Flask', 'Docker', 'Kubernetes', 'Google Cloud Run']
    })

@app.route('/time')
def current_time():
    now = datetime.now()
    return jsonify({
        'date': now.strftime('%d.%m.%Y'),
        'time': now.strftime('%H:%M:%S'),
        'iso': now.isoformat(),
        'weekday': now.strftime('%A')
    })

@app.route('/echo')
def echo():
    from flask import request
    msg = request.args.get('msg', 'Hello from Cloud Lab! 🚀')
    return jsonify({
        'echo': msg,
        'length': len(msg),
        'upper': msg.upper()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)