# places.py
import flet as fl
from data import temp_save


def panel_creator_places(page: fl.Page):

    # ╔¤═══════¤LUGARES AGREGADOS¤════════¤╗
    lugares_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_lugar(lugar_name):
        def handler(e):
            temp_save.remove_lugar(lugar_name)
            for control in lugares_list.controls:
                if control.data == lugar_name:
                    lugares_list.controls.remove(control)
                    break
            page.update()

        return handler

    def create_onlist_lugar(lugar):
        lugar_name = lugar["name"]
        return fl.Container(
            data=lugar_name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Icon(fl.Icons.PLACE, color="#2196F3"),
                            fl.Text(
                                lugar_name,
                                size=16,
                                weight=fl.FontWeight.W_500,
                                color="white",
                            ),
                        ],
                        spacing=10,
                    ),
                    fl.IconButton(
                        icon=fl.Icons.DELETE,
                        icon_color="#F44336",
                        icon_size=20,
                        tooltip="Eliminar lugar",
                        on_click=fl_delete_lugar(lugar_name),
                    ),
                ],
                alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#2D2D2D",
            border_radius=8,
            padding=fl.padding.only(left=15, top=8, bottom=8, right=8),
        )

    # ╚¤═══════¤LUGARES AGREGADOS¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_lugar_name = fl.TextField(
        label="Nombre del lugar",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    def fl_add_lugar(e):
        if not input_lugar_name.value:
            return

        lugar = temp_save.add_lugar(name=input_lugar_name.value)
        lugares_list.controls.append(create_onlist_lugar(lugar))
        input_lugar_name.value = ""
        page.update()

    addlugar_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#2196F3",
        color="white",
        height=45,
        on_click=fl_add_lugar,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_lugares = fl.Row(
        controls=[
            fl.Text(
                "📍 Lugares",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_lugar_name,
                    addlugar_button,
                ],
                spacing=10,
            ),
        ],
        alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=fl.CrossAxisAlignment.CENTER,
    )
    # ╚¤═══════¤HEADER¤════════¤╝

    return fl.Container(
        content=fl.Column(
            controls=[
                header_lugares,
                fl.Divider(height=10, color="#3D3D3D"),
                lugares_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )
