import kivy
kivy.require('1.0.6') # 注意要把这个版本号改变成你现有的Kivy版本号!

from kivy.app import App # 译者注：这里就是从kivy.app包里面导入App类
from kivy.uix.label import Label # 译者注：这里是从kivy.uix.label包中导入Label控件，这里都注意开头字母要大写

class MyApp(App):

        def build(self): # 译者注：这里是实现build()方法
                    return Label(text='Hello world') # 译者注：在这个方法里面使用了Label控件

if __name__ == '__main__':
    MyApp().run() # 译者注：这里就是运行了。
                            
    '''
    译者注：这一段的额外添加的备注是给萌新的.
    就是要告诉萌新们，一定要每一句每一个函数每一个变量甚至每一个符号，都要读得懂！！！
    如果是半懂不懂的状态，一定得学透了，要不然以后早晚得补课.
    这时候又让我想起了结构化学。
    总之更详细的内容后面会有，大家加油。
    '''
