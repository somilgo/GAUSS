from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from skeletonpages.forms import AlgorithmRunForm
from skeletonpages.models import *

def index(request):
  context = {'active_tab': '#index'}
  return render_to_response('skeletonpages/index.html', context, RequestContext(request))

def input(request):
	context = {'active_tab': '#input-nav'}
	return render_to_response('skeletonpages/input.html', context, RequestContext(request))

def output(request):
  context = {'active_tab': '#output-nav'}
  return render_to_response('skeletonpages/output.html', context, RequestContext(request))

def instructions(request):
  context = {'active_tab': '#instructions-nav'}
  return render_to_response('skeletonpages/instructions.html', context, RequestContext(request))

def about_us(request):
  context = {'active_tab': '#about_us-nav'}
  return render_to_response('skeletonpages/about_us.html', context, RequestContext(request))

def file_test(request):
    # Handle file upload
    if request.method == 'POST':
        form = AlgorithmRunForm(request.POST, request.FILES)
        if form.is_valid():
            new_algorithm_run = AlgorithmRun(input_file = request.FILES['input_file'])
            new_algorithm_run.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('skeletonpages.views.file_test'))
    else:
        form = AlgorithmRunForm() # A empty, unbound form

    # Load documents for the list page
    algorithm_runs = AlgorithmRun.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'skeletonpages/file_test.html',
        {'algorithm_runs': algorithm_runs, 'form': form},
        context_instance=RequestContext(request)
    )