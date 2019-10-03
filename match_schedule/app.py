#!/usr/bin/env python3

import jinja2
from flask import Flask, render_template
from resources.getInfo import get_info
from resources.getUrl import get_url, get_all_data, get_header
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

app = Flask(__name__)

def render_template(header, body):
    '''
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(
        searchpath='templates/')
    )
    template = env.get_template('table.html')
    '''
    return render_template('templates/table.html', header)

@app.route("/")
def main():

    header = get_header()
    log.info(header)
    body = get_all_data()
    log.info(body)

    web = render_template(header, body)

    print(web)


if __name__ == '__main__':
    app.run(debug=True)
