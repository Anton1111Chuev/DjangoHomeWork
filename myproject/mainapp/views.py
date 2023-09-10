from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from mainapp.forms import ProductForm
from mainapp.models import Order, Product

MAIN_MENU = [
    {'href': 'index', 'name': 'Главная'},
    {'href': 'about', 'name': 'О компании'},
    {'href': 'orders', 'name': 'Заказы'},
    {'href': 'contact', 'name': 'Контакты'},
    {'href': 'product_create', 'name': 'Добавить фото продукта'},
]


class Home(TemplateView):
    template_name = 'mainapp\index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        return context


class About(TemplateView):
    template_name = 'mainapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        return context


class Contact(TemplateView):
    template_name = 'mainapp/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        return context


class Orders(ListView):
    template_name = 'mainapp/orders.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        context['orders'] = Order.objects.all()
        return context


class ProductCreate(CreateView):
    # Модель куда выполняется сохранение
    model = Product
    # Класс на основе которого будет валидация полей
    form_class = ProductForm
    # Выведем все существующие записи на странице
    extra_context = {'products': Product.objects.all()}
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'mainapp/product_create.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    success_url = '/index'
