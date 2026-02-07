# objects.py
import flet as fl
from data import temp_save


def panel_creator_objects(page: fl.Page):

    # ╔¤═══════¤OBJETOS AGREGADOS¤════════¤╗
    objetos_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_objeto(objeto_name):
        def handler(e):
            temp_save.remove_objeto(objeto_name)
            for control in objetos_list.controls:
                if control.data == objeto_name:
                    objetos_list.controls.remove(control)
                    break
            page.update()

        return handler

    def create_onlist_objeto(objeto):
        objeto_name = objeto["name"]
        return fl.Container(
            data=objeto_name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Icon(fl.Icons.INVENTORY_2, color="#9C27B0"),
                            fl.Text(
                                objeto_name,
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
                        tooltip="Eliminar objeto",
                        on_click=fl_delete_objeto(objeto_name),
                    ),
                ],
                alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#2D2D2D",
            border_radius=8,
            padding=fl.padding.only(left=15, top=8, bottom=8, right=8),
        )

    # ╚¤═══════¤OBJETOS AGREGADOS¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_objeto_name = fl.TextField(
        label="Nombre del objeto",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    def fl_add_objeto(e):
        if not input_objeto_name.value:
            return

        objeto = temp_save.add_objeto(name=input_objeto_name.value)
        objetos_list.controls.append(create_onlist_objeto(objeto))
        input_objeto_name.value = ""
        page.update()

    addobjeto_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#9C27B0",
        color="white",
        height=45,
        on_click=fl_add_objeto,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_objetos = fl.Row(
        controls=[
            fl.Text(
                "📦 Objetos",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_objeto_name,
                    addobjeto_button,
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
                header_objetos,
                fl.Divider(height=10, color="#3D3D3D"),
                objetos_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )
