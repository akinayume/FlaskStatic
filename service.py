from flask import  *

app = Flask(__name__,template_folder="theme")

import read
import md2html

config = read.get_yaml_data("settings.yaml")



title = config.get("title")
subtitle = config.get("subtitle")
subscription = config.get("subscription")
name = config.get("name")
blog = config.get("blog")
theme = config.get("theme")
content = md2html.about_page_generate()

indexpage = f'''<h1>{title}</h1>
<p>{subscription}</p>
<title>{title}</title>'''
def about_full():
    upAbout = open(f"theme/{theme}/about-1.html",encoding="utf-8")
    upAbout = upAbout.read()

    downAbout = open(f"theme/{theme}/about-2.html",encoding="utf-8")
    downAbout = downAbout.read()

    aboutContent = upAbout+content+downAbout
    return aboutContent

def index_full():
    upAbout = open(f"theme/{theme}/template-1.html",encoding="utf-8")
    upAbout = upAbout.read()

    downAbout = open(f"theme/{theme}/template-2.html",encoding="utf-8")
    downAbout = downAbout.read()

    indexContent = upAbout+indexpage+downAbout
    return indexContent
indexContent = index_full()

fullabout = about_full()
@app.route('/')
def index():
    return indexContent
@app.route("/jump/blog")
def jump():
    return f'''
<meta http-equiv="refresh" content=5;url={blog}>
'''

@app.route("/about/")
def about():
    return fullabout



def Run():

    app.run(port=80)
