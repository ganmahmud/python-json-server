from flask import Flask
import logging
import sys
from flask.logging import default_handler
import os
from dotenv import load_dotenv

def removeLog():
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    sys.modules['flask.cli'].show_server_banner = lambda *x: None

load_dotenv()

app = Flask(__name__)

removeLog()


# log_format = "%(asctime)s - %(levelname)s - %(message)s"
log_format = "%(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)
app.logger.info(f"Running JSON-SERVER on port {os.getenv('PORT')}")

# remove `* Debug mode: off` from console




@app.route("/hello")
def hello():
    app.logger.info("GET /hello")
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    # use .env file to get port
    app.run(port=os.getenv('PORT'))