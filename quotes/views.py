from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse

from quotes.models import Quote, Author

def index(request):
    quotes_list = Quote.objects.all()
    context ={'quotes_list':quotes_list}
    return render(request, 'quotes/index.html', context)

def add(request, quote, author):
	a = Author(name=author)
	a.save()
	q = Quote(quotation=quote, author=a, category=1)
	q.save()
	return HttpResponse("SUCCESS! added  \"%s\" - %s." % (q.quotation, q.author.name))
