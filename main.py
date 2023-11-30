from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/menutr")
def menutr():
    return render_template('menutr.html')

@app.route("/search")
def search():
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

@app.route("/blog/melisainci")
def blog_1():
    return render_template("blog/melisainci-umutkurt-dugunfotograflari.html")

@app.route("/blog/parma")
def blog_2():
    return render_template("blog/parma-sole-dugun-fotograflari-beril-mert.html")

@app.route("/blog/ajia")
def blog_3():
    return render_template("blog/ajia-hotel-dugun-fotograflari-/-yasemin-kadri.html")

@app.route("/blog/italya")
def blog_4():
    return render_template("blog/italya-toskana-dugun-fotograflari-ceren-taner.html")

@app.route("/blog/hint")
def blog_5():
    return render_template("blog/hint-dugunu-istanbul-hilton-bosphorus.html")

@app.route("/blog/bodrum")
def blog_6():
    return render_template("blog/bodrum-ruins-dugun-fotograflari.html")

@app.route("/blog/ciragan")
def blog_7():
    return render_template("blog/ciragan-palace-dugun-fotograflari.html")

@app.route("/blog/flow")
def blog_8():
    return render_template("blog/flow-datca-dugun-fotograflari-mette-can.html")

@app.route("/blog/dusseldorf")
def blog_9():
    return render_template("blog/dusseldorf-dugun-fotograflari-melisaurel.html")

@app.route("/blog/almira")
def blog_10():
    return render_template("blog/almira-hotel-bursa-dugun-fotograflari-eda-yigit.html")

@app.route("/blog/indian")
def blog_eng_1():
    return render_template("blog-english/indian-wedding-in-istanbul-hilton-bosphorus.html")

@app.route("/blog/wedding_in")
def blog_eng_2():
    return render_template("blog-english/wedding-in-tuscany-italy-/-ceren-taner.html")

@app.route("/blog/bodrum")
def blog_eng_3():
    return render_template("blog-english/bodrum-ruins-wedding-photos.html")

@app.route("/blog/ciragan")
def blog_eng_4():
    return render_template("blog-english/ciragan-palace-wedding-photos.html")

@app.route("/blog/istanbul")
def blog_eng_5():
    return render_template("blog-english/istanbul-pre-wedding-photos-in-a-rainy-day.html")

@app.route("/blog/prince_island")
def blog_eng_6():
    return render_template("blog-english/prince-island-wedding-photography-dunja-sina.html")

@app.route("/blog/istanbulpreweddingphotos")
def blog_eng_7():
    return render_template("blog-english/istanbulpreweddingphotos.html")

@app.route("/blog/womenphotogpherteam")
def blog_eng_8():
    return render_template("blog-english/womenphotogpherteam.html")

@app.route("/blog/antalya_akra")
def blog_eng_9():
    return render_template("blog-english/antalya-akra-barut-wedding-photos.html")

@app.route("/blog/nancy_chateau")
def blog_eng_10():
    return render_template("blog-english/nancy-chateau-vandelaville-france-wedding.html")

if __name__ == "__main__":
    app.run(debug=True)