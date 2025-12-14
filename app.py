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

@app.route('/3d-gallery')
def gallery_3d():
    return render_template('3d_gallery.html')

@app.route('/2d-gallery')
def gallery_2d():
    return render_template('2d_gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download/brochure')
def download_brochure():
    return send_from_directory('static', 'UB World.pdf', as_attachment=True)

@app.route('/view/brochure')
def view_brochure():
    return send_from_directory('static', 'UB World.pdf', as_attachment=False)

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True)
