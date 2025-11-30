"""
Basic website for Ski Bois Tardy using NiceGUI.
"""

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
        v = ui.video(
            '/static/output.mp4',
            autoplay=True,
            loop=True,
            muted=True,
            controls=False
        ).classes('absolute inset-0 w-full h-full object-cover')
        v.seek(41)  # Start video at 56 seconds

        # Gradient overlay
        ui.element('div').classes(
            'absolute inset-0 bg-gradient-to-t from-black/60 to-transparent'
        )

        # Centered logo + button
        with ui.element('div').classes(
            'absolute inset-0 flex flex-col items-center justify-center text-center text-white z-10'
        ):
            ui.image('./static/tardy_white.png').classes('w-1/4 opacity-50')
            ui.button('ACHETER', on_click=lambda: ui.run_javascript(\
                'document.getElementById("products").scrollIntoView({behavior: "smooth"});'
                )).classes('mt-12 bg-white text-black px-6 py-3 rounded-full font-semibold hover:bg-gray-200 transition')

    # --- PRODUCT SECTION BELOW THE VIDEO ---
    with ui.element('div').classes('w-full py-20 bg-gray-100 flex flex-col items-center'):
        ui.label('Nos produits').classes('text-4xl font-bold mb-10').props('id="products"')

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
                    ui.label(desc['desc']).classes('text-gray-600 mb-4 text-base')
                    with ui.label('Caractéristiques').classes('text-gray-600 mb-4 font-bold text-lg'):
                        with ui.list().props('dense separator'):
                            for item in desc['lst']:
                                ui.item(item).classes('text-base font-normal')
                    with ui.label('La taille').classes('text-gray-600 mb-4 font-bold text-lg'):
                        with ui.list().props('dense separator'):
                            for item in desc['taille']:
                                ui.item(item).classes('text-base font-normal')
                    with ui.label('Prix').classes('text-gray-600 mb-4 font-bold text-lg'):
                        with ui.list().props('dense separator'):             
                            ui.item('880€ Skis nus').classes('text-base font-normal')
                            ui.item('1040€ avec Look NX11').classes('text-base font-normal')
                            ui.item('1110€ avec Look SPX 13').classes('text-base font-normal')


                    ui.button('Acheter', on_click=lambda: ui.run_javascript(
            'document.getElementById("contact").scrollIntoView({behavior: "smooth"});'
            )).classes(
                        'bg-black text-white px-4 py-2 rounded hover:bg-gray-800'
                    )

    # --- CONTACT SECTION ---
    with ui.element('div').classes(
        'w-full py-20 bg-white flex flex-col items-center border-t border-gray-300'
    ).props('id="contact"'):
        # Title
        ui.label('Contactez-nous').classes('text-4xl font-bold mb-6 text-gray-800')

        # Subtitle
        ui.label('Nous serions ravis d\'avoir de vos nouvelles !').classes(
            'text-lg text-gray-600 mb-12'
        )

        # Centered content box
        with ui.element('div').classes(
            'bg-gray-100 p-10 rounded-2xl shadow-xl w-11/12 max-w-3xl flex flex-col items-center gap-8 text-center'
        ):

            # Phone row
            with ui.row().classes('items-center justify-center w-full'):
                ui.icon('call').classes('text-3xl text-black mr-4')
                ui.link(
                    '+33 6 11 48 77 98',
                    'tel:+33611487798'
                ).classes('text-2xl text-gray-800 hover:underline')

            # Phone row
            with ui.row().classes('items-center justify-center w-full'):
                ui.image('/static/410201-PD391H-802.png').classes(
                    'h-8 w-8 object-contain mr-4'
                )
                ui.link(
                    '+33 6 11 48 77 98',
                    'whatsapp:+33611487798'
                ).classes('text-2xl text-gray-800 hover:underline')

            # Email row
            with ui.row().classes('items-center justify-center w-full'):
                ui.icon('email').classes('text-3xl text-black mr-4')
                ui.link(
                    'cyril@skitardy.com',
                    'mailto:cyril@skitardy.com'
                ).classes('text-2xl text-gray-800 hover:underline')

            # Instagram row
            with ui.row().classes('items-center justify-center w-full cursor-pointer'):
                ui.image('/static/instagram.png').classes(
                    'h-8 w-8 object-contain mr-4'
                )
                ui.link(
                    'Suivez-nous sur Instagram',
                    'https://instagram.com/ski_bois_tardy'
                ).classes('text-2xl text-gray-800 hover:underline')

            # Facebook row
            with ui.row().classes('items-center justify-center w-full cursor-pointer'):
                ui.image('/static/Facebook_Logo_Primary.png').classes(
                    'h-8 w-8 object-contain mr-4'
                )
                ui.link(
                    'Suivez-nous sur Facebook',
                    'https://facebook.com/skiboistardy'
                ).classes('text-2xl text-gray-800 hover:underline')

     
    # --- partenaires SECTION BELOW THE VIDEO ---
    with ui.element('div').classes('w-full py-20 bg-gray-100 flex flex-col items-center'):
        ui.label('Nos partenaires').classes('text-4xl font-bold mb-10').props('id="partners"')

        # 4-column responsive grid
        with ui.element('div').classes(
            'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 auto-rows-fr w-11/12 max-w-7xl'
        ):
            
            partners = [['/static/telechargement.png','https://www.auvergnerhonealpes.fr/'],\
                        ['/static/stgervais_cdomaine-skiable.jpg','https://tourism.saintgervais.com/'],\
                        ['/static/Logo-Saint-Gervais-Mont-Blanc.png','https://tourism.saintgervais.com/'],\
                        ['/static/conta-logo.jpg','https://www.lescontamines.net/']]
            for key in partners:
                with ui.card().classes(
                    'shadow-xl p-6 hover:scale-105 transition rounded-xl '
                    'items-center justify-center text-center h-full flex flex-col'
                ):
                    ui.image(key[0]).on('click', lambda: ui.navigate.to(key[1], new_tab=True))

# Run the app
ui.run(title='Ski Bois Tardy', favicon='⛷️',reload=False)