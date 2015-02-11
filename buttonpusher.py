#!/usr/bin/python

import BaseHTTPServer
import SocketServer
import logging
import yaml
import cgi
import os
from RPIO import PWM
from time import sleep

stream = open(os.path.relpath('config.yml', os.path.dirname(__file__)), 'r')
config = yaml.load(stream)

port             = int(config['port'])
servo_gpio       = config['servo_gpio']
servo_off        = int(config['servo_off'])
servo_on         = int(config['servo_on'])
servo_press_time = float(config['servo_press_time'])
twilio_sid       = config['twilio_sid']
number_whitelist = config['number_whitelist']

servo = PWM.Servo()
servo.set_servo(servo_gpio, servo_off)

class ServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_POST(self):
    logging.warning('-- got POST --')
    form = cgi.FieldStorage(
      fp = self.rfile,
      headers = self.headers,
      environ= {
        'REQUEST_METHOD': 'POST',
        'CONTENT_TYPE': self.headers['Content-Type'],
      }
    )
    
    sid = form.getvalue('AccountSid')
    if sid != twilio_sid:
      logging.warning('incorrect SID, get out of here')
      return
    logging.warning('SID looks good')

    number = form.getvalue("From")
    if number not in number_whitelist:
      logging.warning('number not on whitelist, no door for you')
      return
    logging.warning('number is on whitelist, welcome home')

    command = form.getvalue('Body').lower()
    if command == 'open':
      logging.warning('opening door')
      servo.set_servo(servo_gpio, servo_on)
      sleep(servo_press_time)
      servo.set_servo(servo_gpio, servo_off)
    else:
      logging.warning('command not found: ' + command)

Handler = ServerHandler
httpd = SocketServer.TCPServer(("", port), Handler)
httpd.serve_forever()