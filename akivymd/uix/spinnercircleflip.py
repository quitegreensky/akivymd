from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty , ListProperty ,StringProperty,BooleanProperty
from kivymd.theming import ThemableBehavior
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
Builder.load_string("""

<AKSpinnerCircleFlip>:
    size_hint: None, None
    size: root.spinner_size , root.spinner_size
    canvas:
        Color:
            rgba: root.theme_cls.primary_color
        Ellipse:
            size:  root._circle_size
            pos: [ self.x+self.width/2 - root._circle_size[0]/2  , self.y+self.height/2 - root._circle_size[1]/2 ]
          
""")


class AKSpinnerCircleFlip(ThemableBehavior,Widget):
    spinner_size = NumericProperty(48) 
    speed = NumericProperty(0.3)
    animation= StringProperty('out_back')
    active = BooleanProperty(False)

    _circle_size = ListProperty([0,0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def _start_animate(self , size):
        size = [size,size]
        self.flip_v_start = Animation(_circle_size = [size[0] , size[1]],opacity = 1, duration = self.speed  , t=self.animation  )
        self.flip_v = Animation(_circle_size = [size[0] , 0], duration = self.speed  , t=self.animation  ) \
            + Animation(_circle_size = [size[0] , size[1]], duration = self.speed  , t=self.animation  )\
            + Animation(_circle_size = [0 , size[1]], duration = self.speed  , t=self.animation  )\
            + Animation(_circle_size = [size[0] , size[1]], duration = self.speed  , t=self.animation  )

        self.flip_v.repeat = True
        self.flip_v_start.start(self)
        Clock.schedule_once(lambda x:self.flip_v.start(self) , self.speed)

    def _stop_animate(self):
        self.flip_v_start.cancel_all(self)
        self.flip_v.cancel_all(self)
        self.flip_v_stop =  Animation(_circle_size = [0 , 0],opacity = 0, duration = 0.1 , t=self.animation  )
        self.flip_v_stop.start(self)

    def on_active(self,*args):
        size= self.size[0]
        if self.active:
            self._start_animate(size)
        else:
            self._stop_animate()