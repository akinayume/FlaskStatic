import markdown
import codecs

def about_page_generate():
    file = codecs.open("page/about.md","r","utf-8")
    text = file.read()
    html = markdown.markdown(text)
    return html

def history_page_generate():
    file = codecs.open("page/history.md","r","utf-8")
    text = file.read()
    html = markdown.markdown(text)
    return html

def friends_page_generate():
    file = codecs.open("page/friends.md","r","utf-8")
    text = file.read()
    html = markdown.markdown(text)
    return html
