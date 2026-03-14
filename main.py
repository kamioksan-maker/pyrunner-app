from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import sys
import io

class PythonRunner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # 脚本输入区
        self.code_input = TextInput(
            text='print("Hello from Android📱!")\n\n# 在这里输入你的Python代码',
            size_hint=(1, 0.6),
            multiline=True,
            font_size=40
        )
        self.add_widget(self.code_input)
        
        # 运行按钮
        run_btn = Button(text='Run / 运行', size_hint=(1, 0.1), font_size=40)
        run_btn.bind(on_press=self.run_code)
        self.add_widget(run_btn)
        
        # 输出结果区
        self.output_label = Label(
            text='Output will appear here... / 输出结果', 
            size_hint=(1, 0.3),
            font_size=35
        )
        self.add_widget(self.output_label)
        
    def run_code(self, instance):
        code = self.code_input.text
        
        # 捕获 print 输出
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        
        try:
            # 执行 Python 代码
            exec(code)
            output = redirected_output.getvalue()
            if not output:
                output = "Code executed successfully. (No output)"
        except Exception as e:
            output = f"Error: {str(e)}"
        finally:
            sys.stdout = old_stdout
            
        self.output_label.text = output

class PyRunnerApp(App):
    def build(self):
        return PythonRunner()

if __name__ == '__main__':
    PyRunnerApp().run()
