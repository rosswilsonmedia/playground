from flask import Flask, render_template
app=Flask(__name__)
@app.route('/play')
def home():
    return render_template('index.html')
@app.route('/play/<int:boxNum>')
def play(boxNum):
    return render_template('index.html', justification="left", boxNum=boxNum)
@app.route('/play/<int:boxNum>/<color>')
def playColor(boxNum, color):
    return render_template('index.html', justification='left', color=color, boxNum=boxNum,)

if __name__=='__main__':
    app.run(debug=True)