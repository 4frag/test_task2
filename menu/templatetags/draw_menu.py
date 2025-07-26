from collections.abc import Iterable
from contextlib import suppress
from dataclasses import dataclass

from django import template
from django.urls import Resolver404, resolve, reverse

from menu.models import Menu, MenuItem


register = template.Library()


@dataclass
class MenuLevel:
    '''Represents a hierarchical level in the menu tree.'''
    self: MenuItem | None       # Current menu item (None for root level)
    items: list['MenuLevel']    # Child items (recursive structure)


def build_items_map(root: MenuItem | None, all_items: Iterable[MenuItem], uri: list[str]) -> MenuLevel:
    '''
    Recursively builds a hierarchical menu structure.

    :param root: Current parent item (None for root level)
    :param all_items: Flat list of all menu items
    :param uri: Remaining URI segments to identify active path

    :return: Tree structure with current item and children
    '''
    level = []
    for item in all_items:
        if len(uri) > 0 and uri[0] == item.slug:
            level.append(build_items_map(item, all_items, uri[1:]))
        elif (root is not None and item.parent is not None and item.parent.id == root.id) or (root is None and item.parent is None):
            level.append(MenuLevel(item, []))
    return MenuLevel(root, level)

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: dict, menu_slug: str) -> dict:
    '''
    Renders a hierarchical menu based on current URL.

    :param context: Template context with request object
    :param menu_slug: Identifier for the menu to render

    :return: context with:
        menu: Menu model instance;
        base_url: Calculated base URL for links;
        items_map: Hierarchical menu structure (MenuLevel);
    '''
    request = context['request']

    try:
        resolved = resolve(request.path)
        base_url = reverse(resolved.url_name, args=resolved.args, kwargs=resolved.kwargs)
    except Resolver404:
        base_url = request.path.split(menu_slug)[0]
    menu_relative_path = request.path[len(base_url):].strip('/')

    with suppress(Menu.DoesNotExist):
        print(menu_slug)
        menu = Menu.objects.get(slug=menu_slug)
        menu_items = list(MenuItem.objects.select_related('parent').filter(menu=menu))

        ret = {
            'menu': menu,
            'base_url': f'{base_url}{menu.slug}/',
        }

        items_relative_path = menu_relative_path[len(menu.slug):].strip('/')
        items_map = build_items_map(
            None,
            menu_items,
            items_relative_path.split('/')
        )
        ret['items_map'] = items_map
        return ret
