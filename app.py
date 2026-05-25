from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML_CODE = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Turbo Sensi</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Poppins,sans-serif;
}

body{
    background:#000;
    overflow:hidden;
    color:white;
}

/* BACKGROUND */

.bg{
    position:fixed;
    width:100%;
    height:100%;
    z-index:-1;
}

.circle{
    position:absolute;
    border-radius:50%;
    background:rgba(255,0,0,0.08);
    animation:float 10s linear infinite;
}

.circle:nth-child(1){
    width:350px;
    height:350px;
    top:-100px;
    left:-100px;
}

.circle:nth-child(2){
    width:250px;
    height:250px;
    bottom:-80px;
    right:-80px;
}

@keyframes float{

    100%{
        transform:rotate(360deg);
    }

}

/* PARTICLES */

.particle{
    position:absolute;
    width:4px;
    height:4px;
    background:red;
    border-radius:50%;
    opacity:0.5;
    animation:particles 8s linear infinite;
}

@keyframes particles{

    from{
        transform:translateY(100vh);
    }

    to{
        transform:translateY(-100px);
    }

}

/* TOP BUTTONS */

.top-buttons{
    width:100%;
    display:flex;
    justify-content:space-between;
    padding:20px;
}

.top-btn{
    background:#ff0000;
    color:white;
    padding:12px 22px;
    border:none;
    border-radius:50px;
    font-weight:bold;

    box-shadow:
    0 0 20px #ff000088;
}

/* MAIN */

.main{
    width:100%;
    min-height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;

    padding:20px;
}

.logo{
    text-align:center;
    margin-bottom:30px;
}

.logo h1{
    font-size:55px;
    color:#ff0000;

    text-shadow:
    0 0 15px #ff0000,
    0 0 35px #ff0000;
}

.logo p{
    color:#888;
    margin-top:10px;
}

/* CARD */

.card{
    width:100%;
    max-width:430px;

    background:rgba(20,0,0,0.7);

    border-radius:25px;

    padding:30px;

    border:1px solid rgba(255,0,0,0.2);

    backdrop-filter:blur(10px);

    box-shadow:
    0 0 30px rgba(255,0,0,0.15);
}

/* INPUT */

.input-box{
    margin-bottom:20px;
}

.input-box label{
    display:block;
    margin-bottom:10px;
    color:#aaa;
    font-size:13px;
}

.input-box input,
.input-box select{

    width:100%;

    padding:18px;

    background:#140707;

    border:none;

    border-radius:15px;

    color:white;

    outline:none;

    border:1px solid #2d0000;
}

.input-box input:focus,
.input-box select:focus{

    border:1px solid red;

    box-shadow:
    0 0 15px rgba(255,0,0,0.4);

}

/* BUTTON */

