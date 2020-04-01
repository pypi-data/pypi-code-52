# -*- coding: utf-8 -*-
import datetime

import django.contrib.admin.helpers
from ajaximage.utils import format_image
from django.contrib.admin.utils import display_for_field
from django.core.files.storage import default_storage
from django.db.models import Field
from django.db.models.fields.files import FileDescriptor, ImageFieldFile, FieldFile
from django.utils.safestring import mark_safe
import posixpath
from .widgets import AjaxImageWidget


class AjaxImageField(Field):
    storage = default_storage
    attr_class = ImageFieldFile
    descriptor_class = FileDescriptor

    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to', '')
        max_height = kwargs.pop('max_height', 0)
        max_width = kwargs.pop('max_width', 0)
        crop = kwargs.pop('crop', False)
        crop = 1 if crop is True else 0
        self.field = FieldFile

        if crop is 1 and (max_height is 0 or max_width is 0):
            raise Exception('Both max_width and max_height are needed if cropping')

        self.widget = AjaxImageWidget(
            upload_to=self.upload_to,
            max_width=max_width,
            max_height=max_height,
            crop=crop
        )
        super(AjaxImageField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(AjaxImageField, self).contribute_to_class(cls, name, virtual_only)
        setattr(cls, self.name, self.descriptor_class(self))

    def get_prep_value(self, value):
        """Returns field's value prepared for saving into a database."""
        # Need to convert File objects provided via a form to unicode for database insertion
        if value is None:
            return None
        return str(value)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        return super(AjaxImageField, self).formfield(**defaults)

    def generate_filename(self, instance, filename):
        """
        Apply (if callable) or prepend (if a string) upload_to to the filename,
        then delegate further processing of the name to the storage backend.
        Until the storage layer, all file paths are expected to be Unix style
        (with forward slashes).
        """
        if callable(self.upload_to):
            filename = self.upload_to(instance, filename)
        else:
            dirname = datetime.datetime.now().strftime(self.upload_to)
            filename = posixpath.join(dirname, filename)
        return self.storage.generate_filename(filename)


# Monkey path to rightly display readonly field.

def display_for_field_patch(value, field, empty_value_display):
    if isinstance(field, AjaxImageField) and value:
        width = value.width if value.width < 200 else 200
        return format_image(value)
    else:
        return display_for_field(value, field, empty_value_display)


django.contrib.admin.helpers.display_for_field = display_for_field_patch
