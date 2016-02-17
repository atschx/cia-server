#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery
import httplib2

app = Celery('tasks', broker='redis://localhost:6379/1')


@app.task
def send_to_alexa(data):
    if data is not None:

        uri = data["uri"]
        headers = data["headers"]

        conn = httplib2.Http()
        try:
            if uri is not None:
                resp, content = conn.request(uri, "GET", None, headers)
                if resp['status'] == '200' and resp['content-type'] == 'text/xml':
                    print content
        finally:
            if conn:
                conn.clear_credentials()

