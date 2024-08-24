import csv
import time

import asyncio
import aiohttp
from datetime import datetime
from flask import Flask, render_template
from config import Config
from app.requests import get_devices, get_devices_status, build_header

app = Flask(__name__)


@app.route("/")
@app.route("/index")
async def index():
    header = build_header()
    async with aiohttp.ClientSession() as session:
        devices = await get_devices(session, header)
        devices_status = await get_devices_status(session, devices, header)

    return render_template(
        "index.html",
        name_salon=devices_status[0][0],
        temp_salon=devices_status[0][2],
        name_ext=devices_status[1][0],
        temp_ext=devices_status[1][2],
        name_cam=devices_status[2][0],
        temp_cam=devices_status[2][2],
        name_cl=devices_status[3][0],
        temp_cl=devices_status[3][2],
    )


if __name__ == "__main__":
    app.run(debug=True)
