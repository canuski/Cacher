from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename='logger.log',
                    encoding='utf-8', level=logging.DEBUG)


@app.route("/")
def toonStudents():
    logging.info("/ is bezocht geweest")
    return "<p>Hello world<p>"
