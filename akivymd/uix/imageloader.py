from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivy.animation import Animation
from kivymd.theming import ThemableBehavior

__all__ = ('AKImageLoader')
Builder.load_string(
    """
<AKImageLoader>:
    source: ' '
    canvas.before:
        Color:
            rgba: root.theme_cls.bg_darkest
            a: root.fr_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(self.size[0]/2,self.size[1]/2) , (self.size[0]/2,self.size[1]/2),(self.size[0]/2,self.size[1]/2),(self.size[0]/2,self.size[1]/2) ] if root.circle==True else [(dp(20),dp(20)) , (dp(20),dp(20)) , (dp(20),dp(20)) , (dp(20),dp(20)) ]
        Color:
            rgba: root.theme_cls.bg_dark
            a: root.bg_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(self.size[0]/2,self.size[1]/2) , (self.size[0]/2,self.size[1]/2),(self.size[0]/2,self.size[1]/2),(self.size[0]/2,self.size[1]/2) ] if root.circle==True else [(dp(20),dp(20)) , (dp(20),dp(20)) , (dp(20),dp(20)) , (dp(20),dp(20)) ]

"""
)


class AKImageLoader(ThemableBehavior, AsyncImage):

    bg_rec_opacity = NumericProperty(0)
    fr_rec_opacity = NumericProperty(0)
    circle = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_anim = None

    def _check_source(self, source):
        if source == False or len(source.strip()) == 0:
            self.source = ' '
            return False
        else:
            return True

    def _start_animate(self):
        self.bg_rec_opacity = 1
        self.fr_rec_opacity = 1
        self.color = [1, 1, 1, 0]
        duration = 0.8

        self.start_anim = Animation(bg_rec_opacity=1, t='in_quad', duration=duration)\
            + Animation(bg_rec_opacity=0, t='out_quad', duration=duration)
        self.start_anim.repeat = True
        self.start_anim.start(self)

    def _stop_animate(self):
        duration = 0.8

        self.color = [1, 1, 1, 1]
        if self.start_anim:
            self.start_anim.cancel_all(self)
            self.stop_anim = Animation(
                fr_rec_opacity=0, t='out_quad', duration=0.1)
            self.stop_anim &= Animation(
                bg_rec_opacity=0, t='out_quad', duration=0.1)
            self.stop_anim.start(self)

    def on_source(self, *args):
        if self._check_source(self.source):
            self._stop_animate()
        else:
            self._start_animate()
