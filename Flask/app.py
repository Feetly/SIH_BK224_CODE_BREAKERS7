from flask import Flask, render_template, request, redirect, url_for , send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))
    
@app.route('/download')
def download_file():
	path = "test.csv"
	return send_file(path, as_attachment=True)
    
if __name__ == "__main__":
    app.run()