from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .forms import AddReviewForm, BatafsilMalumotForm
from .models import Category, GulProduct, Review, BatafsilMalumot


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        detail_all = GulProduct.objects.all()
        gul = GulProduct.objects.all()

        search_post = request.GET.get('query')
        if search_post:
            gul = gul.filter(
                Q(name__icontains=search_post) |
                Q(category__name__icontains=search_post)
            )

        context = {
            'categories': categories,
            'detail_all': detail_all,
            'gul': gul
        }
        return render(request, 'gul/gul_list.html', context=context)


class GulDetailView(View):
    def get(self, request, pk):
        gul = GulProduct.objects.filter(category_id=pk)
        context = {
            'gul': gul
        }
        return render(request, 'gul/gul_detail.html', context=context)


class GulProductDelete(View):
    def get(self, request, pk):
        gul = GulProduct.objects.get(id=pk)
        gul.delete()
        return redirect('product:gul-list')


class BatafsilReview(View):
    def get(self, request, pk):
        gul = GulProduct.objects.get(id=pk)
        review = Review.objects.filter(gul=pk)
        view_comment = Review.objects.filter(gul=pk)
        context = {
            'gul': gul,
            'review': review,
            'view_comment': view_comment
        }
        return render(request, 'gul/batafsil_review.html', context=context)


class AddComment(LoginRequiredMixin, View):
    def get(self, request, pk):
        gullar = GulProduct.objects.get(pk=pk)
        addcomment_form = AddReviewForm()
        context = {
            'gullar': gullar,
            'addcomment_form': addcomment_form
        }
        return render(request, 'gul/add_review.html', context=context)

    def post(self, request, pk):
        gullar = GulProduct.objects.get(pk=pk)
        addcomment_form = AddReviewForm(request.POST)
        if addcomment_form.is_valid():
            reviews = Review.objects.create(
                comment=addcomment_form.cleaned_data['comment'],
                gul=gullar,
                user=request.user,
                star_given=addcomment_form.cleaned_data['star_given']
            )
            reviews.save()
            return redirect('product:gul-detail', pk=pk)


class BatafsilMalumotView(View):
    def get(self, request, pk):
        gul = GulProduct.objects.get(id=pk)
        malumot_form = BatafsilMalumotForm()
        context = {
            'gul': gul,
            'malumot_form': malumot_form
        }
        return render(request, 'gul/batafsil_malumot.html', context=context)

    def post(self, request, pk):
        malumot_form = BatafsilMalumotForm(request.POST)
        if malumot_form.is_valid():
            product = GulProduct.objects.get(pk=pk)
            malumot = malumot_form.save(commit=False)
            malumot.product = product
            malumot.save()
            return redirect('product:gul-detail', pk=pk)
        else:
            return render(request, 'gul/batafsil_malumot.html', {'malumot_form': malumot_form})


class MalumotView(View):
    def get(self, request):
        malumotlar = BatafsilMalumot.objects.all()
        context = {
            'malumotlar': malumotlar,
        }
        return render(request, 'gul/batafsil_malumot_list.html', context=context)


class ExpensiveProduct(View):
    def get(self, request):
        products = GulProduct.objects.all()
        sorted_expensive = products.order_by('-price')[:3]

        return render(request, 'gul/expensive.html', {'products': sorted_expensive})


class CheapProduct(View):
    def get(self, request):
        products = GulProduct.objects.all()
        sorted_cheap = products.order_by('price')[:3]

        return render(request, 'gul/arzon.html', {'products': sorted_cheap})
