from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref, ref_computed, effect
from dataclasses import dataclass


#region 反应式方法1  不太好
# def onchange():
#     label.text = input.value

# label = ui.label()

# input = ui.input("演示数据绑定",on_change=onchange)

# endregion


#region 反应式方法2  不太好
# @dataclass
# class DataMo(object):
#     """Docstring for ClassName"""
#     content1 = ''
#     content2 = ''

#     @property
#     def result(self):
#         # print('result runned')
#         return self.content1 + self.content2

# dm = DataMo()
# label1 = ui.label().bind_text(dm, "content1")
# label2 = ui.label().bind_text(dm, "content2")

# input1 = ui.input("演示数据绑定").bind_value(dm, "content1")
# input2 = ui.input("演示数据绑定").bind_value(dm, "content2")
# label = ui.label().bind_text(dm, "result")
#endregion


#region
content1 = to_ref('')
content2 = to_ref('')
use_input2 = to_ref(True)

@ref_computed
def result():
    print("result runned!!!")
    if use_input2.value:
        return content1.value + content2.value
    return content1.value 
# result = ref_computed(lambda : content1.value + content2.value)

input1 = rxui.input("演示数据绑定", value=content1)

rxui.switch("使用input2内容", value=use_input2)

input2 = rxui.input("演示数据绑定", value=content2)

label1 = rxui.label(content1)
label2 = rxui.label(content2)
label = rxui.label(result)


#endregion
ui.run()