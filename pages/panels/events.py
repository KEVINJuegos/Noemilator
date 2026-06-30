# events.py
import flet as fl
from data import temp_save


def panel_creator_events(page: fl.Page):

    # ╔¤═══════¤EVENTOS LIST¤════════¤╗
    eventos_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_evento(evento_id):
        def handler(e):
            temp_save.remove_event(evento_id)
            for control in eventos_list.controls:
                if control.data == evento_id:
                    eventos_list.controls.remove(control)
                    break
            page.update()

        return handler

    def create_onlist_evento(evento):
        return fl.Container(
            data=evento.id,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Icon(fl.Icons.EVENT_NOTE, color="#FF9800"),
                            fl.Text(
                                f"#{evento.id}",
                                size=14,
                                weight=fl.FontWeight.BOLD,
                                color="#858585",
                            ),
                            fl.Text(
                                evento.name,
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
                        tooltip="Eliminar evento",
                        on_click=fl_delete_evento(evento.id),
                    ),
                ],
                alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#2D2D2D",
            border_radius=8,
            padding=fl.padding.only(left=15, top=8, bottom=8, right=8),
        )

    # ╚¤═══════¤EVENTOS LIST¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_event_name = fl.TextField(
        label="Nombre del evento",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    def fl_add_evento(e):
        if not input_event_name.value:
            return

        evento = temp_save.add_event(name=input_event_name.value)
        eventos_list.controls.append(create_onlist_evento(evento))
        input_event_name.value = ""
        page.update()

    addevent_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#FF9800",
        color="white",
        height=45,
        on_click=fl_add_evento,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_eventos = fl.Row(
        controls=[
            fl.Text(
                "📅 Eventos",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_event_name,
                    addevent_button,
                ],
                spacing=10,
            ),
        ],
        alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=fl.CrossAxisAlignment.CENTER,
    )
    # ╚¤═══════¤HEADER¤════════¤╝

    # Cargar datos existentes
    [eventos_list.controls.append(create_onlist_evento(e)) for e in temp_save.get_events()]  # fmt: skip

    return fl.Container(
        content=fl.Column(
            controls=[
                header_eventos,
                fl.Divider(height=10, color="#3D3D3D"),
                eventos_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )
