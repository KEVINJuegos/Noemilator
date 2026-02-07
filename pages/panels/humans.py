# humans.py
import flet as fl
from data import temp_save


def panel_creator_humans(page: fl.Page):

    # ╔¤═══════¤HUMANOS AGREGADOS¤════════¤╗
    humanos_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_humano(humano_name):
        def handler(e):
            temp_save.remove_humano(humano_name)
            for control in humanos_list.controls:
                if control.data == humano_name:
                    humanos_list.controls.remove(control)
                    break
            page.update()

        return handler

    def create_onlist_humano(humano):
        return fl.Container(
            data=humano.name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Icon(fl.Icons.PERSON, color="#FF9800"),
                            fl.Text(
                                humano.name,
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
                        tooltip="Eliminar humano",
                        on_click=fl_delete_humano(humano.name),
                    ),
                ],
                alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#2D2D2D",
            border_radius=8,
            padding=fl.padding.only(left=15, top=8, bottom=8, right=8),
        )

    # ╚¤═══════¤HUMANOS AGREGADOS¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_humano_name = fl.TextField(
        label="Nombre del humano",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    def fl_add_humano(e):
        if not input_humano_name.value:
            return

        humano = temp_save.add_humano(name=input_humano_name.value)
        humanos_list.controls.append(create_onlist_humano(humano))
        input_humano_name.value = ""
        page.update()

    addhumano_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#FF9800",
        color="white",
        height=45,
        on_click=fl_add_humano,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_humanos = fl.Row(
        controls=[
            fl.Text(
                "🧑 Humanos",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_humano_name,
                    addhumano_button,
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
                header_humanos,
                fl.Divider(height=10, color="#3D3D3D"),
                humanos_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )
