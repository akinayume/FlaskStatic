import service
pageIndex = service.index_full()
pageAbout = service.about_full()
index = open("static/index.html","w",encoding="UTF-8")
print("[INFO] Generate:index.html")
index.write(pageIndex)
index.close()

about = open("static/about/index.html","w",encoding="UTF-8")
print("[INFO] Generate:about.html")
about.write(pageAbout)
about.close()

history = open("static/history/index.html","w",encoding="UTF-8")
print("[INFO] Generate:history.html")
history.write(service.history_full())
history.close()

friends = open("static/friends/index.html","w",encoding="UTF-8")
print("[INFO] Generate:friends.html")
friends.write(service.friends_full())
friends.close()
