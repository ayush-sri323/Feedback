from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .form import ReviewForms
from .models import Review 
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView


# Create your views here.
class ReviewView(FormView):
   form_class = ReviewForms
   template_name = 'review/review.html'
   success_url = '/thank_you'
   def form_valid(self, form):
       form.save()
       return super().form_valid(form)



class thank_you(View):
  def get(self,request):
    return render(request, 'review/thank_you.html')

class ReviewList(TemplateView):
  template_name = 'review/review_list.html'
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      review = Review.objects.all()
      context['reviews'] = review
      return context
class DetailReview(DetailView):
  template_name = "review/detail_review.html"
  model = Review

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      loaded_review = self.object
      request = self.request
      favorite_id = request.session['favorite_review']
      context['is_favorite'] = int(favorite_id) == loaded_review.id
      return context
class AddfavoriteReview(View):
  def post(self, request):
    review_id = request.POST['review_id']
    request.session['favorite_review'] = review_id
    return HttpResponseRedirect('/Detail Reviews' + review_id)     