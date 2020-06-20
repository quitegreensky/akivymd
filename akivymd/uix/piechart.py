from kivy.lang.builder import Builder
from kivymd.app import MDApp
# from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, NumericProperty,StringProperty,BooleanProperty,OptionProperty
from kivy.clock import Clock
from kivy.graphics import Ellipse, Color, Rotate, PushMatrix,PopMatrix
from kivymd.theming import ThemableBehavior
from kivymd.color_definitions import palette, colors
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from akivymd.helper import point_on_circle
from kivy.core.window import Window 

'''issues
color_mode
'''

Builder.load_string(
    """
<PieChartNumberLabel>
    size_hint: None, None
    size: dp(40), dp(30)
    text: '%s\\n%d%%'%(root.title,root.percent)
    font_size: dp(10)
    halign: 'center'
    valign: 'center'
    font_style: 'Caption'
    theme_text_color: 'Custom'
    text_color: 1,1,1,1

<AKPieChart>:
    size_hint: None,None  

    """
)

class PieChartNumberLabel(MDLabel):
    percent= NumericProperty(0)
    title= StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class AKPieChart(ThemableBehavior, FloatLayout):
    chart_size= NumericProperty(100)
    items= ListProperty()
    order= BooleanProperty(True)
    starting_animation= BooleanProperty(True)
    transition= StringProperty('out_cubic')
    duration= NumericProperty(1)
    color_mode= OptionProperty('colors', options=['primary_color', 'accent_color']) # not solved 

    _pushed= False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self._on_resize)

    def _set_pos(self):
        if not self.pos_hint:
            return
        parent_size = self.parent.size 
        pos_hint = self.pos_hint
        for k,v in pos_hint.items():
            if k=='x':
                parent_size=[parent_size[0]*v, parent_size[1] ]
            elif k=='center_x':
                parent_size=[parent_size[0]*v-self.size[0]/2, parent_size[1] ]
            elif k=='right':
                parent_size=[parent_size[0]*v-self.size[0], parent_size[1] ]
            elif k=='y':
                parent_size=[parent_size[0], parent_size[1]*v ]
            elif k=='center_y':
                parent_size=[parent_size[0], parent_size[1]*v-self.size[1]/2 ]
            elif k=='bottom':
                parent_size=[parent_size[0], parent_size[1]*v-self.size[1] ]
            self.pos = parent_size
            
    def _format_items(self,items):
        percentage_sum= 0
        for k,v in items[0].items():
            percentage_sum+= v 

        if percentage_sum!=100:
            raise Exception('Sum of percenages must be 100')
        
        new_items={}
        for k,v in items[0].items():
            new_items[k]= 360*v/100
        
        if self.order:
            new_items= {k: v for k, v in sorted(new_items.items(), key=lambda item: item[1])}

        return new_items

    def _make_chart(self,items):
        self.size= [self.chart_size, self.chart_size]
        if not items:
            raise Exception('Items cannot be empty.') 

        items= self._format_items(items)
        self._set_pos()

        angle_start=0
        color_item= 0
        i= 1
        circle_center= [self.pos[0]+self.size[0]/2, self.pos[1]+self.size[1]/2]

        for title,value in items.items():
            with self.canvas.before:

                if self.starting_animation:
                    alpha= 0
                else:
                    alpha=1

                if self.color_mode=='colors':
                    color= get_color_from_hex(colors[palette[color_item]]['500']) 

                c= Color(rgb= color, a=alpha)
                if self.starting_animation:
                    e= Ellipse(pos=self.pos , size=self.size ,angle_start=angle_start, angle_end=angle_start+0.01)                    
                    
                    anim= Animation(size=self.size, angle_end=angle_start+value, duration=self.duration, t=self.transition)
                    anim_opcity= Animation(a=1, duration=self.duration*0.5)

                    anim_opcity.start(c)
                    anim.start(e)
                else: 
                    Ellipse(pos=self.pos , size=self.size ,angle_start=angle_start, angle_end=angle_start+value)
            color_item+=1
            angle_start+= value
                
        angle_start=0
        for title,value in items.items():
            with self.canvas.after:
                label_pos= point_on_circle( (angle_start+angle_start+value)/2 , circle_center, self.size[0]/3 )
                l= PieChartNumberLabel( pos=label_pos, title=title)
                anim_label= Animation(percent=value*100/360)
                anim_label.start(l)
            angle_start+= value

    def _clear_canvas(self):
        try:
            self.canvas.before.clear()
            self.canvas.after.clear()
        except:
            pass 

    def on_items(self,*args):
        self._clear_canvas()
        Clock.schedule_once(lambda x:self._make_chart(self.items), 0.1 )

    def _on_resize(self,instance , width , height):
        self._set_pos()
        self._clear_canvas()
        Clock.schedule_once(lambda x:self._make_chart(self.items), 0.1 )
