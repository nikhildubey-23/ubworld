from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download/brochure')
def download_brochure():
    return send_from_directory('static', 'UB World.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
