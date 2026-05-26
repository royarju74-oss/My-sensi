from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>AI SENSI</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Poppins,sans-serif;
}

body{

background:
linear-gradient(135deg,#050505,#120000,#1a0000);

height:100vh;

overflow:hidden;

display:flex;
justify-content:center;
align-items:center;

color:white;

}

/* ANIMATED GLOW */

body::before{

content:'';

position:absolute;

width:700px;
height:700px;

background:
radial-gradient(circle,#ff000055,transparent 70%);

top:-250px;
left:-250px;

animation:rotate 10s linear infinite;

}

@keyframes rotate{

100%{
transform:rotate(360deg);
}

}

/* MAIN BOX */

.container{

width:100%;
max-width:420px;

padding:20px;

}

/* START SCREEN */

.start-screen{

background:
rgba(15,15,15,0.8);

backdrop-filter:blur(10px);

border:1px solid rgba(255,0,0,0.3);

padding:35px;

border-radius:30px;

text-align:center;

box-shadow:
0 0 30px rgba(255,0,0,0.2);

animation:pop 1s ease;

}

@keyframes pop{

from{
transform:scale(0.8);
opacity:0;
}

to{
transform:scale(1);
opacity:1;
}

}

.logo{

font-size:45px;
font-weight:bold;

color:#ff1a1a;

text-shadow:
0 0 20px red;

margin-bottom:10px;

}

.subtitle{

color:#aaa;
margin-bottom:30px;

font-size:14px;

}

/* BUTTON */

.start-btn,
.generate-btn{

width:100%;

padding:16px;

border:none;

border-radius:18px;

background:
linear-gradient(90deg,#ff0000,#ff4d4d);

color:white;

font-size:17px;
font-weight:bold;

cursor:pointer;

transition:0.3s;

}

.start-btn:hover,
.generate-btn:hover{

transform:scale(1.04);

box-shadow:
0 0 20px red;

}

/* PANEL */

.panel{

display:none;

background:
rgba(15,15,15,0.88);

backdrop-filter:blur(12px);

border:1px solid rgba(255,0,0,0.3);

padding:30px;

border-radius:30px;

box-shadow:
0 0 35px rgba(255,0,0,0.2);

animation:slide 0.6s ease;

}

@keyframes slide{

from{
opacity:0;
transform:translateY(30px);
}

to{
opacity:1;
transform:translateY(0);
}

}

/* INPUT */

.input-box{

margin-bottom:18px;

}

.input-box label{

display:block;

margin-bottom:8px;

font-size:13px;

color:#ff6666;

}

.input-box input,
.input-box select{

width:100%;

padding:16px;

border:none;

outline:none;

border-radius:16px;

background:#111;

color:white;

font-size:15px;

border:1px solid #333;

transition:0.3s;

}

.input-box input:focus,
.input-box select:focus{

border:1px solid red;

box-shadow:
0 0 15px rgba(255,0,0,0.5);

}

/* RESULT */

.result{

margin-top:20px;

display:none;

background:#111;

padding:20px;

border-radius:20px;

border:1px solid red;

animation:fade 0.5s ease;

}

@keyframes fade{

from{
opacity:0;
}

to{
opacity:1;
}

}

.result h2{

text-align:center;

margin-bottom:15px;

color:#00ff88;

}

.result p{

margin:10px 0;

font-size:15px;

color:#ddd;

}

/* BADGE */

.badge{

margin-top:15px;

padding:12px;

border-radius:14px;

text-align:center;

font-weight:bold;

background:
linear-gradient(90deg,#ff0000,#ff4d4d);

}

/* MOBILE */

@media(max-width:500px){

.logo{
font-size:35px;
}

}

</style>

</head>

<body>

<div class="container">

<!-- START SCREEN -->

<div class="start-screen"
id="startScreen">

<div class="logo">
AI SENSI
</div>

<div class="subtitle">
Ultra Smart Free Fire Generator
</div>

<button class="start-btn"
onclick="openPanel()">

OPEN GENERATOR

</button>

</div>

<!-- PANEL -->

<div class="panel"
id="panel">

<div class="input-box">

<label>MOBILE NAME</label>

<input type="text"
id="device"
placeholder="e.g. IQOO Z9X">

</div>

<div class="input-box">

<label>RAM</label>

<select id="ram">

<option>4GB</option>
<option>6GB</option>
<option>8GB</option>

</select>

</div>

<div class="input-box">

<label>GAMEPLAY STYLE</label>

<select id="style">

<option>DRAG HEADSHOT</option>

<option>SMOOTH AIM</option>

<option>AIMLOCK</option>

</select>

</div>

<button class="generate-btn"
onclick="generateSensi()">

GENERATE

</button>

<div class="result"
id="result">

<h2>BEST SETTINGS</h2>

<p id="general"></p>
<p id="red"></p>
<p id="scope2x"></p>
<p id="scope4x"></p>
<p id="fire"></p>
<p id="dpi"></p>

<div class="badge"
id="badge">

AI MODE

</div>

</div>

</div>

</div>

<script>

function openPanel(){

document.getElementById("startScreen").style.display =
"none";

document.getElementById("panel").style.display =
"block";

}

async function generateSensi(){

let device =
document.getElementById("device").value;

let ram =
document.getElementById("ram").value;

let style =
document.getElementById("style").value;

let response = await fetch('/generate',{

method:'POST',

headers:{
'Content-Type':'application/json'
},

body:JSON.stringify({

device:device,
ram:ram,
style:style

})

});

let data = await response.json();

document.getElementById("result").style.display =
"block";

document.getElementById("general").innerHTML =
"GENERAL : " + data.general;

document.getElementById("red").innerHTML =
"RED DOT : " + data.red_dot;

document.getElementById("scope2x").innerHTML =
"2X SCOPE : " + data.scope2x;

document.getElementById("scope4x").innerHTML =
"4X SCOPE : " + data.scope4x;

document.getElementById("fire").innerHTML =
"FIRE BUTTON : " + data.fire_button;

document.getElementById("dpi").innerHTML =
"DPI : " + data.dpi;

document.getElementById("badge").innerHTML =
data.ai_mode;

}

</script>

</body>
</html>

"""

# AI LOGIC

def generate_best_sensi(device, ram, style):

    device = device.lower()

    general = 180
    red_dot = 185
    scope2x = 175
    scope4x = 165
    fire_button = 55
    dpi = 650

    ai_mode = "BALANCED AI"

    # DEVICE DETECTION

    high_end = [
        "iphone",
        "iqoo",
        "rog",
        "oneplus",
        "redmagic"
    ]

    low_end = [
        "j2",
        "a03",
        "c11"
    ]

    # HIGH END

    if any(x in device for x in high_end):

        general = 200
        red_dot = 200
        scope2x = 190
        scope4x = 180
        fire_button = 48
        dpi = 720

        ai_mode = "ULTRA AI"

    # LOW END

    elif any(x in device for x in low_end):

        general = 165
        red_dot = 155
        scope2x = 145
        scope4x = 135
        fire_button = 65
        dpi = 520

        ai_mode = "LITE AI"

    # RAM BOOST

    if ram == "4GB":

        general -= 5

    elif ram == "8GB":

        general += 5

    # GAMEPLAY STYLE

    if style == "DRAG HEADSHOT":

        general = 200
        red_dot = 200
        scope2x += 15
        fire_button = 50

        ai_mode = "DRAG AI"

    elif style == "SMOOTH AIM":

        general += 8
        red_dot += 10
        fire_button = 54

        ai_mode = "SMOOTH AIM AI"

    elif style == "AIMLOCK":

        general = 200
        red_dot = 200
        scope2x = 195
        fire_button = 42

        ai_mode = "AIMLOCK AI"

    return {

        "general":general,
        "red_dot":red_dot,
        "scope2x":scope2x,
        "scope4x":scope4x,
        "fire_button":fire_button,
        "dpi":dpi,
        "ai_mode":ai_mode

    }

@app.route('/')

def home():

    return render_template_string(HTML)

@app.route('/generate', methods=['POST'])

def generate():

    data = request.get_json()

    result = generate_best_sensi(

        data['device'],
        data['ram'],
        data['style']

    )

    return jsonify(result)

if __name__ == '__main__':

    app.run(debug=True)
