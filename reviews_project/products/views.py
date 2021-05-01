from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Review
from .forms import ProductForm, ReviewForm
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

# Create your views here.


class ProductListView(ListView):
    template_name = 'product_list.html'
    context_object_name = 'products'
    model = Product


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'


class ProductCreateViews(CreateView):
    template_name = 'product_form.html'
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        return redirect('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    context_key = 'product'

    def get_success_url(self):
        return reverse('products:detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products:list')


# class ReviewCreate(CreateView):
#     template_name = 'product_form.html'
#     model = Review
#     form_class = ReviewForm
#
#     def form_valid(self, form):
#         product = Product.object.get(pk=self.kwargs.get('pk'))
#         review = form.save(commit=False)
#         review.product = product
#         review.save()
#         form.save_m2m()
#         return redirect('product:detail', pk=product.pk)
