from nicegui import ui, app

#add static dir
app.add_static_files('/static', 'static')

# Define page
@ui.page('/')
def main_page():

    # --- FULLSCREEN HERO VIDEO SECTION ---
    with ui.element('div').classes('relative w-full h-screen overflow-hidden'):
        # Background video
        """
        ui.video(
            'https://storage.googleapis.com/tardy-website/ski.mp4',
            autoplay=True,
            loop=True,
            muted=True,
        ).classes('absolute inset-0 w-full h-full object-cover')
        """
        ui.video(
            '/static/reel.mp4',
            autoplay=True,
            loop=True,
            muted=True,
        ).classes('absolute inset-0 w-full h-full object-cover')

        # Gradient overlay
        ui.element('div').classes(
            'absolute inset-0 bg-gradient-to-t from-black/60 to-transparent'
        )

        # Centered logo + button
        with ui.element('div').classes(
            'absolute inset-0 flex flex-col items-center justify-center text-center text-white z-10'
        ):
            ui.image('./static/tardy_white.png').classes('w-1/4 opacity-50')
            ui.button('BUY NOW', on_click=lambda: ui.run_javascript(\
                'document.getElementById("products").scrollIntoView({behavior: "smooth"});'
                )).classes('mt-12 bg-white text-black px-6 py-3 rounded-full font-semibold hover:bg-gray-200 transition')

    # --- PRODUCT SECTION BELOW THE VIDEO ---
    with ui.element('div').classes('w-full py-20 bg-gray-100 flex flex-col items-center'):
        ui.label('Our Products').classes('text-4xl font-bold mb-10').props('id="products"')

        # 4-column responsive grid
        with ui.element('div').classes(
            'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 auto-rows-fr w-11/12 max-w-7xl'
        ):
            products = \
                {'Pagu':{
                    'desc':'Ski de piste par excellence, il ravira les skieurs qui aiment tailler des virages courts sur pistes damées.',
                    'lst':[
                    "Leger Rocker avant",
                    "Cambre classique",
                    "Talon plat",
                    "Lignes de côtes : 130-73-111",
                    "Rayon de courbe : 11 m"],
                    'taille':['155 cm','160 cm','165 cm']
                    },
                'Monchu':{
                    'desc':'Ski de piste polyvalent avec un rayon plus long que le « Pagu ». Il permet de varier entre petits virages et grandes courbes sur piste. Aussi efficace en bords de pistes.',
                    'lst':[
                    "Leger Rocker avant",
                    "Cambre classique",
                    "Talon plat",
                    "Lignes de côtes : 125-80-105",
                    "Rayon de courbe : 16 m"],
                    'taille':['155 cm','160 cm','165 cm']
                    },
                'Gnolu':{
                    'desc':'A la recherche de polyvalence le « Gnolu est là. A l’aise sur piste comme dans la poudreuse ou encore dans le « Trafolle », le « Gnolu donne accès a tout le domaine skiable.',
                    'lst':[
                    "Rocker avant",
                    "Cambre classique",
                    "Talon plat",
                    "Lignes de côtes : 130-90-104",
                    "Rayon de courbe : 21 m"],
                    'taille':['155 cm','160 cm','165 cm']
                    },
                'Tramu':{
                    'desc':'De par sa longueur mini de 180cm le « Tramu » aime les grands « Tout droit » dans la poudreuse. Les virages courts ne sont pas dans son vocabulaire.',
                    'lst':[
                    "Long Rocker avant",
                    "Cambre classique",
                    "Talon plat ( Possibilité double Rocker)",
                    "Lignes de côtes : 133-105-120",
                    "Rayon de courbe : 30 m"],
                    'taille':['155 cm','160 cm','165 cm']
                    },
                }

            for key, desc in products.items():
                with ui.card().classes(
                    'shadow-xl p-6 hover:scale-105 transition rounded-xl '
                    'items-center justify-between text-center h-full flex flex-col'
                ):
                    ui.label(key).classes('text-2xl font-semibold mb-2')
                    ui.label(desc['desc']).classes('text-gray-600 mb-4')
                    with ui.label().classes('text-gray-600 mb-4'):
                        with ui.list().props('dense separator'):
                            for item in desc['lst']:
                                ui.item(item)
                    with ui.label('La taille').classes('text-gray-600 mb-4'):
                        with ui.list().props('dense separator'):
                            for item in desc['taille']:
                                ui.item(item)
                    with ui.label('Prix').classes('text-gray-600 mb-4'):
                        with ui.list().props('dense separator'):             
                            ui.item('880€ Skis nus')
                            ui.item('1040€ avec Look NX11')
                            ui.item('1110€ avec Look SPX 13')


                    ui.button('Order now', on_click=lambda: ui.run_javascript(
            'document.getElementById("contact").scrollIntoView({behavior: "smooth"});'
            )).classes(
                        'bg-black text-white px-4 py-2 rounded hover:bg-gray-800'
                    )

    # --- CONTACT SECTION ---
    with ui.element('div').classes(
        'w-full py-20 bg-white flex flex-col items-center border-t border-gray-300'
    ).props('id="contact"'):
        # Title
        ui.label('Contact Us').classes('text-4xl font-bold mb-6 text-gray-800')

        # Subtitle
        ui.label('We would love to hear from you!').classes(
            'text-lg text-gray-600 mb-12'
        )

        # Centered content box
        with ui.element('div').classes(
            'bg-gray-100 p-10 rounded-2xl shadow-xl w-11/12 max-w-3xl flex flex-col items-center gap-8'
        ):

            # Phone row
            with ui.row().classes('items-center'):
                ui.icon('call').classes('text-3xl text-black mr-4')
                ui.label('+33 6 12 34 56 78').classes('text-2xl text-gray-800')

            # Email row
            with ui.row().classes('items-center'):
                ui.icon('email').classes('text-3xl text-black mr-4')
                ui.label('contact@skitardy.com').classes('text-2xl text-gray-800')

            # Instagram row
            with ui.row().classes('items-center cursor-pointer'):
                ui.icon('instagram').classes(
                    'text-3xl text-pink-600 mr-4'
                )
                ui.link('Follow us on Instagram', 'https://instagram.com/yourhandle').classes(
                    'text-2xl text-gray-800 hover:underline'
                )

            # Facebook row
            with ui.row().classes('items-center cursor-pointer'):
                ui.icon('instagram').classes(
                    'text-3xl text-pink-600 mr-4'
                )
                ui.link('Follow us on Facebook', 'https://instagram.com/yourhandle').classes(
                    'text-2xl text-gray-800 hover:underline'
                )

    with ui.element('div').classes('w-full py-20 bg-gray-100 flex flex-col items-center'):
        # --- GOOGLE MAPS ---
        ui.label('Find Us').classes('text-3xl font-semibold mt-16 mb-6 text-gray-800')
        with ui.element('div').classes('w-1/2 h- flex justify-center'):
            # Note: Leaflet map could be used here, but embedding Google Maps for simplicity
            # leaftlet exa
            m = ui.leaflet(center=(45.841230851478734, 6.728182997997284))

            #45.841230851478734, 6.728182997997284


        """
        ui.html(
            '''
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10957.024999999998!2d6.7000!3d46.0000!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDYuwqAwMCcwMC4wIk4gNsKwNDAnMDAuMCJF!5e0!3m2!1sen!2sfr!4v0000000000000" 
                width="100%" 
                height="350" 
                style="border:0; border-radius: 15px; box-shadow: 0px 4px 20px rgba(0,0,0,0.1);" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
            '''
        ).classes('w-11/12 max-w-4xl')
        """

# Run the app
ui.run(title='Ski Bois Tardy', favicon='⛷️',reload=True)