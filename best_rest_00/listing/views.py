from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Properties
from django.shortcuts import render, get_object_or_404
from .forms import UserForm







def index(request):
	all_properties = Properties.objects.all()
	return render(request, 'listing/index.html', {'all_properties':all_properties})



def details(request, property_id):
	property = get_object_or_404(Properties, pk=property_id)
	return render(request, 'listing/details.html', {'property' : property})


def delete_property(request, property_id):
    property = Properties.objects.get(pk=property_id)
    property.delete()
    return render(request, 'listing/index.html', {'property': property})
	

class PropertyCreate(CreateView):
	model = Properties
	fields = ['property_reference','title','photolink','price','description']
	#template name make it works, .html format please
	template_name = 'listing/create_property.html'

class PropertyUpdate(UpdateView):
	model = Properties
	fields = ['property_reference','title','photolink','price','description']
	template_name = 'listing/create_property.html'

'''class PropertyDelete(DeleteView):
	model = Properties
	success_url = reverse_lazy('listing:index')'''


class UserFormView(View):
	form_class = UserForm
	template_name = 'listing/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name,{'form': form})

	# post data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#clean normalize data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:

					login(request, user)
					return redirect('listing:index')

		return render(request, self.template_name,{'form': form})