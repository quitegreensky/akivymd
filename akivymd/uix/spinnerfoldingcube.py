from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty , ListProperty , BooleanProperty , StringProperty
from kivymd.theming import ThemableBehavior
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
Builder.load_string("""

<AKSpinnerFoldingCube>:
    size_hint: None, None
    size: root.spinner_size , root.spinner_size
    canvas:
        PushMatrix
        Rotate:
            axis: 0,0,1
            angle: root.angle
            origin: self.center    
        Color:
            rgba: root.theme_cls.primary_color
            a:root._cube1a
        Rectangle:
            size: root._cubeitem1
            pos: [self.x, self.y]
        Color:
            rgba: root.theme_cls.primary_color
            a:root._cube2a            
        Rectangle:
            size: root._cubeitem2
            pos: [self.x, self.y+self.height/2  ] 
        Color:
            rgba: root.theme_cls.primary_color
            a:root._cube3a            
        Rectangle:
            size: root._cubeitem3
            pos: [self.x+ self.width/2 , self.y+ self.height - root._cubeitem3[1]]
        Color:
            rgba: root.theme_cls.primary_color
            a:root._cube4a            
        Rectangle:
            size: root._cubeitem4
            pos: [self.x+ self.width - root._cubeitem4[0] , self.y]
        PopMatrix    
                    
""")


class AKSpinnerFoldingCube(ThemableBehavior,Widget):
    spinner_size = NumericProperty(48) 
    angle= NumericProperty(45)
    active = BooleanProperty(False)
    speed = NumericProperty(0.4)
    animation = StringProperty('out_cubic')

    _cubeitem1 = ListProperty([0,0])
    _cubeitem2 = ListProperty([0,0])
    _cubeitem3 = ListProperty([0,0])
    _cubeitem4 = ListProperty([0,0])
    _cube1a = NumericProperty(0)
    _cube2a = NumericProperty(0)
    _cube3a = NumericProperty(0)
    _cube4a = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _start_animate(self , size):
        size/=2
        self.cube_fold = Animation(_cubeitem1 = [size ,size] , _cube1a=1 , duration = self.speed, t=self.animation)\
            + Animation(_cubeitem2 = [size ,size] , _cube2a=1 , duration = self.speed, t=self.animation)\
            + Animation(_cubeitem3 = [size ,size], _cube3a=1 , duration = self.speed, t=self.animation)\
            + Animation(_cubeitem4 = [size ,size], _cube4a=1 , duration = self.speed, t=self.animation)\
            + Animation(_cubeitem4 = [0 ,size], _cube4a=0 , duration = self.speed, t=self.animation)\
            + Animation(_cubeitem3 = [size ,0], _cube3a=0 , duration = self.speed, t=self.animation)\
            + Animation(_cubeitem2 = [0 ,size] , _cube2a=0 , duration = self.speed, t=self.animation)\
            + Animation(_cubeitem1 = [size ,0] , _cube1a=0 , duration = self.speed, t=self.animation)\

        self.cube_fold.repeat = True
        self.cube_fold.start(self)

    def _update(self,size):
        self._cubeitem1 = [size/2,0 ]
        self._cubeitem2 = [0 , size/2]
        self._cubeitem3 = [size/2,0 ]
        self._cubeitem4 = [0 , size/2]

    def _stop_animate(self,size):
        size/=2
        self.cube_fold.cancel_all(self)
        self.cube_stop = Animation(_cubeitem4 = [0 ,size], _cube4a=0 , duration = 0.1, t=self.animation)\
            + Animation(_cubeitem3 = [size ,0], _cube3a=0 , duration = 0.1, t=self.animation)\
            + Animation(_cubeitem2 = [0 ,size] , _cube2a=0 , duration = 0.1, t=self.animation)\
            + Animation(_cubeitem1 = [size ,0] , _cube1a=0 , duration = 0.1, t=self.animation)\
        
        self.cube_stop.start(self)
        
    def on_active(self, *args):
        size = self.size[0]
        self._update(size)
        if self.active:
            self._start_animate(size) 
        else:
            self._stop_animate(size) 