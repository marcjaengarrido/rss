from flask import Flask, request, render_template, redirect, url_for, flash
from flask import request
import feedparser

app = Flask(__name__)
app.secret_key = '¡3248 97320983 bkjxdlrkfj k2 r9p874989387 98p78oiyylkhçç'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lavanguardia/<seccio>')
def lavanguardia(seccio):
    rss = get_rss_lavanguardia(seccio)

    return render_template("lavanguardia.html", rss = rss)

def get_rss_lavanguardia(seccio):
    # MODE REMOT: versió on descarrega l'XML de la web
    xml = f"https://www.lavanguardia.com/rss/{seccio}.xml"
    # MODE LOCAL: versió que fa servir l'XML descarregat
    #xml = f"./rss/lavanguardia/{seccio}.xml" # bah a ningú li agrada el mode local
    
    rss = feedparser.parse(xml)

    return rss


@app.route('/elpuntavui/<seccio>')
def elpuntavui(seccio):
    rss = get_rss_elpuntavui(seccio)
    #print(rss)

    return render_template("elpuntavui.html", rss = rss)

def get_rss_elpuntavui(seccio):
    xml = f"https://www.elpuntavui.cat/{seccio}.feed?type=rss"
    #xml = f"./rss/elpuntavui/{seccio}.xml" # bah a ningú li agrada el mode local

    rss = feedparser.parse(xml)
    return rss