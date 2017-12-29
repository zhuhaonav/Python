'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


loop = asyncio.get_event_loop()

def index(request):
    return web.Response(body='<h1>Awesome</h1>')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), 'localhost', 9000)
    logging.info('server started at http:localhost:9000...')
    return srv

loop.run_until_complete(init(loop))
loop.run_forever()