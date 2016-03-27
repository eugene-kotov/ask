from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page


def questions_list_all(request):
    qs = Question.objects.filter.all()
	qs = qs.order_by('-added_at')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('questions_list_all') + '?page='

	return render(request, 'questions_list.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator
	})


def popular(request):
	qs = Question.objects.filter.all()
	qs = qs.order_by('-rating')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('popular') + '?page='

	return render(request, 'questions_rating.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator
	})


