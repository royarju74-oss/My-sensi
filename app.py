from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Enterprise Login + Generator Interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background: #0a0a0c; color: #00ffcc; font-family: 'Courier New', monospace; }
        .container { max-width: 500px; margin: 50px auto; padding: 20px; border: 1px solid #333; border-radius: 15px; background: #121215; }
        input, select { width: 100%; padding: 10px; margin: 10px 0; background: #1a1a1f; border: 1px solid #00ffcc; color: white; }
        button { width: 100%; padding: 15px; background: #00ffcc; color: black; font-weight: bold; cursor: pointer; border: none; }
    </style>
</head>
<body>
    <div class="container">
        {% if not logged_in %}
        <h2>ENTERPRISE LOGIN</h2>
        <form method="POST" action="/login">
            <input type="text" name="user" placeholder="Username" required>
            <input type="password" name="pass" placeholder="Access Key" required>
            <button type="submit">AUTHENTICATE</button>
        </form>
        {% else %}
        <h2>SENSI GENERATOR V3</h2>
        <input type="text" id="model" placeholder="Device Model (e.g. Realme 5 Pro)">
        <input type="text" id="dpi" placeholder="Custom DPI (e.g. 640)">
        <input type="text" id="fbs" placeholder="Fire Button Size">
        <select id="mode">
            <option>Low-End (Stable)</option>
            <option>High-End (Fast)</option>
        </select>
        <button onclick="alert('Injecting Config... Success!')">GENERATE CONFIG</button>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, logged_in=False)

@app.route('/login', methods=['POST'])
def login():
    # Basic logic: Agar user/pass sahi hai toh login
    return render_template_string(HTML_TEMPLATE, logged_in=True)

if __name__ == '__main__':
    app.run()
