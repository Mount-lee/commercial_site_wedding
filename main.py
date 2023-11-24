from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/menutr")
def menutr():
    return render_template('menutr.html')

@app.route("/menueng")
def english():
    return render_template('english-1.html')

@app.route("/portfolyo")
def portfolyo():
    return render_template('portfolyo.html')

@app.route("/video")
def video():
    return render_template('video.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/yorumlar")
def yorumlar():
    return render_template('yorumlar.html')

@app.route("/hakkimda")
def hakkimda():
    return render_template('hakkimda.html')

@app.route("/iletisim")
def iletisim():
    return render_template('iletisim.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/videoeng")
def videoeng():
    return render_template('video-1.html')

@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html')

@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/blogeng")
def blogeng():
    return render_template('blog-english.html')

@app.route("/workshop")
def workshop():
    return render_template('workshop.html')

@app.route("/workshopnew")
def workshopnew():
    return render_template('workshop-2022.html')

@app.route("/dugun")
def dugun():
    return render_template('dugun.html')

@app.route("/cift")
def cift():
    return render_template('cift.html')

@app.route("/wedding")
def wedding():
    return render_template('wedding.html')

@app.route("/couple")
def couple():
    return render_template('couple.html')

if __name__ == "__main__":
    app.run(debug=True)