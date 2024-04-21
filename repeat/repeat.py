"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from repeat.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from .state.base import State
from repeat.pages.login import login
from repeat.pages.signup import signup
from repeat.pages.recipes import recipes
from repeat.pages.inventory import inventory
from repeat.pages.index import index
from repeat.pages.chat import chat
from repeat.pages.resources import resources
from repeat.pages.profile import profile
from repeat.pages.example_recipe import example_recipe

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/", on_load=State.check_login())
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")
app.add_page(recipes, route="/recipes")
app.add_page(inventory, route="/inventory")
app.add_page(chat, route="/chat")
app.add_page(resources, route="/resources")
app.add_page(profile, route="/profile")
app.add_page(example_recipe, route="/baked_potato_recipe")