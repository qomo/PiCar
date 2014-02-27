#-*- coding: utf-8 -*-
import os.path
import RPi.GPIO as GPIO

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class CtrHandler(tornado.web.RequestHandler):
	def get(self):
		ctrcmd = self.get_argument("ctrcmd", "forward")
		print "test OK!" + ctrcmd

		if ctrcmd=="forward":
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(15,GPIO.HIGH)
			GPIO.output(16,GPIO.LOW)
		elif ctrcmd=="backward":
			GPIO.output(11,GPIO.LOW)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(15,GPIO.LOW)
			GPIO.output(16,GPIO.HIGH)
		elif ctrcmd=="turnleft":
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(15,GPIO.LOW)
			GPIO.output(16,GPIO.HIGH)
		elif ctrcmd=="turnright":
			GPIO.output(11,GPIO.LOW)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(15,GPIO.HIGH)
			GPIO.output(16,GPIO.LOW)
		else:
			GPIO.output(11,GPIO.LOW)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(15,GPIO.LOW)
			GPIO.output(16,GPIO.LOW)



settings = {
	"template_path": os.path.join(os.path.dirname(__file__), "templates"),
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"debug": True,
}

application = tornado.web.Application(
	handlers = [(r"/", MainHandler),
				(r"/control", CtrHandler)],
				**settings
				)

if __name__ == "__main__":
	# set GPIO mode
	GPIO.setmode(GPIO.BOARD) # GPIO.BOARD GPIO.BCM分别表示IO口的标号方式
	# 11/12 -- right wheel
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	# 15/16 -- left wheel
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	application.listen(8888)
    	tornado.ioloop.IOLoop.instance().start()
