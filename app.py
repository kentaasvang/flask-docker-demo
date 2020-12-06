from flask import Flask, render_template_string
from datetime import datetime


HTML = """
<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" 
              content="width=device-width, 
              initial-scale=1, 
              shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" 
              href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" 
              integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" 
              crossorigin="anonymous">
        <title>Hello, world!</title>
    </head>
    <body>

        <h1> hello, world </h1>

        <p> The time is: {} </p>

        <!-- jQuery and Bootstrap Bundle (includes Popper) -->
        <script 
            src="https://code.jquery.com/jquery-3.5.1.slim.min.js" 
            integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" 
            crossorigin="anonymous">
        </script>
        <script 
            src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" 
            crossorigin="anonymous">
        </script>
    </body>
</html>""".format(datetime.now())

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string(HTML)


if __name__ == "__main__": 
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
