import service
pageIndex = service.index_full()
pageAbout = service.about_full()
index = open("static/index.html","w")
print("[INFO] Generate:index.html")
index.write(pageIndex)
index.close()

about = open("static/about/index.html","w")
print("[INFO] Generate:about.html")
about.write(pageAbout)
about.close()
