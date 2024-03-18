import flet as ft


def main(page:ft.Page):
    page.title = "Routes Example"

    print("ruta inicial: ", page.route)

    def ir_configuraciones(e):
        page.go("/settings")

    def ir_mail_configuraciones(e):
        page.go("/setting/mail")

    def cambio_ruta(e):
        print("Cambio de ruta: ", e.route)
        page.views.clear()
        page.views.append(
            ft.View(
                "/", #inicio 
                [
                    ft.AppBar(
                        title=ft.Text("Flet application")
                    ),
                    ft.ElevatedButton(
                        "Ir a configuraciones",
                        on_click=abrir_configuraciones
                    ),

                ],

            )
        )
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        ft.AppBar(
                            title=ft.Text("Settings"),
                            bgcolor=ft.colors.SURFACE_VARIANT
                        ),
                        ft.Text("Settenigs!", style="bodyMedium"),
                        ft.ElevatedButton(
                            "Go to mail settings",
                            on_click=abrir_email_configuraciones
                        )
                    ]
                )
            )

        if page.route =="/settings/mail":
            page.views.append(
                ft.View(
                    "/settings/mail",
                    [
                        ft.AppBar(
                            title= ft.Text("Mail configuracion"),
                        ),
                        ft.Text("Mail Settings")
                    ]
                )
            )

        page.update()

    def ventana_emergente(e):
        print("View pop: ", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = cambio_ruta
    page.on_view_pop = ventana_emergente

    def abrir_email_configuraciones(e):
        page.go("/settings/mail")

    def abrir_configuraciones(e):
        page.go("/settings")

    page.go(page.route)

ft.app(target=main, view=ft.WEB_BROWSER)