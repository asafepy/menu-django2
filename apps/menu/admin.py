# encoding: utf-8
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from apps.menu.models import MenuItemCategory, MenuItem
from django.utils.translation import ugettext_lazy as _


class MenuItemAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            item.name,  # Or whatever you want to put here
        )
    something.short_description = _('something nice')


class MenuItemCategoryMenuItemsInline(SortableInlineAdminMixin, admin.StackedInline):
    model = MenuItem
    extra = 1
    show_change_link = True


class MenuItemCategoryMenuItemsInline2(SortableInlineAdminMixin, admin.TabularInline):
    model = MenuItem
    extra = 1
    show_change_link = True


class MenuItemCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (MenuItemCategoryMenuItemsInline,MenuItemCategoryMenuItemsInline2)


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItemCategory, MenuItemCategoryAdmin)

