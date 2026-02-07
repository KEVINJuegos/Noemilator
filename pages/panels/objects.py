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

    def fl_update_quantity(objeto_name):
        def handler(e):
            new_value = e.control.value
            if new_value == "":
                new_value = 0
            temp_save.update_objeto_quantity(objeto_name, int(new_value))

        return handler

    def create_onlist_objeto(objeto):
        return fl.Container(
            data=objeto.name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Icon(fl.Icons.INVENTORY_2, color="#9C27B0"),
                            fl.Text(
                                objeto.name,
                                size=16,
                                weight=fl.FontWeight.W_500,
                                color="white",
                            ),
                        ],
                        spacing=10,
                    ),
                    fl.Row(
                        controls=[
                            fl.Text(
                                "Cantidad:",
                                size=13,
                                color="#B0B0B0",
                            ),
                            fl.TextField(
                                value=str(objeto.quantity),
                                bgcolor="#3D3D3D",
                                border_color="#858585",
                                color="white",
                                width=70,
                                height=40,
                                text_size=13,
                                text_align=fl.TextAlign.CENTER,
                                input_filter=fl.NumbersOnlyInputFilter(),
                                on_change=fl_update_quantity(objeto.name),
                            ),
                            fl.IconButton(
                                icon=fl.Icons.DELETE,
                                icon_color="#F44336",
                                icon_size=20,
                                tooltip="Eliminar objeto",
                                on_click=fl_delete_objeto(objeto.name),
                            ),
                        ],
                        spacing=5,
                        vertical_alignment=fl.CrossAxisAlignment.CENTER,
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

    input_objeto_quantity = fl.TextField(
        label="Cantidad",
        value="0",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=80,
        height=50,
        text_size=13,
        text_align=fl.TextAlign.CENTER,
        input_filter=fl.NumbersOnlyInputFilter(),
    )

    def fl_add_objeto(e):
        if not input_objeto_name.value:
            return

        if not input_objeto_quantity.value or input_objeto_quantity.value == "":
            input_objeto_quantity.value = "0"
            quantity = 0
        else:
            quantity = int(input_objeto_quantity.value)

        objeto = temp_save.add_objeto(
            name=input_objeto_name.value,
            quantity=quantity,
        )
        objetos_list.controls.append(create_onlist_objeto(objeto))
        input_objeto_name.value = ""
        input_objeto_quantity.value = "0"
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
                    input_objeto_quantity,
                    addobjeto_button,
                ],
                spacing=10,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
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
