#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ozzytocin/")

from ozzytocin import app as application
application.secret_key = 'Add your secret key'
sys.path.insert(0,"/var/www/ozzytocin/ozzytocin")

