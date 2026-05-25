from flask import Flask, render_template_string

app = Flask(__name__)

# CSS ko humne clean aur dark kar diya hai taaki white box na aaye
UI_CODE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background: #050505; color: #ff0000; font-family: 'Courier New', monospace; padding: 20px; margin: 0; }
        .dashboard { border: 1px solid #ff0000; padding: 20px; border-radius: 10px; background: #110000; box-shadow: 0 0 10px #ff0000; }
        .data-panel { border: 1px solid #ff0000; padding: 10px; margin: 10px 0; font-size: 12px; color: #ff0000; }
        input, select { background: #000; border: 1px solid #ff0000; color: #ff0000; padding: 10px; width: 100%; margin: 5px 0; box-sizing: border-box; }
        button { background: #ff0000; color: #fff; padding: 15px; border: none; width: 100%; font-weight: bold; cursor: pointer; margin-top: 10px; }
        /* White box ko hatane ke liye naya style */
        .success-msg { color: #ff0000; font-weight: bold; text-align: center; margin-top: 10px; display: none; }
    </style>
</head>
<body>
    <div class="dashboard">
        <h2 style="text-align:center;">WLC to MY SENSI V3</h2>
        <div class="data-panel" id="status">STATUS: READY | SERVER: ACTIVE</div>
        <input type="text" id="model" placeholder="Device Model">
        <input type="text" id="dpi" placeholder="DPI">
        <input type="text" id="btn" placeholder="Fire Button">
        <select>
            <option>High-End (Fast)</option>
        </select>
        <button onclick="showSuccess()">INJECT SENSITIVITY V3</button>
        <div id="success" class="success-msg">CONFIG INJECTED SUCCESSFULLY!</div>
    </div>
    <script>
        function showSuccess() {
            // Alert ki jagah hum website ke andar hi text dikhayenge
            document.getElementById('success').style.display = 'block';
            document.getElementById('status').innerText = "STATUS: INJECTED ✅";
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(UI_CODE)

if __name__ == '__main__':
    app.run()
