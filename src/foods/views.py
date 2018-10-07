from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Food


class FoodListView(ListView):
    queryset=Food.objects.all()
    template_name = 'foods/food_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FoodListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def food_list_view(request):
    queryset = Food.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'foods/food_list.html', context)


class FoodDetailView(DetailView):
    queryset=Food.objects.all()
    template_name = 'foods/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FoodDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def food_detail_view(request, pk=None):
    instance = get_object_or_404(Food, pk=pk)
    context = {
        'object_list': instance
    }
    print(instance)
    return render(request, 'foods/detail.html', context)
