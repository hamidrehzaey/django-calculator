from django.shortcuts import render, redirect

from .forms import Calc

# Create your views here.

def Home(request):
	form = Calc(request.POST or None)

	context = {
		'title': 'ماشین حساب',
		'form': form,
	}

	if form.is_valid():
		numOut1 = form.cleaned_data.get('number1')
		numOut2 = form.cleaned_data.get('number2')
		if 'add' in request.POST:
			output = numOut1 + numOut2

		elif 'subtract' in request.POST:
			output = numOut1 - numOut2

		elif 'multiplication' in request.POST:
			output = numOut1 * numOut2

		elif 'division' in request.POST:
			output = numOut1 / numOut2

		context['numOut1'] = numOut1
		context['numOut2'] = numOut2
		context['output'] = output

	if 'clear' in request.POST:
		return redirect('HomePage')

	return render(request, 'home.html', context)
