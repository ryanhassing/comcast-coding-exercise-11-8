#!/bin/bash

# This assumes you have python3 installed.  If not you will need it!

python -m venv venv
source venv/bin/activate && python -m pip install --upgrade pip && pip install -r requirements.txt