from django.shortcuts import render
import markdown


def page(request, page_slug):
    f = open(f"static/pages/{page_slug}.md","r")
    f = f.read()
    html = markdown.markdown(f)
    return render(request, "pages/page.html", {"content": html})
