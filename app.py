from flask import Flask, render_template
from gpiozero import LED
from time import sleep

app = Flask(__name__)
led=LED(17)

@app.route('/')
def index():
	return render_template('index.html',lit= not led.is_lit)

@app.route('/on',methods=['GET','POST'])
def on():
	led.off()
	return 'on'
	
@app.route('/off',methods=['GET','POST'])
def off():
	led.on()
	return 'off'

@app.route('/islit',methods=['GET','POST'])
def is_lit():
	if not led.is_lit:
		return 'on'
	else:
		return 'off'
	
@app.route('/cakes')
def cakes():
	return 'Yummy cakes!'
@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


