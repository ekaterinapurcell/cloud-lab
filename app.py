from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Cloud Lab 🚀</h1>
    <p>Aplicație deployată cu Docker, Kubernetes și Google Cloud CI/CD.</p>
    <ul>
      <li>Framework: Python Flask</li>
      <li>Container: Docker</li>
      <li>Orchestrare: Kubernetes</li>
      <li>CI/CD: Google Cloud Build → Cloud Run</li>
    </ul>
    '''

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)