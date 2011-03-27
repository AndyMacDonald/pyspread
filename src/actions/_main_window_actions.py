#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6 on Sun May 25 23:31:23 2008

# Copyright 2008 Martin Manns
# Distributed under the terms of the GNU General Public License
# generated by wxGlade 0.6 on Mon Mar 17 23:22:49 2008

# --------------------------------------------------------------------
# pyspread is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyspread is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyspread.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------


"""
_main_window_actions.py
=======================

Module for main window level actions.
All non-trivial functionality that results from main window actions
and belongs to the application as whole (in contrast to the grid only)
goes here.

Provides:
---------
  1. FileActions: Actions which affect the pys file
  2. ExchangeActions: Actions for foreign format import and export
  3. PrintActions: Actions for printing
  4. ClipboardActions: Actions which affect the clipboard
  5. FindActions: Actions for finding and replacing
  6. MacroActions: Actions which affect macros  
  7. HelpActions: Actions for getting help
  8. AllMainWindowActions: All main window actions as a bundle

"""

import os

import wx
import wx.html

from config import DEFAULT_FILENAME, HELP_SIZE, HELP_DIR

class FileActions(object):
    """Actions which affect the pys file"""
    
    def __init__(self, filename):
        self.filename = filename
        
    def new(self, dim):
        """Creates a new spreadsheet file"""
        
        self.filename = DEFAULT_FILENAME
        
        raise NotImplementedError
        
    def open(self):
        raise NotImplementedError
        
    def save(self):
        raise NotImplementedError

    def approve(self):
        raise NotImplementedError


class ExchangeActions(object):
    """Actions for foreign format import and export"""
    
    def __import(self):
        raise NotImplementedError

    def export(self):
        raise NotImplementedError


class PrintActions(object):
    """Actions for printing"""
    
    def __print(self):
        raise NotImplementedError


class ClipboardActions(object):
    """Actions which affect the clipboard"""
    
    def cut(self):
        raise NotImplementedError
        
    def copy(self):
        raise NotImplementedError
    
    def copy_result(self):
        raise NotImplementedError
    
    def paste(self):
        raise NotImplementedError


class FindActions(object):
    """Actions for finding inside the grid"""
    
    def find(self):
        raise NotImplementedError
        
    def replace(self):
        raise NotImplementedError


class MacroActions(object):
    """Actions which affect macros"""
    
    def show(self):
        raise NotImplementedError
    
    def open(self):
        raise NotImplementedError
        
    def save(self):
        raise NotImplementedError


class HelpActions(object):
    """Actions for getting help"""
    
    def launch_help(self, helpname, filename):
        """Generic help launcher"""
        
        # Set up window
        
        help_window = wx.Frame(self.main_window, -1, helpname, 
                            wx.DefaultPosition, wx.Size(*HELP_SIZE))
        help_htmlwindow = wx.html.HtmlWindow(help_window, -1, 
                            wx.DefaultPosition, wx.Size(*HELP_SIZE))
        
        # Get help data
        current_path = os.getcwd()
        os.chdir(HELP_DIR)
        help_file = open(filename, "r")
        help_html = help_file.read()
        help_file.close()
        
        # Show tutorial window
        
        help_htmlwindow.SetPage(help_html)
        help_window.Show()
        
        os.chdir(current_path)
        
    
class AllMainWindowActions(FileActions, ExchangeActions, PrintActions, 
                           ClipboardActions, FindActions, MacroActions,
                           HelpActions):
    """All main window actions as a bundle"""
    
    def __init__(self, main_window):
        self.main_window = main_window
