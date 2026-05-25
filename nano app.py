
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PREMIUM REGEDIT SENSITIVITY V3</title>
    <style>
        body { background-color: #060608; color: #ffffff; font-family: sans-serif; padding: 20px; }
        .header { background: linear-gradient(135deg, #1f005c, #5b0eeb); padding: 15px; text-align: center; border-radius: 10px; }
        h1 { margin: 0; font-size: 24px; text-transform: uppercase; }
        .setup-box { background: #0f0f14; border: 2px solid #333; padding: 20px; border-radius: 10px; margin-top: 20px; }
        .form-group { margin-bottom: 18px; }
        label { display: block; font-size: 13px; color: #00ffcc; margin-bottom: 5px; }
        input, select { width: 100%; padding: 12px; background: #1a1a1f; border: 1px solid #333; color: #fff; border-radius: 5px; }
        .gen-btn { width: 100%; background: linear-gradient(90deg, #00ffcc, #0088ff); color: #000; font-weight: bold; border: none; padding: 15px; border-radius: 5px; cursor: pointer; }
        .loading-container { display: none; margin-top: 20px; }
        .progress-bar { width: 100%; background: #171721; height: 10px; border-radius: 5px; }
        .progress-fill { height: 100%; background: linear-gradient(90deg, #00ffcc, #0088ff); width: 0%; border-radius: 5px; transition: width 0.5s; }
        .result-box { background: #0f0f14; border: 2px solid #00ffcc; padding: 15px; border-radius: 10px; margin-top: 20px; display: none; }
        .stat { display: flex; justify-content: space-between; margin: 10px 0; border-left: 3px solid #00ffcc; padding-left: 10px; }
        .val { color: #fff; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <h1>REGEDIT SENSITIVITY V3</h1>
        <p>AUTOMATED LOW / HIGH END SENSITIVITY OPTIMIZER</p>
    </div>
    <div class="setup-box">
        <div class="form-group">
            <label>Device Model Name</label>
            <input type="text" id="modelInput" placeholder="e.g., POCO X3, iPhone 14">
        </div>
        <div class="form-group">
            <label>Sensitivity Target Mode</label>
            <select id="modeInput">
                <option value="low_sens">Low-End Sensitivity (Anti-Lag / Zero Recoil)</option>
                <option value="stable" selected>Stable Smooth Mode (Perfect Balance)</option>
                <option value="high_sens">High-End Sensitivity (Super Fast Drag)</option>
            </select>
        </div>
        <button class="gen-btn" onclick="startLoading()">Inject Config Codes ⚡</button>
    </div>
    <div class="loading-container" id="loadingContainer">
        <div id="loadingText">Connecting to Database...</div>
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    </div>
    <div class="result-box" id="resultContainer">
        <h2>✅ REGEDIT INJECTION SUCCESSFUL</h2>
        <div id="DEVICE"></div>
        <div class="stat"><span>General Sensitivity:</span><span class="val" id="resGeneral"></span></div>
        <div class="stat"><span>Red Dot Sensitivity:</span><span class="val" id="resRedDot"></span></div>
        <div class="stat"><span>2X Scope Sensitivity:</span><span class="val" id="res2X"></span></div>
        <div class="stat"><span>4X Scope Sensitivity:</span><span class="val" id="res4X"></span></div>
        <div class="stat"><span>DPI Layout Settings:</span><span class="val" id="resDpi"></span></div>
    </div>
    <script>
        function getRandomValue(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
        function startLoading() {
            document.getElementById('loadingContainer').style.display = 'block';
            let fill = document.getElementById('progressFill');
            let width = 0;
            let interval = setInterval(() => {
                if (width >= 100) { clearInterval(interval); showResults(); }
                else { width += 5; fill.style.width = width + '%'; }
            }, 50);
        }
        function showResults() {
            document.getElementById('loadingContainer').style.display = 'none';
            document.getElementById('resultContainer').style.display = 'block';
            document.getElementById('DEVICE').innerText = document.getElementById('modelInput').value.toUpperCase();
            document.getElementById('resGeneral').innerText = getRandomValue(90, 100);
            document.getElementById('resRedDot').innerText = getRandomValue(85, 95);
            document.getElementById('res2X').innerText = getRandomValue(80, 90);
            document.getElementById('res4X').innerText = getRandomValue(75, 85);
            document.getElementById('resDpi').innerText = "Default (400-500)";
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
