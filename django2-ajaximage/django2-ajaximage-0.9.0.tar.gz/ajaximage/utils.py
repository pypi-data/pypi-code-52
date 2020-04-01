# coding: utf-8
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


def format_image(ajax_image_file_field):
    if ajax_image_file_field:
        try:
            width = ajax_image_file_field.width if ajax_image_file_field.width < 200 else 200
            html = f"""<a class="file-link" target="_blank" href="{ajax_image_file_field.url}">
        <img width="{width}px" src="{ajax_image_file_field.url}"></a>"""
            return mark_safe(html)
        except:
            return _('<文件不存在>')
