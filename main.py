# main.py
import flet as fl
from pages.main_menu import main_menu
from pages.workspace import workspace


def main(page: fl.Page):
    page.title = "Noemilator"

    def navigator(e):
        page.views.clear()
        page.views.append(main_menu(page))

        if page.route == "/workspace":
            page.views.append(workspace(page))

        page.update()

    def navigator_back(e):
        page.views.pop()

        top_page = page.views[-1]
        page.go(top_page.route)  # type: ignore

    page.on_route_change = navigator
    page.on_view_pop = navigator_back

    page.go("/")  # Launch on main_menu.py


fl.app(target=main)
