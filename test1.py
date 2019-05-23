#!/usr/bin/env python3
from npyscreen import *  # Which comes from pip



class MyApp(NPSAppManaged):
    def onStart(self):
        self.registerForm('MAIN',MainForm())

class MainForm(Form):
    def create(self):
        self.add(TitleText, name='Text:', value='Hello world' )

    def afterEditing(self):
        self.parentApp.setNextForm(None)


if __name__=="__main__":
    ta = MyApp()
    ta.run()


