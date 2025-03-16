import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image

class PhotoManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.file_chooser = FileChooserIconView(on_selection=self.display_photos)
        self.add_widget(self.file_chooser)
        
        self.button_sort = Button(text="Sort Photos by Size", on_press=self.sort_photos)
        self.add_widget(self.button_sort)
        
        self.photo_display = BoxLayout(size_hint_y=None, height=500)
        self.add_widget(self.photo_display)

    def display_photos(self, filechooser, selected):
        self.photo_display.clear_widgets()
        for photo in selected:
            image = Image(source=photo)
            self.photo_display.add_widget(image)

    def sort_photos(self, instance):
        photos = self.file_chooser.selection
        if photos:
            sorted_photos = sorted(photos, key=lambda photo: os.path.getsize(photo))
            self.display_photos(None, sorted_photos)

class PhotoApp(App):
    def build(self):
        return PhotoManager()

if __name__ == '__main__':
    PhotoApp().run()
