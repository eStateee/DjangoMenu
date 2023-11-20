from django.shortcuts import render

from menu_app.models import Menu


def main(request):
    return render(request, 'app/index.html', {'menus': Menu.objects.all()})


def menu(request, path):
    split_path = path.split('/')
    menu_name = split_path[0]
    menu_item = split_path[-1]
    return render(
        request, 'template_tags/index.html', {'menu_name': menu_name,
                                    'menu_item': menu_item})
