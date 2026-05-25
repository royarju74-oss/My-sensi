from flask import Flask, render_template_string

app = Flask(__name__)

UI_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gaming Panel</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins', sans-serif;
}

body{
    background:#050505;
    overflow:hidden;
    color:white;
}

/* Animated Background */

body::before{
    content:'';
    position:absolute;
    width:700px;
    height:700px;
    background:radial-gradient(circle,#ff000040,transparent 70%);
    top:-200px;
    left:-200px;
    animation:bgMove 8s linear infinite;
}

@keyframes bgMove{
    0%{
        transform:rotate(0deg);
    }
    100%{
        transform:rotate(360deg);
    }
}

/* Main Container */

.container{
    width:100%;
    height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;

    position:relative;
    z-index:1;
}

/* Gaming Panel */

.panel{
    width:400px;
    background:#0d0d0d;
    border:2px solid #ff0000;

    border-radius:20px;

    padding:25px;

    box-shadow:
    0 0 15px #ff0000,
    0 0 40px #ff000055;

    animation:panelEntry 1s ease;
}

@keyframes panelEntry{
    from{
        opacity:0;
        transform:translateY(40px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* Header */

.header{
    text-align:center;
    margin-bottom:20px;
}

.header h1{
    color:#ff0000;
    font-size:28px;
    letter-spacing:2px;

    text-shadow:
    0 0 10px #ff0000,
    0 0 20px #ff0000;

    animation:glow 2s infinite alternate;
}

@keyframes glow{
    from{
        text-shadow:0 0 10px #ff0000;
    }

    to{
        text-shadow:
        0 0 20px #ff0000,
        0 0 40px #ff0000;
    }
}

.header p{
    color:#999;
    font-size:12px;
    margin-top:5px;
}

/* Status Bar */

.status{
    background:#111;
    border:1px solid #ff0000;

    padding:10px;
    border-radius:10px;

    margin-bottom:20px;

    font-size:12px;

    color:#00ff66;

    animation:pulse 2s infinite;
}

@keyframes pulse{
    0%{
        box-shadow:0 0 5px #ff0000;
    }

    50%{
        box-shadow:0 0 20px #ff0000;
    }

    100%{
        box-shadow:0 0 5px #ff0000;
    }
}

/* Input Boxes */

.input-box{
    margin-bottom:15px;
}

.input-box label{
    display:block;
    margin-bottom:6px;
    color:#ff4444;
    font-size:13px;
}

.input-box input,
.input-box select{
    width:100%;

    padding:12px;

    border:none;
    outline:none;

    background:#141414;

    color:white;

    border-radius:10px;

    border:1px solid #333;

    transition:0.3s;
}

.input-box input:focus,
.input-box select:focus{

    border:1px solid #ff0000;

    box-shadow:
    0 0 10px #ff0000;
}

/* Stats Cards */

.stats{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;

    margin-top:20px;
}

.card{
    background:#111;
    padding:15px;

    border-radius:12px;

    text-align:center;

    border:1px solid #222;

    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);

    border:1px solid #ff0000;

    box-shadow:0 0 15px #ff0000;
}

.card h3{
    color:#ff0000;
    font-size:18px;
}

.card p{
    font-size:11px;
    color:#999;
}

/* Button */

.inject-btn{
    width:100%;
    padding:15px;

    margin-top:20px;

    border:none;
    border-radius:12px;

    background:linear-gradient(90deg,#ff0000,#ff5500);

    color:white;
    font-weight:bold;
    font-size:15px;

    cursor:pointer;

    transition:0.3s;
}

.inject-btn:hover{

    transform:scale(1.03);

    box-shadow:
    0 0 15px #ff0000,
    0 0 30px #ff0000;
}

.inject-btn:active{
    transform:scale(0.96);
}

/* Success Message */

.success{
    margin-top:15px;
    text-align:center;

    color:#00ff66;

    display:none;

    animation:successPop 0.6s ease;
}

@keyframes successPop{
    from{
        opacity:0;
        transform:scale(0.5);
    }

    to{
        opacity:1;
        transform:scale(1);
    }
}

</style>
</head>

<body>

<div class="container">

    <div class="panel">

        <div class="header">
            <h1>MY SENSI V4</h1>
            <p>Gaming Optimization Control Panel</p>
        </div>

        <div class="status" id="status">
            ● SYSTEM ONLINE | FPS BOOST READY
        </div>

        <div class="input-box">
            <label>DEVICE MODEL</label>
            <input type="text" placeholder="Enter Device Name">
        </div>

        <div class="input-box">
            <label>DPI LEVEL</label>
            <input type="text" placeholder="Enter DPI">
        </div>

        <div class="input-box">
            <label>FIRE BUTTON SIZE</label>
            <input type="text" placeholder="Enter Fire Button">
        </div>

        <div class="input-box">
            <label>BOOST MODE</label>
            <select>
                <option>ULTRA FPS BOOST</option>
                <option>BALANCED MODE</option>
                <option>EXTREME AIMLOCK</option>
            </select>
        </div>

        <div class="stats">

            <div class="card">
                <h3>90 FPS</h3>
                <p>Performance</p>
            </div>

            <div class="card">
                <h3>0 MS</h3>
                <p>Ping Boost</p>
            </div>

            <div class="card">
                <h3>HDR</h3>
                <p>Graphics</p>
            </div>

            <div class="card">
                <h3>99%</h3>
                <p>Accuracy</p>
            </div>

        </div>

        <button class="inject-btn" onclick="injectConfig()">
            INJECT CONFIG
        </button>

        <div class="success" id="success">
            CONFIG INJECTED SUCCESSFULLY ✅
        </div>

    </div>

</div>

<script>

function injectConfig(){

    document.getElementById("success").style.display = "block";

    document.getElementById("status").innerHTML =
    "● CONFIG ACTIVE | GAMING MODE ENABLED";

}

</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(UI_CODE)

if __name__ == '__main__':
    app.run(debug=True)
