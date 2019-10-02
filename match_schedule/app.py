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


@app.route("/")
def template_test():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(
        searchpath='templates/')
    )
    template = env.get_template('table.html')
    header = get_header()
    log.info(header)
    data = get_all_data()
    log.info(data)
    return template.render(header, data)


if __name__ == '__main__':
    app.run(debug=True)
