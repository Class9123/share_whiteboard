account_html='''
<!DOCTYPE html>
<html>
<head>
	<title>Slide Navbar</title>
	<link rel="stylesheet" type="text/css" href="slide navbar style.css">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@500&display=swap" rel="stylesheet">

<style>
  body{
	margin: 0;
	padding: 0;
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: 100vh;
	font-family: 'Jost', sans-serif;
	background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e);
}
.main{
	width: 350px;
	height: 500px;
	background: red;
	overflow: hidden;
	background: url("https://doc-08-2c-docs.googleusercontent.com/docs/securesc/68c90smiglihng9534mvqmq1946dmis5/fo0picsp1nhiucmc0l25s29respgpr4j/1631524275000/03522360960922298374/03522360960922298374/1Sx0jhdpEpnNIydS4rnN4kHSJtU1EyWka?e=view&authuser=0&nonce=gcrocepgbb17m&user=03522360960922298374&hash=tfhgbs86ka6divo3llbvp93mg4csvb38") no-repeat center/ cover;
	border-radius: 10px;
	box-shadow: 5px 20px 50px #000;
}
#chk{
	display: none;
}
.signup{
	position: relative;
	width:100%;
	height: 100%;
}
label{
	color: #fff;
	font-size: 2.3em;
	justify-content: center;
	display: flex;
	margin: 50px;
	font-weight: bold;
	cursor: pointer;
	transition: .5s ease-in-out;
}
input{
	width: 60%;
	height: 10px;
	background: #e0dede;
	justify-content: center;
	display: flex;
	margin: 20px auto;
	padding: 12px;
	border: none;
	outline: none;
	border-radius: 5px;
}
button{
	width: 60%;
	height: 40px;
	margin: 10px auto;
	justify-content: center;
	display: block;
	color: #fff;
	background: #573b8a;
	font-size: 1em;
	font-weight: bold;
	margin-top: 30px;
	outline: none;
	border: none;
	border-radius: 5px;
	transition: .2s ease-in;
	cursor: pointer;
}
button:hover{
	background: #6d44b8;
}
.login{
	height: 460px;
	background: #eee;
	border-radius: 60% / 10%;
	transform: translateY(-180px);
	transition: .8s ease-in-out;
}
.login label{
	color: #573b8a;
	transform: scale(.6);
}

#chk:checked ~ .login{
	transform: translateY(-500px);
}
#chk:checked ~ .login label{
	transform: scale(1);	
}
#chk:checked ~ .signup label{
	transform: scale(.6);
}

</style>
</head>
<body>
	<div class="main">  	
		<input type="checkbox" id="chk" aria-hidden="true">

			<div class="signup">
				<form>
					<label for="chk" aria-hidden="true">Sign up</label>
					<input type="text" name="name" placeholder="User name" required="">
					<input type="email" name="email" placeholder="Email" name="email" required="">
					<input type="password" name="pswd" placeholder="Password" name="password" required="">
					<button>Sign up</button>
				</form>
			</div>

			<div class="login">
				<form>
					<label for="chk" aria-hidden="true">Login</label>
					<input type="email" name="email" placeholder="Email" required="">
					<input type="password" name="pswd" placeholder="Password" required="">
					<button>Login</button>
				</form>
			</div>
	</div>
</body>
</html>
'''
html='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
  <style>
    *:focus {
      outline: none;
    }

    html, body {
      overflow: hidden;
      margin: 0;
      padding: 0;
    }

    h2 {
      font-family: 'Pacifico';
    }

    main {
      width: 100vw;
      height: 100vh;
    }

    #canvas {}

    #tools {
      width: 100%;
      height: 50px;
      overflow-x: auto;
      overflow-y: hidden;
      background-color: #DDD;
      display: flex;
      position: absolute;
      bottom: 0;
      left: 0;
    }

    .tool, .option {
      width: 50px;
      height: 50px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
    }

    .tool, .option > i {
      font-size: 1.5em;
    }

    .tool-selected {
      background-color: #555;
      color: white;
    }

    .pane {
      position: absolute;
      top: 100%;
      height: 50vh;
      width: 100%;
      max-width: 500px;
      left: 0%;
      background-color: #EEE;
      transition: top .3s ease;
    }
    .open {
      top: 50% !important;
    }

    .picker-titlebar {
      width: 100%;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .picker-titlebar > h2 {
      margin-left: auto;
    }

    .close-picker {
      font-size: 2em;
      cursor: pointer;
      display: inline-block;
      margin-left: auto;
      margin-right: 10px;
    }

    #sliders-wrapper {
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 5fr;
      grid-row-gap: 20px;
    }

    #sliders-wrapper > input {
      box-sizing: border-box;
      margin-right: 20px;
    }
    #sliders-wrapper > span {
      font-weight: 900;
      font-family: 'Pacifico';
      text-align: center;
    }
    </style>
  </head>
  <body>
    <main>
      <div id="canvas"></div>
      <div id="tools">
        <div class="tool tool-selected">
          <i class="fas fa-paint-brush"></i>
        </div>

        <div class="tool">
          <i class="fas fa-eraser"></i>
        </div>

        <div class="option" id="size-selector">
          <i class="fas fa-sliders-h"></i>
        </div>
        <div class="option" id="color-selector"></div>
      </div>
    </main>

    <div id="color-picker" class="pane">
      <div class="picker-titlebar">
        <h2>Choose a color</h2>
        <i class="fas fa-times close-picker" id="close-color-picker"></i>
      </div>
      <div id="sliders-wrapper">
        <span>R</span>
        <input type="range" class="color-range" value="50" min="0" max="255">
        <span>G</span>
        <input type="range" class="color-range" value="50" min="0" max="255">
        <span>B</span>
        <input type="range" class="color-range" value="60" min="0" max="255">
      </div>
    </div>

    <div id="size-picker" class="pane">
      <div class="picker-titlebar">
        <h2>Settings</h2>
        <i class="fas fa-times close-picker" id="close-size-picker"></i>
      </div>
      <div id="sliders-wrapper">
        <span>Radius</span>
        <input type="range" value="20" min="0" max="255" id="radius-range">
      </div>
    </div>
  </body>
  <script src="https://cdn.socket.io/4.4.1/socket.io.min.js"></script>
  <script>
    /*** GUI Part ***/
    const socket = io();
    let tool = 0;
    const tools = document.querySelectorAll(".tool");
    let drawColor = null;
    let radius = 50;
    let candraw=true;
    setColor([50, 50, 60]);
    
    socket.on("draw_data",function(data){
     // tool: tool,
    //  drawColor: drawColor,
   //   radius: radius,
    //  mouseX: mouseX,
     // mouseY: mouseY,
    //  lastPoint: lastPoint,
     
      let tool=data.tool
      let drawColor=data.drawColor
      let radius=data.radius
      let mouseX=data.mouseX
      let mouseY=data.mouseY
      let lastPoint=data.lastPoint
      
      if (lastPoint == null) lastPoint = [mouseX,
          mouseY];

        if (tool === 0) {
          graphic.noFill();
          graphic.stroke(drawColor);
          graphic.strokeWeight(radius);
          graphic.line(mouseX, mouseY, lastPoint[0], lastPoint[1]);
        }

        if (tool === 1) {
          graphic.noFill();
          graphic.stroke(255);
          graphic.strokeWeight(radius);
          graphic.line(mouseX, mouseY, lastPoint[0], lastPoint[1]);
        }

        lastPoint = [mouseX,
          mouseY];
    })
    
    tools.forEach((toolElem, index) => {
      toolElem.onclick = () => setTool(index);
    });

    function setTool(id) {
      tool = id;
      tools.forEach((toolElem, index) => {
        toolElem.classList.toggle("tool-selected", id === index);
      });
    }

    function setColor(c) {
      drawColor = c;
      const colorString = `rgb(${drawColor.join(",")})`;
      document.querySelector('#color-selector').style.backgroundColor = colorString;
      document.querySelector('#color-picker').style.backgroundColor = colorString;
      document.querySelector('#color-picker').style.color = (drawColor.reduce((a, b) => a + b) / 3 < 122) ? 'white': 'black';
    }

    document.onwheel = (e) => {
      radius += (e.deltaY < 0) ? 2: -2;
    };

    document.querySelector("#color-selector").onclick = () => {
      document.querySelector("#color-picker").classList.add("open");
    };

    document.querySelector("#close-color-picker").onclick = () => {
      document.querySelector("#color-picker").classList.remove("open");
    };

    document.querySelector("#size-selector").onclick = () => {
      document.querySelector("#size-picker").classList.add("open");
    };

    document.querySelector("#close-size-picker").onclick = () => {
      document.querySelector("#size-picker").classList.remove("open");
    };

    document.querySelectorAll(".color-range").forEach(range => {
      range.oninput = refreshColorPicker;
    });

    document.querySelector("#radius-range").oninput = refreshRadius;

    function refreshColorPicker() {
      const n = Array.from(document.querySelectorAll(".color-range")).map(range => parseInt(range.value));
      setColor(n);
    }

    function refreshRadius() {
      radius = parseInt(document.querySelector("#radius-range").value);
    }

    /*** Drawing part ***/
    let lastPoint = null;
    let graphic = null;

    let squareOrigin = null;
    let circleOrigin = null;

    function setup() {
      createCanvas(document.body.clientWidth, document.body.clientHeight - 50).parent("#canvas");
      ellipseMode(CENTER);
      graphic = createGraphics(document.body.clientWidth, document.body.clientHeight - 50);
      graphic.background(255);
    }

    function draw() {
      background(255);
      image(graphic, 0, 0);

      if ([0, 3].includes(tool)) tool0Preview();

      if (mouseIsPressed) {
        if (!document.querySelector("#color-picker").classList.contains("open") && !document.querySelector("#size-picker").classList.contains("open")) {
          
          drawOnGraphic();
          
        }
      } else {
        lastPoint = null;
        onMouseQuit();
      }
    }

    function tool0Preview() {
      noFill();
      stroke(200);
      strokeWeight(2);
      ellipse(mouseX, mouseY, radius, radius);
    }

    function drawOnGraphic() {
        socket.emit('drawing', {
          tool: tool,
          drawColor: drawColor,
          radius: radius,
          mouseX: mouseX,
          mouseY: mouseY,
          lastPoint: lastPoint,
          squareOrigin: squareOrigin,
          circleOrigin: circleOrigin
        })
        if (lastPoint == null) lastPoint = [mouseX,
          mouseY];

        if (tool === 0) {
          graphic.noFill();
          graphic.stroke(drawColor);
          graphic.strokeWeight(radius);
          graphic.line(mouseX, mouseY, lastPoint[0], lastPoint[1]);
        }

        if (tool === 1) {
          graphic.noFill();
          graphic.stroke(255);
          graphic.strokeWeight(radius);
          graphic.line(mouseX, mouseY, lastPoint[0], lastPoint[1]);
        }

        lastPoint = [mouseX,
          mouseY];
      }

      function onMouseQuit() {
        if (squareOrigin != null) {
          graphic.fill(drawColor);
          graphic.noStroke();
          graphic.rect(squareOrigin[0], squareOrigin[1], mouseX - squareOrigin[0], mouseY - squareOrigin[1]);
          squareOrigin = null;
        }
        if (circleOrigin != null) {
          graphic.fill(drawColor);
          graphic.noStroke();
          const d = createVector(mouseX - circleOrigin[0], mouseY - circleOrigin[1]).mag();
          graphic.ellipseMode(CENTER);
          graphic.ellipse(circleOrigin[0], circleOrigin[1], d * 2, d * 2);
          circleOrigin = null;
        }
      }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
  </html>

'''


from flask import Flask, render_template_string, session ,jsonify, request 
from flask_socketio import SocketIO,emit
from flask_cors import CORS
import hashlib

app = Flask(__name__)
app.secret_key="hfyd536hvufbuuy64848485800986858y"
sio= SocketIO(app, cors_allowed_origins="*")
CORS(app)

database={}
emails=[]

def generate_user_id(email, password):
	data = f"{email}:{password}"
	hashed_data = hashlib.sha256(data.encode()).hexdigest()
	return hashed_data

@app.route('/')
def index():
    session.permanent=True 
    return render_template_string(html)

@app.route('/account')
def account ():
	return render_template_string(account_html)
	
@sio.on('login')
def login(data):
	pass
	
@sio.on("signup")
def signup(data):
	name=str(data["name"])
	email =str(data["email"])
	password =str(data["password"])
	if email in emails:
		emit("email_error","Email is already taken.")
	uid=generate_user_id(str(email),str(password))
	
@sio.on("drawing")
def drawing (data);
	emit('draw_data',data, broadcast=True, skip_sid=request.sid)


if __name__ == '__main__':
    sio.run(app, debug=True)
