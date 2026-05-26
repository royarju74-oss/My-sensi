from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>ULTRA AI SENSI</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Poppins,sans-serif;
}

body{
background:#050505;
overflow:hidden;
color:white;
}

/* BACKGROUND */

body::before{

content:'';

position:absolute;

width:700px;
height:700px;

background:
radial-gradient(circle,#ff000040,transparent 70%);

top:-200px;
left:-200px;

animation:bg 8s linear infinite;

}

@keyframes bg{

100%{
transform:rotate(360deg);
}

}

/* MAIN */

.main{

width:100%;
min-height:100vh;

display:flex;
justify-content:center;
align-items:center;

padding:20px;

}

/* PANEL */

.panel{

width:430px;

background:#0d0d0d;

border:2px solid #ff0000;

border-radius:25px;

padding:25px;

box-shadow:
0 0 20px #ff0000,
0 0 50px #ff000055;

backdrop-filter:blur(10px);

}

/* HEADER */

.header{
text-align:center;
margin-bottom:20px;
}

.header h1{

font-size:38px;
color:#ff0000;

text-shadow:
0 0 15px #ff0000;

}

.header p{

color:#888;
font-size:13px;

}

/* INPUT */

.input-box{

margin-bottom:18px;

}

.input-box label{

display:block;
margin-bottom:8px;

color:#ff4444;

font-size:13px;

}

.input-box input,
.input-box select{

width:100%;

padding:15px;

background:#111;

border:none;

outline:none;

color:white;

border-radius:12px;

border:1px solid #333;

font-size:15px;

}

.input-box input:focus,
.input-box select:focus{

border:1px solid red;

box-shadow:
0 0 10px red;

}

/* BUTTON */

.btn{

width:100%;

padding:16px;

border:none;

border-radius:14px;

background:
linear-gradient(90deg,#ff0000,#ff5500);

color:white;

font-size:17px;
font-weight:bold;

cursor:pointer;

transition:0.3s;

}

.btn:hover{

transform:scale(1.03);

box-shadow:
0 0 20px red;

}

/* RESULT */

.result{

margin-top:20px;

background:#111;

padding:20px;

border-radius:15px;

display:none;

border:1px solid red;

animation:show 0.5s ease;

}

@keyframes show{

from{
opacity:0;
transform:translateY(20px);
}

to{
opacity:1;
transform:translateY(0);
}

}

.result h2{

color:#00ff66;

margin-bottom:15px;

text-align:center;

}

.result p{

margin:8px 0;

color:#ddd;

font-size:14px;

}

/* BADGE */

.badge{

margin-top:15px;

padding:12px;

border-radius:12px;

background:red;

text-align:center;

font-weight:bold;

}

/* MOBILE */

@media(max-width:500px){

.panel{
width:100%;
}

.header h1{
font-size:30px;
}

}

</style>

</head>

<body>

<div class="main">

<div class="panel">

<div class="header">

<h1>ULTRA AI SENSI</h1>

<p>Smart Free Fire Sensitivity Generator</p>

</div>

<div class="input-box">

<label>MOBILE NAME</label>

<input type="text"
id="device"
placeholder="e.g. IQOO Z9X">

</div>

<div class="input-box">

<label>RAM</label>

<select id="ram">

<option>2GB</option>
<option>3GB</option>
<option>4GB</option>
<option>6GB</option>
<option>8GB</option>
<option>12GB</option>
<option>16GB</option>

</select>

</div>

<div class="input-box">

<label>DPI LEVEL</label>

<input type="number"
id="dpi"
placeholder="e.g. 650">

</div>

<div class="input-box">

<label>GAMEPLAY STYLE</label>

<select id="style">

<option>ACCURACY+</option>

<option>DRAG HEADSHOT</option>

<option>FREE STYLE</option>

<option>ONE TAP</option>

<option>SNIPER PRO</option>

<option>AIMLOCK</option>

<option>BALANCED</option>

</select>

</div>

<button class="btn"
onclick="generateSensi()">

GENERATE AI SENSI

</button>

<div class="result" id="result">

<h2>BEST SENSITIVITY</h2>

<p id="general"></p>
<p id="red"></p>
<p id="scope2x"></p>
<p id="scope4x"></p>
<p id="sniper"></p>
<p id="free"></p>
<p id="dpiresult"></p>
<p id="aimode"></p>

<div class="badge"
id="badge">

DEVICE TYPE

</div>

</div>

</div>

</div>

<script>

async function generateSensi(){

let device =
document.getElementById("device").value;

let ram =
document.getElementById("ram").value;

let dpi =
document.getElementById("dpi").value;

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
dpi:dpi,
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

document.getElementById("sniper").innerHTML =
"SNIPER : " + data.sniper;

document.getElementById("free").innerHTML =
"FREE LOOK : " + data.free_look;

document.getElementById("dpiresult").innerHTML =
"DPI : " + data.dpi;

document.getElementById("aimode").innerHTML =
"AI MODE : " + data.ai_mode;

document.getElementById("badge").innerHTML =
data.device_type;

}

</script>

</body>
</html>

"""

# AI SYSTEM

def generate_best_sensi(device, ram, dpi, style):

    device = device.lower()

    dpi = int(dpi)

    general = 180
    red_dot = 180
    scope2x = 170
    scope4x = 160
    sniper = 120
    free_look = 190

    device_type = "MID RANGE"

    ai_mode = "BALANCED AI"

    # DEVICE DETECTION

    high_end = [
        "iphone",
        "rog",
        "iqoo",
        "oneplus",
        "s24",
        "redmagic",
        "pixel"
    ]

    low_end = [
        "j2",
        "j5",
        "a03",
        "c11",
        "c21"
    ]

    if any(x in device for x in high_end):

        device_type = "HIGH END"

        general = 200
        red_dot = 200
        scope2x = 190
        scope4x = 180
        sniper = 160
        free_look = 200

        ai_mode = "ULTRA AI"

    elif any(x in device for x in low_end):

        device_type = "LOW END"

        general = 165
        red_dot = 155
        scope2x = 145
        scope4x = 135
        sniper = 110
        free_look = 165

        ai_mode = "LITE AI"

    # RAM BOOST

    if ram == "2GB":

        general -= 20

    elif ram == "4GB":

        general -= 10

    elif ram == "8GB":

        general += 5

    elif ram == "12GB":

        general += 10

    elif ram == "16GB":

        general += 15

    # DPI BOOST

    if dpi >= 700:

        general += 10
        red_dot += 10

    elif dpi <= 300:

        general -= 10

    # GAMEPLAY STYLE AI

    if style == "ACCURACY+":

        general += 5
        red_dot += 15
        scope2x += 10

        ai_mode = "ACCURACY AI"

    elif style == "DRAG HEADSHOT":

        general = 200
        red_dot = 200
        scope2x += 12
        scope4x += 10

        ai_mode = "DRAG AI"

    elif style == "FREE STYLE":

        free_look = 200
        general += 8

        ai_mode = "FREESTYLE AI"

    elif style == "ONE TAP":

        sniper += 25
        red_dot += 8

        ai_mode = "ONE TAP AI"

    elif style == "SNIPER PRO":

        sniper = 200
        scope4x += 15

        ai_mode = "SNIPER AI"

    elif style == "AIMLOCK":

        general = 200
        red_dot = 200
        scope2x = 195

        ai_mode = "AIMLOCK AI"

    elif style == "BALANCED":

        ai_mode = "BALANCED AI"

    # LIMIT

    general = max(100,min(general,200))
    red_dot = max(100,min(red_dot,200))
    scope2x = max(100,min(scope2x,200))
    scope4x = max(100,min(scope4x,200))
    sniper = max(80,min(sniper,200))
    free_look = max(100,min(free_look,200))

    return {

        "general":general,
        "red_dot":red_dot,
        "scope2x":scope2x,
        "scope4x":scope4x,
        "sniper":sniper,
        "free_look":free_look,
        "dpi":dpi,
        "ai_mode":ai_mode,
        "device_type":device_type

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
        data['dpi'],
        data['style']

    )

    return jsonify(result)

if __name__ == '__main__':

    app.run(debug=True)
