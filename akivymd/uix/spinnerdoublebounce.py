from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty , ListProperty ,StringProperty, BooleanProperty
from kivymd.theming import ThemableBehavior
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp

Builder.load_string("""
<AKSpinnerDoubleBounce>:
    size_hint: None, None
    size: root.spinner_size , root.spinner_size
    canvas:
        Color:
            rgba: root.theme_cls.primary_color    
        Ellipse:
            size:  root._circle_size1
            pos: [ self.x+self.width/2 - root._circle_size1[0]/2  , self.y+self.height/2 - root._circle_size1[1]/2 ]
        
        Color:
            rgba: root.theme_cls.primary_light
        Ellipse:
            size:  root._circle_size2
            pos: [ self.x+self.width/2 - root._circle_size2[0]/2  , self.y+self.height/2 - root._circle_size2[1]/2 ]
                    
""")


class AKSpinnerDoubleBounce(ThemableBehavior , Widget):
    spinner_size = NumericProperty(48)
    active = BooleanProperty(False)
    speed= NumericProperty(0.5)

    _circle_size1 = ListProperty([0,0])
    _circle_size2 = ListProperty([0,0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def _update(self , size ):
        self._circle_size1 = [size,size]
        self._circle_size2 = [0,0]
        self._start_animate(size)

    def _start_animate(self , size):
        self.anim0 = Animation(_circle_size1=[size,size] ,opacity=1, t='out_quad' , duration=self.speed)

        self.anim1 = Animation(_circle_size1 = [size/2, size/2] , t='in_quad' , duration=self.speed)\
            + Animation(_circle_size1 = [size, size], t='out_quad', duration=self.speed)

        self.anim2 = Animation(_circle_size2 = [size/2, size/2] ,opacity=1, t='in_quad', duration=self.speed)\
            + Animation(_circle_size2 = [0, 0], t='out_quad', duration=self.speed)

        self.anim1.repeat= True
        self.anim2.repeat= True

        self.anim0.start(self)
        Clock.schedule_once(lambda x:self.anim1.start(self) , self.speed)
        Clock.schedule_once(lambda x:self.anim2.start(self) , self.speed)

    def _stop_animate(self):
        self.anim0.cancel_all(self)
        self.anim1.cancel_all(self) 
        self.anim2.cancel_all(self) 
        self.anim1_stop = Animation(_circle_size1 = [0, 0] ,opacity=0, t='in_quad' , duration=0.1)
        self.anim2_stop = Animation(_circle_size2 = [0, 0] ,opacity=0, t='in_quad' , duration=0.1)
        self.anim1_stop.start(self)
        self.anim2_stop.start(self)
        
    def on_active(self,*args):
        size= self.size[0]
        if self.active:
            self._start_animate(size)
        else:
            self._stop_animate()

