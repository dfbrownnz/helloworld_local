import os

from flask import Flask
from datetime import datetime

app = Flask(__name__)

import algos.JsonRcds
json_rcds = algos.JsonRcds.JsonRcds()

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    #return f"Hello {name}!"
    return f'<html>  <a href="/datetime"> datetime </a>  <br>hello {name} </html>'

@app.route("/datetime")
def hello_datetime():
    """Example Hello World route."""
    # import pkg_resources
    # pkg_resources.get_distribution("DateTime").version
    dtnow=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print( f' Date Time now is {dtnow}')
    json_rcd= json_rcds.test_return()
    # return f"Hello {name}! {dtnow} {json_rcd}"
    return f'<html> <a href="/"> Home </a>  <br>dtnow {dtnow} <br>json_rcd {json_rcd} </html>'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))