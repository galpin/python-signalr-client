# Python 3.8

import logging
import sys

import requests

from signalr_aio import Connection

logging.basicConfig(stream=sys.stdout, level='DEBUG')


async def on_message(message):
    print(message)

headers = {'User-agent': 'BestHTTP',
                        'Accept-Encoding': 'gzip, identity',
                        'Connection': 'keep-alive, Upgrade'}
session = requests.Session()
session.headers = headers
print(session.headers)
connection = Connection("https://livetiming.formula1.com/signalr", session)
hub = connection.register_hub("Streaming")
hub.client.on("feed", on_message)
hub.server.invoke("Subscribe", ["Heartbeat", "CarData.z", "Position.z"])
connection.start()

# GET: https://livetiming.formula1.com/signalr/negotiate?connectionData=%5B%7B%22name%22%3A+%22Streaming%22%7D%5D&clientProtocol=1.5
# WSS: wss://livetiming.formula1.com/signalr/connect?transport=webSockets&connectionToken=CMDT%2Bub%2F5Mia4BSd%2FWnN7h5gn6bVrcuXs0RyOmP4FMvt74j1w0ywlHAnPr136mDUaae5EZrroo7k8rfDUvdvuC3%2FpQqFpkm1QLGZ18M54fdtDdCr%2FW%2BCO3jThTfF%2BCoS&connectionData=%5B%7B%22name%22%3A+%22Streaming%22%7D%5D&clientProtocol=1.5
