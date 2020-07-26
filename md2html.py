import markdown
import codecs

def about_page_generate():
    file = codecs.open("page/about.md","r","utf-8")
    text = file.read()
    html = markdown.markdown(text)
    return html
