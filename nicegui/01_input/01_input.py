# coding=utf-8

from nicegui import ui, Tailwind 

# 创建输入文本框
input01 = ui.input('演示', value="默认值").props('standout="bg-teal style="max-width:300px" autogrow text-white" clearable v-model="text" label="Please Input"')
# 输入框后面添加图标
with input01.add_slot('append'):
    ui.icon('event', color='green')
# 输入框前面添加图标
with input01.add_slot('prepend'):
    ui.icon('place', color='orange')


def on_change():
    print(input03.value)
    print(type(input03.value))

# 输入密码
# 方法1: 
input02 = ui.input('演示', value="默认值", password=True, password_toggle_button=True).props('standout="bg-teal text-white" outlined clearable')
# 方法2
# input02 = ui.input('演示', value="默认值" ).props('standout="bg-teal text-white" v-model="password" type="password" hind="Password" outlined clearable')


# 输入日期
input03 = ui.input('演示', value="2023-01-01", on_change=on_change).props('v-model="date" filled type="date" clearable') # hint="Native date"')

ui.run(native=True)