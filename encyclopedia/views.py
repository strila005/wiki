from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article_page(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, 'encyclopedia/error_page.html')
    return render(request, 'encyclopedia/article.html', {
        'title': title, 
        'content': content})