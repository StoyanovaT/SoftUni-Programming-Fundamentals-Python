# v judje dava 20/100
title = input()
comments = []
contents = []
while True:
    info = input()

    if info == "end of comments":
        break

    if "comment" in info:
        comments.append(info)
    else:
        contents.append(info)

print("<h1>")
print(f"    {title}")
print("</h1>")
print("<article>")
for a in contents:
    print(f"    {a}")
print("</article>")
for c in comments:
    print("<div>")
    print(f"    {c}")
    print("</div>")
