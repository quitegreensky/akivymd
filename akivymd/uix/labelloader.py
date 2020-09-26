from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.animation import Animation

__all__ = ('AKLabelLoader')

Builder.load_string(
    """

<AKLabelLoader>:
    canvas.before:
        Color:
            rgba: root.theme_cls.bg_darkest
            a: root.fr_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(dp(20),dp(20)) , (dp(20),dp(20)),(dp(20),dp(20)),(dp(20),dp(20)) ]
        Color:
            rgba: root.theme_cls.bg_dark
            a: root.bg_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(dp(20),dp(20)) , (dp(20),dp(20)),(dp(20),dp(20)),(dp(20),dp(20)) ]

"""
)


class AKLabelLoader(MDLabel):

    bg_rec_opacity = NumericProperty(0)
    fr_rec_opacity = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_anim = None
        Clock.schedule_once(lambda x: self._update(self.text))

    def _update(self, text):
        if self._check_text(text):
            self._stop_animate()
        else:
            self._start_animate()

    def _check_text(self, text):
        if not text:
            return False
        else:
            return True

    def _start_animate(self):
        self.bg_rec_opacity = 1
        self.fr_rec_opacity = 1
        duration = 0.8
        self.start_anim = Animation(bg_rec_opacity=1, t='in_quad', duration=duration)\
            + Animation(bg_rec_opacity=0, t='out_quad', duration=duration)
        self.start_anim.repeat = True
        self.start_anim.start(self)

    def _stop_animate(self):
        duration = 0.8

        if self.start_anim:
            self.start_anim.cancel_all(self)

        if self.bg_rec_opacity != 0 and self.fr_rec_opacity != 0:
            self.stop_anim = Animation(
                fr_rec_opacity=0, t='out_quad', duration=duration)
            self.stop_anim &= Animation(
                bg_rec_opacity=0, t='out_quad', duration=duration)
            self.stop_anim.start(self)

    def on_text(self, *args):
        if self._check_text(self.text):
            self._stop_animate()
        else:
            self._start_animate()
