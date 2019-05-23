#!/usr/bin/env python3
from npyscreen import *  # Which comes from pip
from curses import wrapper


def main(stdscr):
    stdscr.clear()

    my_form = Form()

    box1 = my_form.add_widget(TitleText, name="Your name:")
    url = my_form.add_widget(TitleText, name="Favorite url:")

    my_form.edit()


if __name__=="__main__":
    wrapper(main)

