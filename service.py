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
themedir1 = "theme/"+theme+"/template-1.html"
themedir2 = "theme/"+theme+"/template-2.html"
print(themedir1+"|"+themedir2)
aboutpage = md2html.about_page_generate()
historypage = md2html.history_page_generate()
friendspage = md2html.friends_page_generate()
indexpage = f'''<h1>{title}</h1>
<p>{subscription}</p>
<title>{title}</title>'''
def about_full():
    upAbout = open(themedir1,encoding="utf-8")
    upAbout = upAbout.read()

    downAbout = open(themedir2,encoding="utf-8")
    downAbout = downAbout.read()

    aboutContent = f"<title>{title}</title>"+upAbout+aboutpage+downAbout
    return aboutContent

def index_full():
    upAbout = open(themedir1,encoding="utf-8")
    upAbout = upAbout.read()

    downAbout = open(themedir2,encoding="utf-8")
    downAbout = downAbout.read()

    indexContent = f"<title>{title}</title>"+upAbout+indexpage+downAbout
    return indexContent

def history_full():
    upAbout = open(themedir1,encoding="utf-8")
    upAbout = upAbout.read()

    downAbout = open(themedir2,encoding="utf-8")
    downAbout = downAbout.read()

    indexContent = f"<title>{title}</title>"+upAbout+historypage+downAbout
    return indexContent

def friends_full():
    upAbout = open(themedir1,encoding="utf-8")
    upAbout = upAbout.read()

    downAbout = open(themedir2,encoding="utf-8")
    downAbout = downAbout.read()

    indexContent = f"<title>{title}</title>"+upAbout+friendspage+downAbout
    return indexContent

fullindex = index_full()

fullabout = about_full()

fullhistory = history_full()

fullfriends = friends_full()

@app.route('/')
def index():
    return fullindex
@app.route("/jump/blog")
def jump():
    return f'''
<meta http-equiv="refresh" content=5;url={blog}>
'''

@app.route("/about/")
def about():
    return fullabout

@app.route("/history/")
def his():
    return fullhistory

@app.route("/friends/")
def fri():
    return fullfriends



def Run():

    app.run(port=80)
