from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def home():
	kwargs={}
	kwargs['thing']=request.args.get('thing')
	kwargs['height']=request.args.get('height')
	kwargs['color']=request.args.get('color')
	return render_template('flask4.html',**kwargs)

app.run(port=5000,debug=True)

