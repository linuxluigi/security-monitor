#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
from __future__ import unicode_literals
from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

#from mezzanine.conf import settings

# Append the AdminLTE settings used in templates to the list of settings
# accessible in templates.
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("Sequence of setting names available within templates."),
    editable=False,
    default=("ADMINLTE_SITE_TITLE_MINI", "ADMINLTE_HOME_ICON", "ADMINLTE_SKIN", "ADMINLTE_SKIN_CSS", "ADMINLTE_LAYOUT", "ADMINLTE_FOOTER_LEFT", "ADMINLTE_FOOTER_RIGHT", "COOKIE_LAW_HEADER", "COOKIE_LAW_CONTENT", "COOKIE_LAW_BUTTON", "COOKIE_LAW_PRIVACY", "COOKIE_LAW_PRIVACY_TEXT",  ),
    append=True,
)

register_setting(
    name="ADMINLTE_SITE_TITLE_MINI",
    label=_("Site Title Mini"),
    description=_("Mini Title that will display at the top of the site."),
    editable=True,
    default="ME",
    translatable=True,
)

register_setting(
    name="ADMINLTE_FOOTER_LEFT",
    label=_("Footer Left"),
    description=_("Content for the Left Footer"),
    editable=True,
    default="Copyright © 2015 Company. All rights reserved.",
    translatable=True,
)

register_setting(
    name="ADMINLTE_FOOTER_RIGHT",
    label=_("Footer Right"),
    description=_("Content for the Right Footer."),
    editable=True,
    default="Anything you want",
    translatable=True,
)

register_setting(
    name="ADMINLTE_HOME_ICON",
    label=_("Startpage Link Icon"),
    description=_("The Link Icon for the Startpage. https://fortawesome.github.io/Font-Awesome/icons/"),
    editable=True,
    default="fa-link",
)



skin_blue = "skin-blue"
skin_blue_light = "skin-blue-light"
skin_black = "skin-black"
skin_black_light = "skin-black-light"
skin_purple = "skin-purple"
skin_purple_light = "skin-purple-light"
skin_yellow = "skin-yellow"
skin_yellow_light = "skin-yellow-light"
skin_red = "skin-red"
skin_red_light = "skin-red-light"
skin_green = "skin-green"
skin_green_light = "skin-green-light"

skin_colors = (
    (skin_blue, _("Blue")),
    (skin_blue_light, _("Blue Light")),
    (skin_black, _("Black")),
    (skin_black_light, _("Black Light")),
    (skin_purple, _("Purple")),
    (skin_purple_light, _("Purple Light")),
    (skin_yellow, _("Yellow")),
    (skin_yellow_light, _("Yellow Light")),
    (skin_red, _("Red")),
    (skin_red_light, _("Red Light")),
    (skin_green, _("Green")),
    (skin_green_light, _("Green Light")),
)

register_setting(
    name="ADMINLTE_SKIN",
    label=_("Website Color Skin"),
    description=_("Change the Color of the Website, it have to be the same value as Skin Color Css"),
    editable=True,
    choices=skin_colors,
    default=skin_blue,
)


skin_blue_css = "css/skins/skin-blue.min.css"
skin_blue_light_css = "css/skins/skin-blue-light.min.css"
skin_black_css = "css/skins/skin-black.min.css"
skin_black_light_css = "css/skins/skin-black-light.min.css"
skin_purple_css = "css/skins/skin-purple.min.css"
skin_purple_light_css = "css/skins/skin-purple-light.min.css"
skin_yellow_css = "css/skins/skin-yellow.min.css"
skin_yellow_light_css = "css/skins/skin-yellow-light.min.css"
skin_red_css = "css/skins/skin-red.min.css"
skin_red_light_css = "css/skins/skin-red-light.min.css"
skin_green_css = "css/skins/skin-green.min.css"
skin_green_light_css = "css/skins/skin-green-light.min.css"

skin_colors_css = (
    (skin_blue_css, _("Blue")),
    (skin_blue_light_css, _("Blue Light")),
    (skin_black_css, _("Black")),
    (skin_black_light_css, _("Black Light")),
    (skin_purple_css, _("Purple")),
    (skin_purple_light_css, _("Purple Light")),
    (skin_yellow_css, _("Yellow")),
    (skin_yellow_light_css, _("Yellow Light")),
    (skin_red_css, _("Red")),
    (skin_red_light_css, _("Red Light")),
    (skin_green_css, _("Green")),
    (skin_green_light_css, _("Green Light")),
)

register_setting(
    name="ADMINLTE_SKIN_CSS",
    label=_("Website Color Skin Css"),
    description=_("Change the Color of the Website, it have to be the same value as Skin Color"),
    editable=True,
    choices=skin_colors_css,
    default=skin_blue_css,
)

layout_fixed = "fixed"
layout_boxed = "layout-boxed"
layout_top_nav = "layout-top-nav"
layout_sidebar_collapse = "sidebar-collapse"
layout_sidebar_mini = "sidebar-mini"

layout = (
    (layout_fixed, _("Fixed")),
    (layout_boxed, _("Layout Boxed")),
    (layout_top_nav, _("Layout Top Nav")),
    (layout_sidebar_collapse, _("Sidebar Collapse")),
    (layout_sidebar_mini, _("Sidebar Mini")),
)

register_setting(
    name="ADMINLTE_LAYOUT",
    label=_("Website Layout"),
    description=_("Change the Layout of the Website"),
    editable=True,
    choices=layout,
    default=layout_sidebar_mini,
)


register_setting(
    name="COOKIE_LAW_HEADER",
    label=_("Cookie law header"),
    description=_("Cookie law header"),
    editable=True,
    default="COOKIE_LAW_HEADER",
    translatable=True,
)

register_setting(
    name="COOKIE_LAW_CONTENT",
    label=_("Cookie law content"),
    description=_("Cookie law content"),
    editable=True,
    default="COOKIE_LAW_CONTENT",
    translatable=True,
)

register_setting(
    name="COOKIE_LAW_BUTTON",
    label=_("Cookie law Button"),
    description=_("Cookie law Button"),
    editable=True,
    default="OK",
    translatable=True,
)

register_setting(
    name="COOKIE_LAW_PRIVACY",
    label=_("Cookie law Privacy Link"),
    description=_("Cookie law Privacy Link"),
    editable=True,
    default="#",
    translatable=True,
)

register_setting(
    name="COOKIE_LAW_PRIVACY_TEXT",
    label=_("Cookie law Privacy Link Text"),
    description=_("Cookie law Privacy Link Text"),
    editable=True,
    default="Privacy Law",
    translatable=True,
)
