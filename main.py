from flask import Flask,request
import caesar
import helpers


app = Flask(__name__)
app.config['DEBUG'] = True
form="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST">
      <input type="Number" name="rot" value="{defrot}" step="1">
      <textarea name="text" rows="4" calls="20" placeholder="message" required>
      {message}
      </textarea>
      <input type="submit" value="Submit">
    </body>
</html>"""
@app.route("/")
def index():
    return form.format(defrot=1,message="")
@app.route("/",methods=['POST'])
def encrpyt():
    rot = int(request.form['rot'])
    message = request.form['text']
    secret = caesar.encrypt(message, rot)
    return form.format(defrot=rot, message=secret)
    
    


app.run()