from flask import Flask, render_template_string

app = Flask(__name__)

# Sirf Direct Generator Interface
UI_CODE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background: #050505; color: #ff0000; font-family: 'Courier New', monospace; padding: 20px; }
        .dashboard { border: 1px solid #ff0000; padding: 20px; border-radius: 10px; background: #110000; box-shadow: 0 0 15px #ff0000; }
        .data-panel { border: 1px solid #ff0000; padding: 10px; margin: 10px 0; font-size: 12px; }
        input, select { background: #000; border: 1px solid #ff0000; color: #ff0000; padding: 10px; width: 100%; margin: 5px 0; }
        button { background: #ff0000; color: #fff; padding: 15px; border: none; width: 100%; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="dashboard">
        <h2 style="text-align:center;">WLC to MY SENSI V3</h2>
        <div class="data-panel">
            STATUS: READY | SERVER: ACTIVE
        </div>
        <input type="text" placeholder="Device Model">
        <input type="text" placeholder="DPI">
        <input type="text" placeholder="Fire Button">
        <select>
            <option>High-End (Fast)</option>
        </select>
        <button onclick="alert('Injecting Config... Success!')">INJECT SENSITIVITY V3</button>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(UI_CODE)

if __name__ == '__main__':
    app.run()
    
