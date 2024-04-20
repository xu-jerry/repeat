import reflex as rx

from repeat.template import template
from gemini.recipes import generate_recipe, recipe_ingredients

class FormState(rx.State):
    form_data: dict = {}
    lines = []
    recipe = ""

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        recipe = generate_recipe(self.form_data["ingredients"])
        self.recipe = recipe
        self.lines = recipe.split('\n')

    def recipe_info(self):
        """Test recipe_ingredients"""
        recipe_ingredients()

@template
def recipes() -> rx.Component:
    return rx.box(
            rx.box(
                rx.text("Recipes"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            rx.foreach(FormState.lines, lambda line: rx.box(
                rx.text(line))),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Ingredients",
                        name="ingredients",
                    ),
                    rx.button("Submit", type="submit"),
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.button("Ingredients", on_click=FormState.recipe_info),
            padding_left="250px",
        )
