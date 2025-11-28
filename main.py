from nicegui import ui

# Define page
@ui.page('/')
def main_page():
    with ui.element('div').classes('relative w-full h-screen overflow-hidden'):
        # 🔹 Background video
        ui.video(
            #'./static/piano.mp4',  # place your video in 'static/' folder
            'https://storage.googleapis.com/tardy-website/ski.mp4',  # place your video in 'static/' folder
            autoplay=True,
            loop=True,
            muted=True,
        ).classes('absolute inset-0 w-full h-full object-cover')

        # 🔹 Overlay gradient for better text contrast
        ui.element('div').classes(
            'absolute inset-0 bg-gradient-to-t from-black/60 to-transparent'
        )

        # 🔹 Centered text & button content
        with ui.element('div').classes(
            'absolute inset-0 flex flex-col items-center justify-center text-center text-white z-10'
        ):
            ui.image('./static/tardy_white.png').classes('w-1/4 opacity-50')
            #ui.label('Your Ski').classes('text-5xl font-light mb-2')
            #ui.label('Our Art').classes('text-5xl font-bold mb-8')
            ui.button('BUY NOW', on_click=lambda: ui.notify('Get Started!')).classes(
                'mt-12 bg-white text-black px-6 py-3 rounded-full font-semibold hover:bg-gray-200 transition'
            )
            #ui.label('Start for free. No credit card required.').classes(
            #    'text-sm mt-4 text-gray-200'
            #)

# Run the app
ui.run(title='Ski Bois Tardy', favicon='🌐')
