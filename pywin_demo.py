from pywinauto.application import Application
import time
app = Application().start(r"control.exe")

time.sleep(3)
app = Application().connect(title=u'All Control Panel Items', class_name='CabinetWClass')
#cabinetwclass = app.CabinetWClass
window = app['All Control Panel Items']
print(window.print_control_identifiers(depth=2))
window.child_window(class_name="ToolbarWindow32")

'''
#https://pywinauto.readthedocs.io/en/latest/controls_overview.html
#notepad_window.print_control_identifiers(filename='output.txt')

#https://www.mbalslow.com/blog/article/how-to-get-started-gui-automation-pywinauto-python/
#https://medium.com/financeexplained
#https://blog.usejournal.com/how-to-automate-your-computer-with-python-d4d20a8e0b92
#https://github.com/blackrosezy/gui-inspect-tool


http://library.sadjad.ac.ir/opac/temp/18467.pdf
https://buildmedia.readthedocs.org/media/pdf/pytest/latest/pytest.pdf
https://github.com/hackebrot?tab=repositories
https://www.bountysource.com/issues/68393542-wait-operation-error
https://stackoverflow.com/questions/54767813/pywinauto-capture-as-image-adds-unwanted-borders

https://stackoverflow.com/questions/40252343/need-a-way-to-access-control-in-a-window-with-control-id-using-pywinauto
'''


from pywinauto.application import Application
import time
app = Application(backend="uia").start('control.exe')
time.sleep(5)


app = Application().connect(title=u'All Control Panel Items', class_name='CabinetWClass')
cabinetwclass = app.CabinetWClass
cabinetwclass.wait('ready')
#cabinetwclass.print_control_identifiers(filename='E:\\ramu_python_practise\info_ramu.txt')
cabinetwclass.AddressBarRoot.click_input()
#cabinetwclass.AddressBarRoot.type_keys('testdata')
#cabinetwclass.AddressBarRoot.type_keys("{1}{2}{3}") 
cabinetwclass.AddressBarRoot.type_keys('{ENTER}') 

#wait('enabled', timeout=20) 