.generate-btn{

    width:100%;

    padding:18px;

    border:none;

    border-radius:15px;

    background:
    linear-gradient(90deg,#ff0000,#ff2d2d);

    color:white;

    font-size:20px;

    font-weight:bold;

    cursor:pointer;

    transition:0.3s;
}

.generate-btn:hover{

    transform:scale(1.03);

    box-shadow:
    0 0 25px #ff0000;
}

/* RESULT */

.result{

    margin-top:25px;

    display:none;

    background:#120000;

    padding:20px;

    border-radius:20px;

    border:1px solid red;
}

.result h2{

    color:#00ff66;

    margin-bottom:15px;

    text-align:center;
}

.result p{

    margin:10px 0;

    color:#ddd;
}

/* MOBILE */

@media(max-width:500px){

.logo h1{
    font-size:40px;
}

.card{
    padding:20px;
}

}

</style>

</head>

<body>

<!-- BACKGROUND -->

<div class="bg">

<div class="circle"></div>
<div class="circle"></div>

</div>

<!-- TOP BUTTONS -->

<div class="top-buttons">

<button class="top-btn">
📢 JOIN TELEGRAM
</button>

<button class="top-btn">
🔥 PAID SENSI
</button>

</div>

<!-- MAIN -->

<div class="main">

<div class="logo">

<h1>TURBO SENSI</h1>

<p>Pro sensitivity generator for Free Fire MAX</p>

</div>

<div class="card">

<div class="input-box">

<label>PHONE MODEL NAME</label>

<input type="text"
id="device"
placeholder="e.g., IQOO Z9X 5G">

</div>

<div class="input-box">

<label>RAM</label>

<select id="ram">

<option>4GB</option>
<option>6GB</option>
<option>8GB</option>
<option>12GB</option>

</select>

</div>

<div class="input-box">

<label>PLAY STYLE</label>

<select id="style">

<option>HEADSHOT</option>
<option>ONE TAP</option>
<option>DRAG</option>
<option>NORMAL</option>

</select>

</div>

<button class="generate-btn"
onclick="generateSensi()">

GENERATE SENSITIVITY

</button>

<div class="result" id="result">

<h2>BEST SENSITIVITY</h2>

<p id="general"></p>
<p id="reddot"></p>
<p id="scope2x"></p>
<p id="scope4x"></p>
<p id="sniper"></p>
<p id="freelook"></p>

</div>

</div>

</div>

<script>

/* PARTICLES */

for(let i=0;i<40;i++){

let particle=document.createElement("div");

particle.classList.add("particle");

particle.style.left=Math.random()*100+"%";

particle.style.animationDuration=
(Math.random()*5+5)+"s";

document.body.appendChild(particle);

}

/* GENERATE */

function generateSensi(){

let device =
document.getElementById("device").value;

let ram =
document.getElementById("ram").value;

let style =
document.getElementById("style").value;

fetch('/generate',{

method:'POST',

headers:{
'Content-Type':'application/json'
},

body:JSON.stringify({

device:device,
ram:ram,
style:style

})

})

.then(response => response.json())

.then(data => {

document.getElementById("result").style.display="block";

document.getElementById("general").innerHTML =
"GENERAL : " + data.general;

document.getElementById("reddot").innerHTML =
"RED DOT : " + data.red_dot;

document.getElementById("scope2x").innerHTML =
"2X SCOPE : " + data.scope2x;

document.getElementById("scope4x").innerHTML =
"4X SCOPE : " + data.scope4x;

document.getElementById("sniper").innerHTML =
"SNIPER : " + data.sniper;

document.getElementById("freelook").innerHTML =
"FREE LOOK : " + data.free_look;

});

}

</script>

</body>
</html>

"""

# SMART SENSI LOGIC

def generate_best_sensi(device, ram, style):

    device = device.lower()

    general = 180
    red_dot = 185
    scope2x = 175
    scope4x = 165
    sniper = 130
    free_look = 190

    high_end = [
        "iphone",
        "rog",
        "iqoo",
        "oneplus",
        "s23",
        "s24",
        "redmagic",
        "realme gt",
        "pixel"
    ]

    mid_range = [
        "vivo",
        "oppo",
        "realme",
        "redmi",
        "poco",
        "narzo",
        "samsung"
    ]

    low_end = [
        "j2",
        "j5",
        "a03",
        "a10",
        "a20"
    ]

    # HIGH END

    if any(x in device for x in high_end):

        general = 200
        red_dot = 200
        scope2x = 190
        scope4x = 180
        sniper = 160
        free_look = 200

    # MID RANGE

    elif any(x in device for x in mid_range):

        general = 195
        red_dot = 190
        scope2x = 180
        scope4x = 170
        sniper = 145
        free_look = 195

    # LOW END

    elif any(x in device for x in low_end):

        general = 170
        red_dot = 160
        scope2x = 150
        scope4x = 140
        sniper = 120
        free_look = 170

    # RAM LOGIC

    if ram == "4GB":

        general -= 10
        red_dot -= 10

    elif ram == "8GB":

        general += 5
        red_dot += 5

    elif ram == "12GB":

        general += 10
        red_dot += 10

    # STYLE LOGIC

    if style == "HEADSHOT":

        general = 200
        red_dot = 200

    elif style == "DRAG":

        scope2x += 10
        scope4x += 10

    elif style == "ONE TAP":

        sniper += 20

    # LIMITS

    general = min(general, 200)
    red_dot = min(red_dot, 200)

    return {
        "general": general,
        "red_dot": red_dot,
        "scope2x": scope2x,
        "scope4x": scope4x,
        "sniper": sniper,
        "free_look": free_look
    }

@app.route('/')

def home():
    return render_template_string(HTML_CODE)

@app.route('/generate', methods=['POST'])

def generate():

    data = request.get_json()

    device = data['device']
    ram = data['ram']
    style = data['style']

    result = generate_best_sensi(
        device,
        ram,
        style
    )

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
