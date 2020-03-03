
#import objgraph
from pandas import DataFrame
import pandas as pd
from random import randint
from temp_reading1 import temperature_read
from functools import partial
from python_7_feb_2020 import Switch,AnalogGaugeWidget
#from keyboards import numerickeyboard,keyboard,capital_keyboard
from time import sleep
import time
import sqlite3
import gc
from datetime import datetime
#from PyQt5 import sip
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import math
#from PyQt5 import QtWidgets, uic,sip
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy
from pyqtgraph import AxisItem
from datetime import datetime, timedelta
from time import mktime
import psutil
#from PyQt5.QtWidgets import QScroller

# print("Try5: analoggaugewidget.py")
#from PyQt5.QtWidgets import QMainWindow

#from PyQt5.QtWidgets import QWidget
#from PyQt5.QtWidgets import QApplication
# QtWidgets -> QWidget
# QtWidgets -> QApplication

#from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont
#from PyQt5.QtGui import QPainter, QFontMetrics, QConicalGradient
# QtGui -> QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient

#from PyQt5.QtCore import Qt ,QTime, QTimer, QPoint, QPointF, QRect, QSize
#from PyQt5.QtCore import QObject, pyqtSignal

#from PyQt5.QtCore import QPropertyAnimation, QRectF, QSize, Qt, pyqtProperty
#from PyQt5.QtGui import QPainter
#from PyQt5.QtWidgets import (
    #QAbstractButton,
    #QApplication,
    #QHBoxLayout,
    #QSizePolicy,
    #QWidget,
#)
# class self(QWidget):
#     def __init__(self,name):
#        super().__init__() 
#        #parent=None
#        #super(secondwindow,self).__init__(parent)
#        #self.setGeometry(0, 100, 1024, 668)
#        self.title = "App2"
#        self.top = 0
#        self.left = 100
#        self.width = 1024
#        self.height = 668
#        self.name=name
#        self.InitUI1()class subwindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
class settingswindow(QWidget):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.mainwindow=mainwindow
       self.InitUI()
       #self.InitUI()
       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,0,1024,668)
        self.ins_settings = QPushButton('Instrument', self)
        self.ins_settings.setFont(QFont('Arial', 25))
        self.ins_settings.setGeometry(370,100,285,155)
        self.ins_settings.setStyleSheet('background-image: url(setting.png);')
        self.ins_settings.clicked.connect(self.instrumentsettingswindow)
        self.service = QPushButton('Service   ', self)
        self.service.setFont(QFont('Arial', 25))
        self.service.setGeometry(370,300,285,155)
        self.service.setStyleSheet('background-image: url(setting.png);')
        self.service.clicked.connect(self.servicewindow)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(370,490,280,100)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def instrumentsettingswindow(self):
        self.close()
        self.destroy()
        gc.collect()
        self.swindow = instrumentwindow(self.mainwindow)
        self.swindow.show()

    def servicewindow(self):
        pass
        #self.close()
        #self.svwindow = servicewindow()
        #self.svwindow.show()
    def call_first1(self):
        self.close()
        self.destroy()
        gc.collect()
        self.mainwindow.show()


class instrumentwindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.mainwindow=mainwindow
       self.InitUI()


       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.background = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.background.setPixmap(QPixmap('graph_screen.png'))
        self.background.setGeometry(0,0,1024,668)
        self.label = QLabel('Instrument Settings',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(400,20,220,50)
        self.home = QPushButton('Home', self)
        self.home.setGeometry(650,80,140,70)
        self.home.setFont(QFont('Arial', 19))
        self.home.setStyleSheet('background-color:#4299ff; color: white')
        self.home.clicked.connect(self.call_home)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(820,80,140,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_back)
        self.save = QPushButton('Save', self)
        self.save.setGeometry(480,80,140,70)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet('background-color:#4299ff; color: white')
        #self.save.clicked.connect(self.call_back)
        self.c_name = QLabel('Company Name',self)
        self.c_name.setFont(QFont('Arial', 16))
        self.c_name.setStyleSheet('background-color:white; color: black')
        self.c_name.move(90,130)
        self.c_name_entry = QLineEdit(self)
        self.c_name_entry.setFont(QFont('Arial', 16))
        self.c_name_entry.setGeometry(90,170,240,40)
        self.c_name_entry.setStyleSheet('background-color:white; color: black')
        self.tele_no = QLabel('Telephone Number',self)
        self.tele_no.setFont(QFont('Arial', 16))
        self.tele_no.setStyleSheet('background-color:white; color: black')
        self.tele_no.move(90,230)
        self.tele_no_entry = QLineEdit(self)
        self.tele_no_entry.setFont(QFont('Arial', 16))
        self.tele_no_entry.setGeometry(90,270,240,40)
        self.tele_no_entry.setStyleSheet('background-color:white; color: black')
        self.time = QLabel('Time',self)
        self.time.setFont(QFont('Arial', 16))
        self.time.setStyleSheet('background-color:white; color: black')
        self.time.move(90,330)
        self.s1 = Switch(self,thumb_radius=24, track_radius=25,text='Time')
        self.s1.move(90,370)
        self.temperature = QLabel('Temperature',self)
        self.temperature.setFont(QFont('Arial', 16))
        self.temperature.setStyleSheet('background-color:white; color: black')
        self.temperature.move(90,440)
        self.s2 = Switch(self,thumb_radius=24, track_radius=25,text='Temperature')
        self.s2.move(90,480)
        obj_Disk = psutil.disk_usage('/')
        self.progress_l = QLabel('Disk Storage',self)
        self.progress_l.setFont(QFont('Arial', 16))
        self.progress_l .setStyleSheet('background-color:white; color: black')
        self.progress_l .move(90,540)
        self.progress = QProgressBar(self)
        self.progress.setGeometry(90, 580, 300, 25)
        self.progress.setMaximum(100)
        self.progress.setValue(obj_Disk.percent) 
        self.screentimeout = QLabel('Screen Timeout',self)
        self.screentimeout.setFont(QFont('Arial', 16))
        self.screentimeout.setStyleSheet('background-color:white; color: black')
        self.screentimeout.move(500,230)
        self.b_timeout = QPushButton('Screen Timeout', self)
        self.b_timeout.setGeometry(500,280,240,90)
        self.b_timeout.setFont(QFont('Arial', 19))
        self.b_timeout.setStyleSheet('background-color:#4299ff; color: white')
        #self.b_timeout.clicked.connect(self.call_home)
        self.printer = QLabel('Printer',self)
        self.printer.setFont(QFont('Arial', 16))
        self.printer.setStyleSheet('background-color:white; color: black')
        self.printer.move(500,390)
        self.b_printer = QPushButton('Select Printer', self)
        self.b_printer.setGeometry(500,440,240,90)
        self.b_printer.setFont(QFont('Arial', 19))
        self.b_printer.setStyleSheet('background-color:#4299ff; color: white')
        #self.b_printer.clicked.connect(self.call_home)

        self.show()

    def call_home(self):
        self.close()
        self.destroy()
        gc.collect()
        self.mainwindow.show()
        
        #self.mySubwindow = result_window(self.mainwindow)
        #self.mySubwindow.show()
        #self.close()
        #self.svwindow = subwindow()
        #self.svwindow.show()
    def call_back(self):
        pass
        #self.close()
        #self.swindow = settingswindow()
        #self.swindow.show()
class damper_screen(QWidget):
    def __init__(self,mainwindow):
        super().__init__()
        self.title = "App3"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.mainwindow=mainwindow
        self.InitUI1()
    def InitUI1(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:#f7f7ff;")
        self.label = QLabel('Damper Screen',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black;')
        self.label.setGeometry(450,10,220,50)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,60,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white;')
        self.back.clicked.connect(self.call_first1)
        
        self.d_off = QPushButton('Off 0%', self)
        self.d_off.setCheckable(True)
        self.d_off.setGeometry(105,140,240,120)
        self.d_off.setFont(QFont('Arial', 21))
        self.d_off.setStyleSheet(("QPushButton{background-color:#4299ff; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:red;color:black; }"))
        
        self.d_off.clicked.connect(self.d_off_on)
        
        self.d_50 = QPushButton('Half 50 %', self)
        self.d_50.setCheckable(True)
        self.d_50.setGeometry(105,290,240,120)
        self.d_50.setFont(QFont('Arial', 21))
        #self.d_50.setStyleSheet("QPushButton{background-color:red;}")
        self.d_50.setStyleSheet(("QPushButton{background-color:#4299ff; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:red;color:black; }"))
        #self.d_50.setStyleSheet("QPushButton:pressed { background-color: ; }")
        #self.d_50.setStyleSheet("QPushButton:checked{background-color: white;}")
        self.d_50.clicked.connect(self.d_50_on)
        
        self.d_100 = QPushButton('Full 100 %', self)
        self.d_100.setCheckable(True)
        self.d_100.setGeometry(105,440,240,120)
        self.d_100.setFont(QFont('Arial', 21))
        self.d_100.setStyleSheet(("QPushButton{background-color:#4299ff; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:red;color:black; }"))
        
        self.d_100.clicked.connect(self.d_100_on)
    def d_50_on(self):
        #self.d_50.setCheckable(False)
        print("50")
        self.d_off.setEnabled(True)
        self.d_50.setEnabled(False)
        self.d_100.setEnabled(True)
        
        self.d_off.setCheckable(False)
        self.d_off.setEnabled(False)
        self.d_off.setEnabled(True)
        self.d_off.setCheckable(True)

        self.d_100.setCheckable(False)
        self.d_100.setEnabled(False)
        self.d_100.setEnabled(True)
        self.d_100.setCheckable(True)
        self.popup1=popup2(name='             Damper is turned to 50 %',name2='Close')
        self.popup1.show()

    def d_off_on(self):
        print("off")
        self.d_off.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_100.setEnabled(True)

        self.d_50.setCheckable(False)
        self.d_50.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_50.setCheckable(True)

        self.d_100.setCheckable(False)
        self.d_100.setEnabled(False)
        self.d_100.setEnabled(True)
        self.d_100.setCheckable(True)
        self.popup1=popup2(name='               Damper is turned off',name2='Close')
        self.popup1.show()

    def d_100_on(self):
        print("100")
        #self.d_off.setEnabled(False)
        self.d_100.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_off.setEnabled(True)

        self.d_50.setCheckable(False)
        self.d_50.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_50.setCheckable(True)

        self.d_off.setCheckable(False)
        self.d_off.setEnabled(False)
        self.d_off.setEnabled(True)
        self.d_off.setCheckable(True)
        self.popup1=popup2(name='              Damper is turned to 100 %',name2='Close')
        self.popup1.show()
    def call_first1(self):
        self.close()
        self.destroy()
        gc.collect()
        self.mainwindow.show()

        
class about_screen(QWidget):
    def __init__(self,mainwindow):
        super().__init__()
        self.title = "App3"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.mainwindow=mainwindow
        self.InitUI1()
    def InitUI1(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:#f7f7ff;")
        self.label = QLabel('About Us',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(450,10,220,50)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,60,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_first1)
        self.plainText = QPlainTextEdit(self)
        self.plainText.setStyleSheet('background-color:white; color: black')
        self.plainText.setTextCursor(QTextCursor())
        self.plainText.setFont(QFont('Arial',20))
        self.plainText.setReadOnly(True)
        self.plainText.setGeometry(10,150,1000,500)
        self.quote = """Anamed Systems was established back in 2006 with an aim in mind to provide the best medical and laboratory instruments to all over the world. Company 
has successfully achieved its target over the period of 13 years in the industry and now moving forward with a drastic pace to accomplish the vision of it’s 
founder.
Anamed Systems was installed with an purpose in thoughts to provide the 
excellent Medical and laboratory instruments to everywhere in the international.
Company has successfully performed its target over the length of thirteen 
years inside the industry and now transferring forward with a drastic tempo to 
perform the imaginative and prescient of it’s founder.
Anamed Systems is the specialized supplier of revolutionary heat technology
merchandise of drying, incubating and hot air sterilization carried out in 
studies, improvement, production and satisfactory guarantee.
As a member of Anamed Systems, KSA is specialized inside the income and 
carrier of these super merchandise. This technologically leading product line is based on a knowledge amassed over a few years and meets the needs and 
requirements of an ever changing marketplace.
Competent consulting, an international energetic network of buyers and a 
properly skilled group of provider technicians are the foundation of happy 
customers."""
        
        self.plainText.appendPlainText(self.quote)
    def call_first1(self):
        self.close()
        self.destroy()
        gc.collect()
        self.mainwindow.show()

class graphresultwindowsecond(QWidget):
    def __init__(self,mainwindow):
       super().__init__() 
       self.title = "App3"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.mainwindow=mainwindow
       self.startui()
       self.InitUI1()
    def getting_table_data(self):
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute(f"Select * from result where  key={starttestdata.key}")
            for x in y:
                print(x,x[0])
                self.set_temperature=x[2]
                self.set_timer=x[3]
                self.set_username=x[4]
                self.set_status=x[7]

            conn.commit()
            c.close()
            conn.close()
            self.df_faisal=pd.read_csv(starttestdata.key+'.csv')  
    def startui(self):
        self.getting_table_data()       
    def InitUI1(self):
        self.setWindowTitle(self.title)

        #self.setStyleSheet("background-image: url(header.png);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('resultscreen1.png'))
        self.label.setGeometry(0,0,1024,668)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(80,510,180,80)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_first1)
        self.print = QPushButton('Print', self)
        self.print.setGeometry(280,510,180,80)
        self.print.setFont(QFont('Arial', 21))
        self.print.setStyleSheet('background-color:#4299ff; color: white')
        self.print.clicked.connect(self.call_first1)
        self.exportcsv = QPushButton('Export Csv', self)
        self.exportcsv.setGeometry(480,510,180,80)
        self.exportcsv.setFont(QFont('Arial', 21))
        self.exportcsv.setStyleSheet('background-color:#4299ff; color: white')
        self.exportcsv.clicked.connect(self.call_first1)
        self.exportgraph = QPushButton('Export Graph', self)
        self.exportgraph.setGeometry(680,510,180,80)
        self.exportgraph.setFont(QFont('Arial', 21))
        self.exportgraph.setStyleSheet('background-color:#4299ff; color: white')
        self.exportgraph.clicked.connect(self.call_first1)
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(550,70,420, 390)
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=False,y=True)
        self.graphWidget.setLabel('left', 'Temperature')
        self.graphWidget.setLabel('bottom', 'Time')
        self.graphWidget.setWindowTitle('Temperature Graph')
        self.axis = DateAxisItem(orientation='bottom')
        self.axis.attachToPlotItem(self.graphWidget.getPlotItem())

        #self.xax = self.graphWidget.getAxis('bottom')
        #self.xax.setStyle(autoExpandTextSpace=True,tickTextHeight=25)
        #self.xax.setTicks(ticks)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.df_faisal['Time'], self.df_faisal['Temperature'], pen=pen)
        self.temperature = QLabel("Temperature",self)
        self.temperature.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.temperature.setGeometry(100,70,140,85)

        self.timer = QLabel("Timer",self)
        self.timer.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.timer.setGeometry(100,185,140,85)

                
        self.username = QLabel("User Name",self)
        self.username.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.username.setGeometry(100,290,140,85)
        
        self.status = QLabel("Status",self)
        self.status.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.status.setGeometry(100,400,100,85)
        
        self.temperature = QLabel(self)
        self.temperature.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.temperature.setGeometry(340,70,170,85)
        self.temperature.setText(self.set_temperature)

        self.timer = QLabel(self)
        self.timer.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.timer.setGeometry(340,185,170,85)
        self.timer.setText(self.set_timer)

                
        self.username = QLabel(self)
        self.username.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.username.setGeometry(340,290,170,85)
        self.username.setText(self.set_username)
        
        self.status = QLabel(self)
        self.status.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.status.setGeometry(340,400,170,85)
        self.status.setText(self.set_status)


        self.show()

    def call_first1(self):
        self.close()
        self.destroy()
        gc.collect()
        self.mySubwindow = result_window(self.mainwindow)
        self.mySubwindow.show()
class result_window(QWidget):
    def __init__(self,mainwindow):
       super().__init__()
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.mainwindow=mainwindow
       self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Results Data',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(450,10,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,60,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_back)

        self.exp_result = QPushButton('Export All Results', self)
        self.exp_result.setGeometry(30,60,240,70)
        self.exp_result.setFont(QFont('Arial', 21))
        self.exp_result.setStyleSheet('background-color:#4299ff; color: white')
        #self.addnewuser.clicked.connect(self.call_add)
        self.show_aresult = QPushButton('Show All Results', self)
        self.show_aresult.setGeometry(270,60,240,70)
        self.show_aresult.setFont(QFont('Arial', 21))
        self.show_aresult.setStyleSheet('background-color:#4299ff; color: white')
        self.show_aresult.clicked.connect(self.insert_data)
        
        self.view_result = QPushButton('View Result', self)
        self.view_result.setGeometry(510,60,240,70)
        self.view_result.setFont(QFont('Arial', 21))
        self.view_result.setStyleSheet('background-color:#4299ff; color: white')
        self.view_result.clicked.connect(self.view_result1)

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(150, 170, 231, 60)
        self.comboBox.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setStyleSheet("font: 87 15pt \"Arial\";background-color: rgb(241, 241, 241);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Date")
        self.comboBox.addItem("Temperature")
        self.comboBox.addItem("Timer")
        self.comboBox.addItem("Username")
        self.comboBox.addItem("Fanspeed")
        self.comboBox.addItem("Level")
        self.comboBox.addItem("Status")
        self.search = QLineEdit(self)
        self.search.setGeometry(410, 170, 251, 60)
        self.search.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.search.setObjectName("lineEdit_3")
        self.search.setFont(QFont('Arial', 21))
        self.search.setPlaceholderText('Enter Key Word')
        self.search_b = QPushButton('Search', self)
        self.search_b.setGeometry(680,170,200,60)
        self.search_b.setFont(QFont('Arial', 21))
        self.search_b.setStyleSheet('background-color:#4299ff; color: white')
        self.search_b.clicked.connect(self.view_search)


        self.dataView = QTreeWidget(self)
        #self.dataView.model=QAbstractItemModel()
        self.dataView.setRootIsDecorated(False)

        self.dataView.setHeaderLabels(['No','Date/\nTime','Temperature','Timer','User\nName','Fan\nSpeed','Level','Status'])

        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:14pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')



        self.dataView.setColumnCount(8)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,0)
        self.dataView.setColumnWidth(1,140)
        self.dataView.setColumnWidth(2,120)
        self.dataView.setColumnWidth(3,130)
        self.dataView.setColumnWidth(4,180)
        self.dataView.setColumnWidth(5,100)
        self.dataView.setColumnWidth(6,120)
        self.dataView.setColumnWidth(7,130)
        self.dataView.setAlternatingRowColors(True)
        #self.dataView.setColumnWidth(8,100)
        self.dataView.setColumnWidth(8,0)


        self.dataView.setStyleSheet('background-color:white;color: black;')
        self.dataView.setFont(QFont('Times New Roman', 18))
        self.dataView.setGeometry(10,250,1000,415)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dataView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dataView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        #self.dataView.setMouseEnabled(x=False)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        #self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
        self.show()
    @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(8)
        print(getChildNode)
    def call_back(self):
        self.close()
        self.destroy()
        gc.collect()
        self.mainwindow.show()
    def insert_data(self):
        #if(self.insertfirsttime==0):
            self.dataView.clear()
            self.insertfirsttime=1
            l=[]
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute("Select * from result order by Key DESC")
            for row in y:
                #print(row)
                l.append(row)
            for i,x in enumerate(l):
                #print(i,x)
                QTreeWidgetItem(self.dataView,[str(i),x[0]+str('\n')+x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]]) 

            conn.commit()
            c.close()
            conn.close()
    def view_result1(self):
        global getChildNode
        try:
            if len(str(getChildNode))==0:
                 raise ValueError 
            self.close()
            self.destroy()
            gc.collect() 
            #info.info1=getChildNode
            #self.e.show()
            starttestdata.key=str(getChildNode)
            self.grw=graphresultwindowsecond(self.mainwindow)
            self.grw.show()
            getChildNode=''

        except:
            print("error")
            self.popup1=popup1(name='            Please select any value !',name2='Close')
            self.popup1.show()
    def view_search(self):
        self.popup1=popup2(name='         The results has been updated !',name2='Close')
        self.popup1.show()
        self.dataView.clear()
        mg=self.search.text()
        mg.strip()
        temp_search=self.comboBox.currentText()
        temp_search.strip()
        print(mg,temp_search)
        l=[]
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        y=c.execute(f"SELECT * from result WHERE {temp_search} LIKE '{mg}%' OR {temp_search} LIKE '0{mg}%' order by Key DESC ")
        for row in y:
            #print(row)
            l.append(row)
        for i,x in enumerate(l):
            #print(i,x)
            QTreeWidgetItem(self.dataView,[str(i),x[0]+str('\n')+x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]]) 

        conn.commit()
        c.close()
        conn.close() 
class rg():
    rg=False
class running_window(QWidget):
    def __init__(self,runninggraph):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.runninggraph=runninggraph
       self.InitUI()
       #self.InitUI()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    def updateTime(self):
        #print('faisal')
        time = QTime.currentTime().toString()
        x_t=self.temp_call()
        #my_gauge.value=x_t
       #self.label.setText(str(x_t))
        self.gauge.update_value(x_t)
        # if (c_to_f==0):
        #     my_gauge.value_min = 0
        #     my_gauge.value_max = 300
        # if (c_to_f==1):
        #     my_gauge.value_min = 32
        #     my_gauge.value_max = 572

       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_AcceptTouchEvents)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,150,320, 340)
        self.gauge.setStyleSheet("background-color:#f7f7ff;")
        #self.Form = QtWidgets.QWidget()
        #self.ui = Ui_Form()
        #self.ui.setupUi(self.Form)
        #self.Form.show()
        # self.label = QLabel('uu',self)
        # self.label.setGeometry(165, 5, 61, 16)
        # self.label.setObjectName("label")
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(10)
        #self.gauge.show()
        #self.s1 = Switch(self)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        buttonWindow1 = QPushButton('View Running Test', self)
        buttonWindow1.setFont(QFont('Arial', 27))
        buttonWindow1.setGeometry(20,60,285,155)
        #buttonWindow1.setStyleSheet('background-image: url(start.png);')
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        Settings = QPushButton('Settings  ', self)
        Settings.setFont(QFont('Arial', 27))
        Settings.setGeometry(20,250,285,155)
        Settings.setStyleSheet('background-image: url(setting.png);')
        Settings.clicked.connect(self.settingswindow)
        User = QPushButton('User      ', self)
        User.setFont(QFont('Arial', 27))
        User.setGeometry(20,440,285,155)
        User.setStyleSheet('background-image: url(user.png);')
        User.clicked.connect(self.userswindow)
        Results = QPushButton('Results', self)
        Results.setFont(QFont('Arial', 27))
        Results.setGeometry(330,60,285,155)
        Results.setStyleSheet('background-image: url(Result.png);')
        Results.clicked.connect(self.resultswindow)
        About = QPushButton('About  ', self)
        About.setFont(QFont('Arial', 27))
        About.setGeometry(330,250,285,155)
        About.setStyleSheet('background-image: url(about.png);')
        About.clicked.connect(self.aboutwindow)
        Damper = QPushButton('Damper ', self)
        Damper.setFont(QFont('Arial', 27))
        Damper.setGeometry(330,440,285,155)
        Damper.setStyleSheet('background-image: url(damper.png);')
        Damper.clicked.connect(self.damperwindow)
        #objgraph.show_refs(self, filename='sample-graph.png')
        self.show()

    def buttonWindow1_onClick(self):
        self.close()
        self.destroy()
        gc.collect()
        #self.rgwindow = startwindow(self)
        self.runninggraph.show()
    def settingswindow(self):
        self.close()
        self.destroy()
        gc.collect()
        self.s_w=settingswindow(self)
        pass
        #self.close()
        #self.swindow = settingswindow()
        #self.swindow.show()
    def userswindow(self):
        self.close()
        self.uwindow = userswindow(self)
        self.uwindow.show()
    def resultswindow(self):
        self.close()
        self.rw=result_window(self)
        self.rw.show()
        #self.close()
        #self.rswindow = resultswindow()
        #self.rswindow.show()
    def aboutwindow(self):
        self.close()
        self.a_s=about_screen(self)
        self.a_s.show()
        #self.close()
        #self.abwindow = aboutwindow()
        #self.abwindow.show()
    def damperwindow(self):
        self.close()
        self.d_s=damper_screen(self)
        self.d_s.show()
        #self.close()
        #self.dwindow = damperwindow()
        #self.dwindow.show()

        #parent.destroy()
        #url.focusInEvent(QFocusEvent)
        #self.emit(SIGNAL("clicked()"))



class temperature_list():
    def temp_call(self):
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    start=False
    temperature_1=[]
    time_1=[]
    while start:
        now = time.time()
        #self.time.append(now)
        temperature_1.append(temp_call)
        time_1.append(now)



class DateAxisItem(AxisItem):
    """
    A tool that provides a date-time aware axis. It is implemented as an
    AxisItem that interpretes positions as unix timestamps (i.e. seconds
    since 1970).
    The labels and the tick positions are dynamically adjusted depending
    on the range.
    It provides a  :meth:`attachToPlotItem` method to add it to a given
    PlotItem
    """
    
    # Max width in pixels reserved for each label in axis
    _pxLabelWidth = 80

    def __init__(self, *args, **kwargs):
        AxisItem.__init__(self, *args, **kwargs)
        self._oldAxis = None

    def tickValues(self, minVal, maxVal, size):
        """
        Reimplemented from PlotItem to adjust to the range and to force
        the ticks at "round" positions in the context of time units instead of
        rounding in a decimal base
        """

        maxMajSteps = int(size/self._pxLabelWidth)

        dt1 = datetime.fromtimestamp(minVal)
        dt2 = datetime.fromtimestamp(maxVal)

        dx = maxVal - minVal
        majticks = []

        if dx > 63072001:  # 3600s*24*(365+366) = 2 years (count leap year)
            d = timedelta(days=366)
            for y in range(dt1.year + 1, dt2.year):
                dt = datetime(year=y, month=1, day=1)
                majticks.append(mktime(dt.timetuple()))

        elif dx > 5270400:  # 3600s*24*61 = 61 days
            d = timedelta(days=31)
            dt = dt1.replace(day=1, hour=0, minute=0,
                             second=0, microsecond=0) + d
            while dt < dt2:
                # make sure that we are on day 1 (even if always sum 31 days)
                dt = dt.replace(day=1)
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 172800:  # 3600s24*2 = 2 days
            d = timedelta(days=1)
            dt = dt1.replace(hour=0, minute=0, second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 7200:  # 3600s*2 = 2hours
            d = timedelta(hours=1)
            dt = dt1.replace(minute=0, second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 1200:  # 60s*20 = 20 minutes
            d = timedelta(minutes=10)
            dt = dt1.replace(minute=(dt1.minute // 10) * 10,
                             second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 120:  # 60s*2 = 2 minutes
            d = timedelta(minutes=1)
            dt = dt1.replace(second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 20:  # 20s
            d = timedelta(seconds=10)
            dt = dt1.replace(second=(dt1.second // 10) * 10, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 2:  # 2s
            d = timedelta(seconds=1)
            majticks = range(int(minVal), int(maxVal))

        else:  # <2s , use standard implementation from parent
            return AxisItem.tickValues(self, minVal, maxVal, size)

        L = len(majticks)
        if L > maxMajSteps:
            majticks = majticks[::int(numpy.ceil(float(L) / maxMajSteps))]

        return [(d.total_seconds(), majticks)]

    def tickStrings(self, values, scale, spacing):
        """Reimplemented from PlotItem to adjust to the range"""
        ret = []
        if not values:
            return []

        if spacing >= 31622400:  # 366 days
            fmt = "%Y"

        elif spacing >= 2678400:  # 31 days
            fmt = "%Y %b"

        elif spacing >= 86400:  # = 1 day
            fmt = "%b/%d"

        elif spacing >= 3600:  # 1 h
            fmt = "%b/%d-%Hh"

        elif spacing >= 60:  # 1 m
            fmt = "%H:%M"

        elif spacing >= 1:  # 1s
            fmt = "%H:%M:%S"

        else:
            # less than 2s (show microseconds)
            # fmt = '%S.%f"'
            fmt = '[+%fms]'  # explicitly relative to last second

        for x in values:
            try:
                t = datetime.fromtimestamp(x)
                ret.append(t.strftime(fmt))
            except ValueError:  # Windows can't handle dates before 1970
                ret.append('')

        return ret

    def attachToPlotItem(self, plotItem):
        """Add this axis to the given PlotItem
        :param plotItem: (PlotItem)
        """
        self.setParentItem(plotItem)
        viewBox = plotItem.getViewBox()
        self.linkToView(viewBox)
        self._oldAxis = plotItem.axes[self.orientation]['item']
        self._oldAxis.hide()
        plotItem.axes[self.orientation]['item'] = self
        pos = plotItem.axes[self.orientation]['pos']
        plotItem.layout.addItem(self, *pos)
        self.setZValue(-1000)

    def detachFromPlotItem(self):
        """Remove this axis from its attached PlotItem
        (not yet implemented)
        """
        raise NotImplementedError()  # TODO
class MyStringAxis(pg.AxisItem):
        def __init__(self, xdict, *args, **kwargs):
            pg.AxisItem.__init__(self, *args, **kwargs)
            self.x_values = np.asarray(xdict.keys())
            self.x_strings = xdict.values()

        def tickStrings(self, values, scale, spacing):
            strings = []
            for v in values:
                # vs is the original tick value
                vs = v * scale
                # if we have vs in our values, show the string
                # otherwise show nothing
                if vs in self.x_values:
                    # Find the string with x_values closest to vs
                    vstr = self.x_strings[np.abs(self.x_values-vs).argmin()]
                else:
                    vstr = ""
                strings.append(vstr)
            return strings
class selectuserscreen(QWidget):
    def __init__(self,mainwindowshow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.mainwindowshow=mainwindowshow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Select User',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,20,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,100,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        
        self.selectuser = QPushButton('Select User', self)
        self.selectuser.setGeometry(30,100,240,70)
        self.selectuser.setFont(QFont('Arial', 21))
        self.selectuser.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.selectuser.clicked.connect(self.call_select)

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','User Name'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.setColumnCount(2)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,200,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
    @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
        
    def insert_data(self):
        #if(self.insertfirsttime==0):
            #self.insertfirsttime=1
            l=[]
            test = UsersTable("faisal.db")
            x=test.select("SELECT * FROM Userdata order by ActionKey DESC")
            for row in x:
                #print(row)
                l.append(row)
            for i,x in enumerate(l):
                #print(i,x)
                QTreeWidgetItem(self.dataView,[str(i),x[0]])
    def call_back(self):
        self.close()
        self.userswindow=startwindow(self.mainwindowshow)
        self.userswindow.show()
    def call_select(self):
        global getChildNode
        self.close()
        starttestdata.username=getChildNode
        self.userswindow=startwindow(self.mainwindowshow)
        self.userswindow.show()




class timer_keyboard(QWidget):
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):
    #def __init__(self,name):
        super().__init__()
        #self.name=name
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='hours' ):
            self.labelshow="Enter Hours"
            self.length=2
        elif(self.previouswindow=='minutes' ):
            self.labelshow="Enter Minutes"
            self.length=2




    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,16,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        #self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QtGui.QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,133,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,133,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,133,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,237,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,237,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,237,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,341,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,341,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,341,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,445,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,445,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kinf = QPushButton('infinity', self)
        kinf.setGeometry(670,445,297,100)
        kinf.setFont(QFont('Arial', 28))
        kinf.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kinf.clicked.connect(self.enter1)
        
        kl = QPushButton('<', self)
        kl.setGeometry(45,549,296,100)
        kl.setFont(QFont('Arial', 24))
        kl.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kl.clicked.connect(self.moveleft)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(358,549,296,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)
        
        kr = QPushButton('>', self)
        kr.setGeometry(670,549,297,100)
        kr.setFont(QFont('Arial', 24))
        kr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kr.clicked.connect(self.moveright)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.insert(str(sender.text()))
            #self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
    def clear1(self):
        self.entry.backspace()
        #self.entry.text=self.entry.text()[0:-2]
        # print(self.entry.text()[0:-1])
        # l=self.entry.text()[0:-1]
        # self.entry.setText(l)
        self.entry.setFocus()
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    
    def enter1(self):
        if(self.previouswindow=='hours' ):
            try:
                text=self.entry.text()
                sender = self.sender()
                #print(self.sender())
                if(str(sender.text())=='infinity'):
                    self.close()
                    # starttestdata.hours = self.entry.text()
                    # starttestdata.minutes = self.entry.text()
                    starttestdata.hours = 'infinity'
                    starttestdata.minutes = 'infinity'
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()

                elif(len(text)==0):
                    self.close()
                    starttestdata.hours = self.entry.text()
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()

                #elif(text.count('.')>=2):
                #    raise NameError
                #elif(float(self.entry.text())>300 or float(self.entry.text())<25):
                #    raise ValueError
                
                #print(y.username,'ee')
                elif(int(self.entry.text())>99):
                    raise ValueError

                else:
                    self.close()
                    starttestdata.hours = self.entry.text()
                    #self.destroy()
                    #gc.collect()
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()
            except NameError:
                self.popup1=popup1(name='           Please enter valid temperature !',name2='Close')
                self.popup1.show()
            except ValueError:
                self.popup1=popup1(name='           Pleae enter hours less than 100.',name2='Close')
                self.popup1.show()
        elif(self.previouswindow=='minutes' ):
            try:
                text=self.entry.text()
                sender = self.sender()
                #print(self.sender())
                if(str(sender.text())=='infinity'):
                    self.close()
                    # starttestdata.hours = self.entry.text()
                    # starttestdata.minutes = self.entry.text()
                    starttestdata.hours = 'infinity'
                    starttestdata.minutes = 'infinity'
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()

                elif(len(text)==0):
                    self.close()
                    starttestdata.minutes = self.entry.text()
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()

                #elif(text.count('.')>=2):
                #    raise NameError
                elif(int(self.entry.text())>59):
                    raise ValueError
                
                #print(y.username,'ee')
                elif(text=='infinity'):
                    self.close()
                    starttestdata.hours = self.entry.text()
                    starttestdata.minutes = self.entry.text()
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()

                else:
                    self.close()
                    starttestdata.minutes = self.entry.text()
                    #self.destroy()
                    #gc.collect()
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()
            except NameError:
                self.popup1=popup1(name='           Please enter valid temperature !',name2='Close')
                self.popup1.show()
            except ValueError:
                self.popup1=popup1(name='           Pleae enter minutes less than 60.',name2='Close')
                self.popup1.show()



    def moveleft(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()-1
        self.entry.setCursorPosition(x)

    def moveright(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()+1
        self.entry.setCursorPosition(x)
class temperature_keyboard(QWidget):
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):
    #def __init__(self,name):
        super().__init__()
        #self.name=name
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='temperature' ):
            self.labelshow="Enter Temerature"
            self.length=5



    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,16,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        #self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QtGui.QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,133,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,133,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,133,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,237,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,237,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,237,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,341,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,341,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,341,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,445,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,445,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,445,297,100)
        kpo.setFont(QFont('Arial', 28))
        kpo.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kpo.clicked.connect(self.insert_text)
        
        kl = QPushButton('<', self)
        kl.setGeometry(45,549,296,100)
        kl.setFont(QFont('Arial', 24))
        kl.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kl.clicked.connect(self.moveleft)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(358,549,296,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)
        
        kr = QPushButton('>', self)
        kr.setGeometry(670,549,297,100)
        kr.setFont(QFont('Arial', 24))
        kr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kr.clicked.connect(self.moveright)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.insert(str(sender.text()))
            #self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
    def clear1(self):
        self.entry.backspace()
        #self.entry.text=self.entry.text()[0:-2]
        # print(self.entry.text()[0:-1])
        # l=self.entry.text()[0:-1]
        # self.entry.setText(l)
        self.entry.setFocus()
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    
    def enter1(self):
        if(self.previouswindow=='temperature' ):
            try:
                text=self.entry.text()
                if(len(text)==0):
                    self.close()
                    starttestdata.temperature = self.entry.text()
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()

                elif(text.count('.')>=2):
                    raise NameError
                elif(float(self.entry.text())>300 or float(self.entry.text())<25):
                    raise ValueError
                
                #print(y.username,'ee')
                else:
                    self.close()
                    starttestdata.temperature = self.entry.text()
                    #self.destroy()
                    #gc.collect()
                    self.userswindow=startwindow(self.mainwindowshow)
                    self.userswindow.show()
            except NameError:
                self.popup1=popup1(name='           Please enter valid temperature !',name2='Close')
                self.popup1.show()
            except ValueError:
                self.popup1=popup1(name='Pleae enter temperature less than 300\n and greater than 25.',name2='Close')
                self.popup1.show()





    def moveleft(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()-1
        self.entry.setCursorPosition(x)

    def moveright(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()+1
        self.entry.setCursorPosition(x)

        #self.close()
        #self.destroy()
        #gc.collect()        
class graphresultwindow(QWidget):
    def __init__(self,mainwindow):
       super().__init__() 
       #parent=None
       #super(secondwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App3"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.mainwindow=mainwindow
       self.startui()
       self.InitUI1()
    def getting_table_data(self):
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute(f"Select * from result where  key={starttestdata.key}")
            for x in y:
                print(x,x[0])
                self.set_temperature=x[2]
                self.set_timer=x[3]
                self.set_username=x[4]
                self.set_status=x[7]

            conn.commit()
            c.close()
            conn.close()
            self.df_faisal=pd.read_csv(starttestdata.key+'.csv')  
    def startui(self):
        self.getting_table_data()       
    def InitUI1(self):
        self.setWindowTitle(self.title)

        #self.setStyleSheet("background-image: url(header.png);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('resultscreen1.png'))
        self.label.setGeometry(0,0,1024,668)
        self.back = QPushButton('Home', self)
        self.back.setGeometry(80,510,180,80)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_first1)
        self.print = QPushButton('Print', self)
        self.print.setGeometry(280,510,180,80)
        self.print.setFont(QFont('Arial', 21))
        self.print.setStyleSheet('background-color:#4299ff; color: white')
        #self.print.clicked.connect(self.call_first1)
        self.exportcsv = QPushButton('Export Csv', self)
        self.exportcsv.setGeometry(480,510,180,80)
        self.exportcsv.setFont(QFont('Arial', 21))
        self.exportcsv.setStyleSheet('background-color:#4299ff; color: white')
        #self.exportcsv.clicked.connect(self.call_first1)
        self.exportgraph = QPushButton('Export Graph', self)
        self.exportgraph.setGeometry(680,510,180,80)
        self.exportgraph.setFont(QFont('Arial', 21))
        self.exportgraph.setStyleSheet('background-color:#4299ff; color: white')
        #self.exportgraph.clicked.connect(self.call_first1)
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(550,70,420, 390)
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=False,y=True)
        self.graphWidget.setLabel('left', 'Temperature')
        self.graphWidget.setLabel('bottom', 'Time')
        self.graphWidget.setWindowTitle('Temperature Graph')
        self.axis = DateAxisItem(orientation='bottom')
        self.axis.attachToPlotItem(self.graphWidget.getPlotItem())

        #self.xax = self.graphWidget.getAxis('bottom')
        #self.xax.setStyle(autoExpandTextSpace=True,tickTextHeight=25)
        #self.xax.setTicks(ticks)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.df_faisal['Time'], self.df_faisal['Temperature'], pen=pen)
        self.temperature = QLabel("Temperature",self)
        self.temperature.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.temperature.setGeometry(100,70,140,85)

        self.timer = QLabel("Timer",self)
        self.timer.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.timer.setGeometry(100,185,140,85)

                
        self.username = QLabel("User Name",self)
        self.username.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.username.setGeometry(100,290,140,85)
        
        self.status = QLabel("Status",self)
        self.status.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.status.setGeometry(100,400,100,85)
        
        self.temperature = QLabel(self)
        self.temperature.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.temperature.setGeometry(340,70,170,85)
        self.temperature.setText(self.set_temperature)

        self.timer = QLabel(self)
        self.timer.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.timer.setGeometry(340,185,170,85)
        self.timer.setText(self.set_timer)

                
        self.username = QLabel(self)
        self.username.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.username.setGeometry(340,290,170,85)
        self.username.setText(self.set_username)
        
        self.status = QLabel(self)
        self.status.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.status.setGeometry(340,400,170,85)
        self.status.setText(self.set_status)


        self.show()

    def call_first1(self):
        self.close()
        self.destroy()
        gc.collect()
        self.mainwindow.show()
class runninggraphwindow(QWidget):
    def __init__(self,name):
        super().__init__()
        self.title = "App3"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.mainwindow=name
        self.i=0
        self.time1=[]
        self.startUI()
        self.InitUI()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55

    def update_plot_data(self):
        #time = QTime.currentTime().toString()
        now = time.time()
        #timestamps = numpy.linspace(now - 3600, now, 100)
        self.time.append(now)
        #self.time1.append(self.i)
        #self.ticks = [list(zip(range(self.i), self.time))]
        #self.i=self.i+1

        #self.xax.setTicks(self.ticks)
        
        #self.x = self.x[1:]  # Remove the first y element.
        #time = QTime.currentTime().toString()
        #self.time.append('time')  # Add a new value 1 higher than the last.


        #self.y = self.y[1:]  # Remove the first

        x_t=self.temp_call() 
        self.temperature.append(x_t)  # Add a new random value.
        #self.xdict=dict(enumerate(self.time))

        self.data_line .setData(self.time, self.temperature)
        self.gauge.update_value(x_t)  # Update the data.
    def startUI(self):
        if(starttestdata.hours=='infinity'):
            self.time_show='infinity'
        else:
            self.time_show=str(starttestdata.hours)+'Hrs'+str(starttestdata.minutes)+'Mins'
        
    def InitUI(self):

        self.setWindowTitle(self.title)

        #self.setStyleSheet("background-image: url(header.png);")


        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        #self.setCursor(Qt.BlankCursor)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,0,1024,668)
        
        self.set_temp = QLabel("Set Temperature :",self)
        self.set_temp.setFont(QFont('Arial', 17))
        #self.set_temp.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.set_temp.setGeometry(120,400,200,85)
        
        self.set_temp_data = QLabel(self)
        self.set_temp_data.setFont(QFont('Arial', 17))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.set_temp_data.setGeometry(300,400,100,85)
        self.set_temp_data.setText(starttestdata.temperature)

        self.set_timer = QLabel("Set Timer :",self)
        self.set_timer.setFont(QFont('Arial', 17))
        #self.set_timer.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.set_timer.setGeometry(650,400,130,85)
        
        self.set_timer_data = QLabel(self)
        self.set_timer_data.setFont(QFont('Arial', 17))
        #self.set_timer_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.set_timer_data.setGeometry(780,400,200,85)
        self.set_timer_data.setText(self.time_show)
        #self.time_show

        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(700,100,250, 300)
        self.gauge.setStyleSheet("background-color:white;")
        #self.gauge.show()
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(70,40,550, 350)
        self.graphWidget.setBackground('w')
        self.graphWidget.plotItem.setMouseEnabled(y=False) # Only allow zoom in X-axis
        self.graphWidget.setMouseEnabled(x=False)
        #pg.setConfigOption('leftButtonPan', False)
        #pg.setConfigOption('WheelspinPan', False)
        #graphWidget.setStyleSheet("background-color:white;")
       #pg.setConfigOption('background', 'w')
       # pg.setConfigOption('foreground', 'k')
        self.graphWidget.showGrid(x=False,y=True)
##        plt.addLegend()
##
##        # set properties
        self.graphWidget.setLabel('left', 'Temperature')
        self.graphWidget.setLabel('bottom', 'Time')
##        plt.setXRange(0,10)
##        plt.setYRange(0,20)
        self.graphWidget.setWindowTitle('Temperature Graph')
        #self.graphWidget.addPlot(axisItems={'bottom': stringaxis})
           # x = ['a', 'b', 'c', 'd', 'e', 'f']
    #y = [1, 2, 3, 4, 5, 6]
    #xdict = dict(enumerate(x))

    #win = pg.GraphicsWindow()
    #stringaxis = MyStringAxis(xdict, orientation='bottom')
    #plot = win.addPlot(axisItems={'bottom': stringaxis})
    #curve = plot.plot(list(xdict.keys()),y)
        
        self.time = []  # 100 time points
        #self.xdict=dict(enumerate(self.time))
        #self.stringaxis = MyStringAxis(self.xdict, orientation='bottom')
        #self.graphWidget.addPlot(axisItems={'bottom': self.stringaxis})
        self.axis = DateAxisItem(orientation='bottom')
        self.axis.attachToPlotItem(self.graphWidget.getPlotItem())

        #self.xax = self.graphWidget.getAxis('bottom')
        #self.xax.setStyle(autoExpandTextSpace=True,tickTextHeight=25)
        self.temperature = []
        #self.xax.setTicks(ticks)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.time, self.temperature, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        #self.graphWidget.show()
        
        #self.setCentralWidget(self.graphWidget)

        #hour = [1,2,3,4,5,6,7,8,9,10]
        #temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        #self.graphWidget.plot(hour, temperature)
        self.Home = QPushButton('Home', self)
        self.Home.setGeometry(120,500,250,90)
        self.Home.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.Home.clicked.connect(self.call_home)
        self.stoptest = QPushButton('Stop Test', self)
        self.stoptest.setGeometry(650,500,250,90)
        self.stoptest.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.stoptest.clicked.connect(self.popup_stoptest)

        self.show()
    def insert_data(self):
            if(starttestdata.hours=='infinity'):
                timer_data='infinity'
            else:
                timer_data=str(starttestdata.hours)+"hrs"+str(starttestdata.minutes)+"mins"
            status='halted'
            currentDT = datetime.now()
            date_test=currentDT.strftime("%d-%m-%Y")
            time_test=currentDT.strftime("%H:%M:%S")
            key_1=currentDT.strftime("%Y%m%d%H%M%S")
            #print(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1)
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            #c.execute(f"DELETE from Userdata where ActionKey={keydata.editdata}") 
            c.execute("INSERT INTO result(Date,Time,Temperature,Timer,Username,FanSpeed,Level,Status,Key) VALUES(?,?,?,?,?,?,?,?,?)",(date_test,time_test,starttestdata.temperature,timer_data,starttestdata.username,starttestdata.fanspeed,starttestdata.level,status,key_1))
            conn.commit()
            c.close()
            conn.close()
            Value={'Time':self.time , 'Temperature':self.temperature}
            df1=DataFrame(Value,columns=['Time','Temperature'])
            ex_csv=key_1+'.csv'
            export_csv=df1.to_csv(ex_csv,index=None,header=True)
            starttestdata.key=key_1
            #self.close()
            #self.destroy()
            #gc.collect()
    def call_home(self):
        self.close()
        self.mm=running_window(self)
        self.mm.show()
    def call_stopfinal(self):
                self.insert_data()
                #a.close()
                #a.destroy()
                
                self.close()
                self.destroy()
                gc.collect()
                self.grw=graphresultwindow(self.mainwindow)
                self.grw.show()
    def popup_stoptest(self):
            def call_no():
                a.close()
                a.destroy()
                gc.collect()

                #pass
            #print("popup")
            a=QFrame()
            a.setGeometry(237,209,550,350)
            a.setWindowModality(Qt.ApplicationModal)
            a.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
            a.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(a)
            self._gif.move(215,30)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("as4.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            movie.start()
            label1 = QLabel('Error',a)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(236,130)
            label2 = QLabel('Are you sure you want to stop this test !',a)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            yes_delete = QPushButton('Yes !', a)
            yes_delete .setGeometry(50,240,240,90)
            yes_delete .setFont(QFont('Arial', 21))
            yes_delete .setStyleSheet('background-color:#d00403; color: white')
            yes_delete .clicked.connect(self.call_stopfinal)
            yes_delete .clicked.connect(call_no)
            no = QPushButton('No', a)
            no.setGeometry(270,240,240,90)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(call_no)
            a.show()
    def call_stoptest(self):
        self.popup_stoptest()


class startwindow(QWidget):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.setupUi()
    def call_b(self,data):
        print("asdss",data)
        if(data=="temperature"):
            user_data=self.lineEdit.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=temperature_keyboard(self.name,data,user_data)
            self.nk.show()
        elif(data=="hours"):
            user_data=self.lineEdit_2.text()
            if(user_data=='infinity'):
                user_data=''
                starttestdata.hours=''
                starttestdata.minutes=''
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=timer_keyboard(self.name,data,user_data)
            self.nk.show()
        elif(data=="minutes"):
            user_data=self.lineEdit_3.text()
            if(user_data=='infinity'):
                user_data=''
                starttestdata.hours=''
                starttestdata.minutes=''
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=timer_keyboard(self.name,data,user_data)
            self.nk.show()
        elif(data=='username'):
            self.close()
            self.sc=selectuserscreen(self.name)
            self.sc.show()

    def setupUi(self):
        #self.setObjectName("self")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setEnabled(True)
        #self.resize(1024, 668)
        self.setGeometry(0,100,1024,668)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setMouseTracking(True)
        self.setAcceptDrops(False)
        self.setToolTip("")
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(247, 247, 255)")

        self.TestScreen = QtWidgets.QLabel(self)
        self.TestScreen.setGeometry(QtCore.QRect(410, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TestScreen.setFont(font)
        self.TestScreen.setAutoFillBackground(False)
        self.TestScreen.setStyleSheet("")
        self.TestScreen.setObjectName("TestScreen")
        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(QtCore.QRect(20, 150, 981, 81))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit = extQLineEdit1(self)
        self.lineEdit.setGeometry(QtCore.QRect(710, 170, 211, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QFont('Arial', 21))
        self.lineEdit.setPlaceholderText('Temperature')
        self.lineEdit.speak.connect(partial(self.call_b,data='temperature'))
        self.graphicsView_2 = QtWidgets.QGraphicsView(self)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 230, 981, 81))
        self.graphicsView_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.lineEdit_2 = extQLineEdit1(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 250, 101, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(QFont('Arial', 21))
        self.lineEdit_2.setPlaceholderText('Hrs')
        self.lineEdit_2.speak.connect(partial(self.call_b,data='hours'))
        self.graphicsView_3 = QtWidgets.QGraphicsView(self)
        self.graphicsView_3.setGeometry(QtCore.QRect(20, 390, 981, 81))
        self.graphicsView_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.lineEdit_3 = extQLineEdit1(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(820, 250, 101, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(QFont('Arial', 21))
        self.lineEdit_3.setPlaceholderText('Min')
        self.lineEdit_3.speak.connect(partial(self.call_b,data='minutes'))
        self.lineEdit_6 = extQLineEdit1(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(710, 490, 231, 41))
        self.lineEdit_6.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setFont(QFont('Arial', 21))
        self.lineEdit_6.setPlaceholderText('Username')
        self.lineEdit_6.speak.connect(partial(self.call_b,data='username'))
        self.graphicsView_6 = QtWidgets.QGraphicsView(self)
        self.graphicsView_6.setGeometry(QtCore.QRect(20, 310, 981, 81))
        self.graphicsView_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self)
        self.graphicsView_7.setGeometry(QtCore.QRect(20, 470, 981, 81))
        self.graphicsView_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.TestScreen_2 = QtWidgets.QLabel(self)
        self.TestScreen_2.setGeometry(QtCore.QRect(50, 180, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_2.setFont(font)
        self.TestScreen_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.TestScreen_2.setAutoFillBackground(False)
        self.TestScreen_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_2.setObjectName("TestScreen_2")
        self.TestScreen_3 = QtWidgets.QLabel(self)
        self.TestScreen_3.setGeometry(QtCore.QRect(50, 260, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_3.setFont(font)
        self.TestScreen_3.setAutoFillBackground(False)
        self.TestScreen_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_3.setObjectName("TestScreen_3")
        self.TestScreen_4 = QtWidgets.QLabel(self)
        self.TestScreen_4.setGeometry(QtCore.QRect(50, 340, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_4.setFont(font)
        self.TestScreen_4.setAutoFillBackground(False)
        self.TestScreen_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_4.setObjectName("TestScreen_4")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(710, 330, 231, 41))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setStyleSheet("font: 87 15pt \"Arial\";background-color: rgb(241, 241, 241);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.TestScreen_5 = QtWidgets.QLabel(self)
        self.TestScreen_5.setGeometry(QtCore.QRect(50, 420, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_5.setFont(font)
        self.TestScreen_5.setAutoFillBackground(False)
        self.TestScreen_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_5.setObjectName("TestScreen_5")
        self.TestScreen_6 = QtWidgets.QLabel(self)
        self.TestScreen_6.setGeometry(QtCore.QRect(50, 500, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_6.setFont(font)
        self.TestScreen_6.setAutoFillBackground(False)
        self.TestScreen_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_6.setObjectName("TestScreen_6")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(710, 410, 231, 41))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_2.setAcceptDrops(False)
        self.comboBox_2.setStyleSheet("font: 87 15pt \"Arial\";background-color: rgb(241, 241, 241);")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(660, 52, 291, 71))
        self.pushButton.clicked.connect(self.call_starttest)
        self.pushButton.setStyleSheet("border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 2px;\n"
"background-color: rgb(188, 255, 194);\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 570, 241, 61))
        
        #self.pushButton_2.clicked.connect(QtWidgets.qApp.quit)
        #self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_2.clicked.connect(self.call_first1)
        self.pushButton_2.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_7.raise_()
        self.graphicsView_6.raise_()
        self.TestScreen.raise_()
        self.graphicsView.raise_()
        self.lineEdit.raise_()
        self.graphicsView_2.raise_()
        self.lineEdit_2.raise_()
        self.graphicsView_3.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_6.raise_()
        self.TestScreen_2.raise_()
        self.TestScreen_3.raise_()
        self.TestScreen_4.raise_()
        self.comboBox.raise_()
        self.TestScreen_5.raise_()
        self.TestScreen_6.raise_()
        self.comboBox_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        uni=u'\u231A'
        #uni=U+1F550
        self.label = QLabel(uni,self)
        self.label.setFont(QFont('Arial', 38))
        self.label.setStyleSheet('background-color:white;color: black;')
        self.label.setGeometry(924,240,57,45)
        self.retranslateUi()
        self.inserteditdata()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Start Test"))
        self.TestScreen.setText(_translate("self", "Test Screen"))
        self.TestScreen_2.setText(_translate("self", "SET TEMPERATURE"))
        self.TestScreen_3.setText(_translate("self", "SET TIMER"))
        self.TestScreen_4.setText(_translate("self", "SET LEVEL"))
        self.comboBox.setItemText(0, _translate("self", "FAST"))
        self.comboBox.setItemText(1, _translate("self", "MEDIUM"))
        self.comboBox.setItemText(2, _translate("self", "SLOW"))
        self.TestScreen_5.setText(_translate("self", "SET FAN SPEED"))
        self.TestScreen_6.setText(_translate("self", "SELECT USER"))
        self.comboBox_2.setItemText(0, _translate("self", "100%"))
        self.comboBox_2.setItemText(1, _translate("self", "50%"))
        self.comboBox_2.setItemText(2, _translate("self", "25%"))
        self.comboBox_2.setItemText(2, _translate("self", "off"))
        self.pushButton.setText(_translate("self", "START TEST"))
        self.pushButton_2.setText(_translate("self", "BACK"))
    
    def inserteditdata(self):
            self.lineEdit.setText(starttestdata.temperature)
            self.lineEdit_2.setText(starttestdata.hours)
            self.lineEdit_3.setText(starttestdata.minutes)
            self.lineEdit_6.setText(starttestdata.username)

    def call_first1(self):
        #self.destroy()
        #gc.collect()
        self.close()

        self.name.show()
    def call_starttest(self):
        
        temp=self.lineEdit.text()
        timer1=self.lineEdit_2.text()
        timer2=self.lineEdit_3.text()
        level=self.comboBox.currentText()
        fansp=self.comboBox_2.currentText()
        un=self.lineEdit_6.text()
        try:
            if(len(temp)==0 or len(timer1)==0 or len(timer2)==0 or len(level)==0 or len(fansp)==0 or len(un)==0):
                raise ValueError
            else:
                self.close()
                starttestdata.temperature=self.lineEdit.text()
                starttestdata.hours=self.lineEdit_2.text()
                starttestdata.minutes=self.lineEdit_3.text()
                starttestdata.level=self.comboBox.currentText()
                starttestdata.fanspeed=self.comboBox_2.currentText()
                starttestdata.username=self.lineEdit_6.text()    
                self.rg=runninggraphwindow(self.name)
                self.rg.show()
        except ValueError:
            self.popup1=popup1(name='           Please enter all values !',name2='Close')
            self.popup1.show()


    
# class self(QWidget):
#     def __init__(self,name):
#        super().__init__() 
#        #parent=None
#        #super(secondwindow,self).__init__(parent)
#        #self.setGeometry(0, 100, 1024, 668)
#        self.title = "App2"
#        self.top = 0
#        self.left = 100
#        self.width = 1024
#        self.height = 668
#        self.name=name
#        self.InitUI1()
#     def call_b(self):
#         pass   
       
#     def InitUI1(self):
#         self.setWindowTitle(self.title)
#         #self.setStyleSheet("background-image: url(header.png);")
#         self.setGeometry(self.top, self.left, self.width, self.height)
#         self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
#         self.setStyleSheet('background-color:#030b32;')
#         #self.label = QLabel(self)
#         #self.pixmap = QPixmap('header.png')
#         #self.label.setPixmap(QPixmap('screens3.png'))
#         #self.label.setGeometry(0,0,1024,668)

# ##        self.s_temperature = extQLineEdit1(self)
# ##        self.s_temperature.setFont(QFont('Arial', 21))
# ##        self.s_temperature.setGeometry(469,140,493,53)
# ##        self.s_temperature.setStyleSheet('background-color:white; color: black')
# ##        self.s_temperature.setPlaceholderText('Enter Temerature')
# ##        self.s_temperature.speak.connect(partial(self.call_b,data='s_temperature'))

#         self.back = QPushButton('Back', self)
#         self.back.setGeometry(740,510,180,80)
#         self.back.setFont(QFont('Arial',19))
#         self.back.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
# border-width: 1px;
# border-radius: 15px;
# border-color: black;
# padding: 4px; color: black''')
#         #self.buttonWindow12.move(100, 100)
#         self.back.clicked.connect(self.call_first1)
# ##        self.starttest = QPushButton('Start Test', self)
# ##        self.starttest.setGeometry(700,20,250,90)
# ##        #self.buttonWindow12.move(100, 100)
# ##        self.starttest.clicked.connect(self.call_first2)
# ##        self.show()
#     def call_first1(self):
#         self.destroy()
#         gc.collect()
#         #self.close()
#         self.name.show()
#     def call_first2(self):
#         self.close()
#         self.mySubwindow = runninggraphwindow()
#         self.mySubwindow.show()
class contactkeyboard(QWidget): 
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):

        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,16,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QtGui.QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,133,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,133,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,133,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,237,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,237,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,237,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,341,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,341,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,341,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,445,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,445,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,445,297,100)
        kpo.setFont(QFont('Arial', 28))
        kpo.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kpo.clicked.connect(self.insert_text)
        
        kplus = QPushButton('+', self)
        kplus.setGeometry(45,549,296,100)
        kplus.setFont(QFont('Arial', 24))
        kplus.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kplus.clicked.connect(self.insert_text)
        
        kspace = QPushButton('space', self)
        kspace.setGeometry(358,549,296,100)
        kspace.setFont(QFont('Arial', 24))
        kspace.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kspace.clicked.connect(self.space1)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(670,549,297,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()

class numerickeyboard(QWidget): 
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,16,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QtGui.QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,133,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,133,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,133,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,237,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,237,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,237,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,341,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,341,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,341,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,445,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,445,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,445,297,100)
        kpo.setFont(QFont('Arial', 28))
        kpo.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kpo.clicked.connect(self.insert_text)
        
        kabc = QPushButton('abc', self)
        kabc.setGeometry(45,549,296,100)
        kabc.setFont(QFont('Arial', 24))
        kabc.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kabc.clicked.connect(self.change_abc)
        
        kspace = QPushButton('space', self)
        kspace.setGeometry(358,549,296,100)
        kspace.setFont(QFont('Arial', 24))
        kspace.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kspace.clicked.connect(self.space1)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(670,549,297,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()

    def change_abc(self):
        self.close()
        self.destroy()
        gc.collect()        

        self.capital_keyboard1=keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.capital_keyboard1.show()
    
class keyboard(QWidget):
    def __init__(self,mainwindowshow,previouswindow,entry_1):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entry_1=entry_1
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,16,200,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setMaxLength(self.length)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setText(self.entry_1)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('q', self)
        q.setGeometry(59,149,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('w', self)
        self.w.setGeometry(149,149,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('e', self)
        self.e.setGeometry(240,149,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('r', self)
        self.r.setGeometry(331,149,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('t', self)
        self.t.setGeometry(422,149,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('y', self)
        self.y.setGeometry(513,149,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('u', self)
        self.u.setGeometry(604,149,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('i', self)
        self.i.setGeometry(695,149,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('o', self)
        self.o.setGeometry(786,149,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('p', self)
        self.p.setGeometry(877,149,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('a', self)
        self.a.setGeometry(59,280,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('s', self)
        self.s.setGeometry(149,280,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('d', self)
        self.d.setGeometry(240,280,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('f', self)
        self.f.setGeometry(331,280,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('g', self)
        self.g.setGeometry(422,280,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('h', self)
        self.h.setGeometry(513,280,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('j', self)
        self.j.setGeometry(604,280,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('k', self)
        self.k.setGeometry(695,280,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('l', self)
        self.l.setGeometry(786,280,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,280,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,414,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('z', self)
        self.z.setGeometry(149,413,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('x', self)
        self.x.setGeometry(240,413,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('c', self)
        self.c.setGeometry(331,413,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('v', self)
        self.v.setGeometry(422,413,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('b', self)
        self.b.setGeometry(513,413,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('n', self)
        self.n.setGeometry(604,413,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('m', self)
        self.m.setGeometry(695,413,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,413,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,413,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,538,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,538,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.insert_text)
        
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,538,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,538,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.enter.clicked.connect(self.enter1)

    def insert_text(self,data):
            sender = self.sender()
##            print(sender.text())
##            cursor = self.entry.cursorPosition()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
##            print('cursor',cursor)
##            self.entry.cursorWordForward(True)
##            self.entry.setCursorPosition(2)
            #self.entry.setText(str(data))
            
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()

    def shift1(self):
        self.close()
        self.destroy()
        gc.collect()

        self.capital_keyboard1=capital_keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.capital_keyboard1.show()
    def change_numeric(self):
        self.close()
        self.destroy()
        gc.collect()
        self.numerickeyboard1=numerickeyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.numerickeyboard1.show()
        
        
            
class capital_keyboard(QWidget):
    def __init__(self,mainwindowshow,previouswindow,entry_small):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 668
        self.temp_user=''
        self.entrys=entry_small
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;')
        self.label.setGeometry(20,16,220,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black')
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setMaxLength(self.length)
        self.entry.setText(self.entrys)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('Q', self)
        q.setGeometry(59,149,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('W', self)
        self.w.setGeometry(149,149,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('E', self)
        self.e.setGeometry(240,149,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('R', self)
        self.r.setGeometry(331,149,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('T', self)
        self.t.setGeometry(422,149,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('Y', self)
        self.y.setGeometry(513,149,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('U', self)
        self.u.setGeometry(604,149,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('I', self)
        self.i.setGeometry(695,149,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('O', self)
        self.o.setGeometry(786,149,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('P', self)
        self.p.setGeometry(877,149,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('A', self)
        self.a.setGeometry(59,280,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('S', self)
        self.s.setGeometry(149,280,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('D', self)
        self.d.setGeometry(240,280,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('F', self)
        self.f.setGeometry(331,280,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('G', self)
        self.g.setGeometry(422,280,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('H', self)
        self.h.setGeometry(513,280,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('J', self)
        self.j.setGeometry(604,280,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('K', self)
        self.k.setGeometry(695,280,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('L', self)
        self.l.setGeometry(786,280,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,280,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,414,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('Z', self)
        self.z.setGeometry(149,413,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('X', self)
        self.x.setGeometry(240,413,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('C', self)
        self.c.setGeometry(331,413,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('V', self)
        self.v.setGeometry(422,413,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('B', self)
        self.b.setGeometry(513,413,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('N', self)
        self.n.setGeometry(604,413,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('M', self)
        self.m.setGeometry(695,413,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,413,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,413,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,538,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,538,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.insert_text)
        
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,538,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,538,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.enter.clicked.connect(self.enter1)
    
    def insert_text(self,data):
            sender = self.sender()
##            print(sender.text())
##            cursor = self.entry.cursorPosition()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
##            print('cursor',cursor)
##            self.entry.cursorWordForward(True)
##            self.entry.setCursorPosition(2)
            #self.entry.setText(str(data))
            
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            self.destroy()
            gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            self.edituser1.show()
    def shift1(self):
        self.close()
        self.destroy()
        gc.collect()

        self.keyboard1=keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.keyboard1.show()
    def change_numeric(self):
        self.close()
        self.destroy()
        gc.collect()
        self.numerickeyboard1=numerickeyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        self.numerickeyboard1.show()

class popup1(QDialog):
    def __init__(self,name=None,name2=None):
        super().__init__()
        self.title = "App"
        self.name=name
        self.name2=name2
        #self.tablefirsttime=0
        self.InitUI()
    def InitUI(self):
            #a=QFrame()
            #print("start")
            self.setGeometry(237,209,550,350)
            self.setWindowModality(Qt.ApplicationModal)
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
            self.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(self)
            self._gif.move(215,30)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("as4.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            movie.start()
            label1 = QLabel('Error',self)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(236,130)
            label2 = QLabel(self.name,self)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            no = QPushButton(self.name2, self)
            no.setGeometry(155,240,240,80)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(self.call_no)
            #self.show()
            #a.show()
    def call_no(self):
        self.close()
        self.destroy()
        gc.collect() 
        
class popup2(QDialog):
    def __init__(self,name=None,name2=None):
        super().__init__()
        self.title = "App"
        self.name=name
        self.name2=name2
        #self.tablefirsttime=0
        self.InitUI()
    def InitUI(self):
            #a=QFrame()
            #print("start")
            self.setGeometry(237,209,550,350)
            self.setWindowModality(Qt.ApplicationModal)
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
            self.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(self)
            self._gif.setGeometry(160,10,200,100)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("success2.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            movie.start()
            label1 = QLabel('Notification',self)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(220,130)
            label2 = QLabel(self.name,self)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            no = QPushButton(self.name2, self)
            no.setGeometry(165,240,240,80)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(self.call_no)
            #self.show()
            #a.show()
    def call_no(self):
        self.close()
        self.destroy()
        gc.collect() 
        
class UsersTable():

    def __init__(self,name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            #print(sqlite3.version)
        except sqlite3.Error as e:
            print("Failed connecting to database...")

    def create_table(self):
        c = self.cursor
        c.execute("""CREATE TABLE IF NOT EXISTS Userdata(Name TEXT,Employerid TEXT , Contact TEXT, Designation TEXT,ActionKey TEXT)""")
    def edit(self,query):#INSERT & UPDATE
        c = self.cursor
        c.execute(query)
        self.conn.commit()

    def select(self,query):#SELECT
        c = self.cursor
        c.execute(query)
        return c.fetchall()
    def delete(self,query):
        c = self.cursor
        c.execute(query)
        self.conn.commit()

class info():
    info1='none'


class subwindow2(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,parent=None):
       #parent=None
       super(subwindow2,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 0
       self.width = 1024
       self.height = 768
       self.InitUI()
       #self.InitUI()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    def updateTime(self):
        #print('faisal')
        #time = QTime.currentTime().toString()
        currentDT = datetime.now()
        date=currentDT.strftime("%d-%b-%Y")
        time=currentDT.strftime("%H:%M:%S")
        x_t=self.temp_call()
        #my_gauge.value=x_t
        degree_sign=u'\u00B0'
        self.ct1.setText(str(x_t)+degree_sign+'C')
        #self.gauge.update_value(x_t)
        self.date_label.setText(date)
        self.time_label.setText(time)   
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint) 
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('header.png'))
        self.label.setGeometry(0,0,1024,100)
        self.ct = QLabel("Current Temperature",self)
        self.ct.setFont(QFont('Arial', 20,QFont.Bold))
        #self.ct.setWeight(QFont(Bold))
        self.ct.setStyleSheet('background-color:#efeeef;')
        self.ct.setGeometry(400, 13,280,30)
        self.ct1 = QLabel(self)
        self.ct1.setFont(QFont('Arial', 21))
        self.ct1.setStyleSheet('background-color:#efeeef;')
        self.ct1.setGeometry(500, 48,100,30)
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont('Arial', 20,16))
        self.date_label.setStyleSheet('background-color:#efeeef;')
        self.date_label.setGeometry(800, 13,160,30)
        self.time_label = QLabel(self)
        self.time_label.setFont(QFont('Arial', 20,16))
        self.time_label.setStyleSheet('background-color:#efeeef;')
        self.time_label.setGeometry(830, 48,150,30)
        #self.ct.setObjectName("label")
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(100)
        self.mySubwindow=subwindow()
       
        #self.mySubwindow.createWindow(1024,668)
        self.mySubwindow.show()

class subwindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,parent=None):
       #parent=None
       super(subwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI()
       #self.InitUI()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    def updateTime(self):
        #print('faisal')
        time = QTime.currentTime().toString()
        x_t=self.temp_call()
        #my_gauge.value=x_t
       #self.label.setText(str(x_t))
        self.gauge.update_value(x_t)
        # if (c_to_f==0):
        #     my_gauge.value_min = 0
        #     my_gauge.value_max = 300
        # if (c_to_f==1):
        #     my_gauge.value_min = 32
        #     my_gauge.value_max = 572

       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setAttribute(Qt.WA_AcceptTouchEvents)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,150,320, 340)
        self.gauge.setStyleSheet("background-color:#f7f7ff;")
        #self.Form = QtWidgets.QWidget()
        #self.ui = Ui_Form()
        #self.ui.setupUi(self.Form)
        #self.Form.show()
        # self.label = QLabel('uu',self)
        # self.label.setGeometry(165, 5, 61, 16)
        # self.label.setObjectName("label")
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(10)
        #self.gauge.show()
        #self.s1 = Switch(self)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        buttonWindow1 = QPushButton('Start Test', self)
        buttonWindow1.setFont(QFont('Arial', 27))
        buttonWindow1.setGeometry(20,60,285,155)
        buttonWindow1.setStyleSheet('background-image: url(start.png);')
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        Settings = QPushButton('Settings  ', self)
        Settings.setFont(QFont('Arial', 27))
        Settings.setGeometry(20,250,285,155)
        Settings.setStyleSheet('background-image: url(setting.png);')
        Settings.clicked.connect(self.settingswindow)
        User = QPushButton('User      ', self)
        User.setFont(QFont('Arial', 27))
        User.setGeometry(20,440,285,155)
        User.setStyleSheet('background-image: url(user.png);')
        User.clicked.connect(self.userswindow)
        Results = QPushButton('Results', self)
        Results.setFont(QFont('Arial', 27))
        Results.setGeometry(330,60,285,155)
        Results.setStyleSheet('background-image: url(Result.png);')
        Results.clicked.connect(self.resultswindow)
        About = QPushButton('About  ', self)
        About.setFont(QFont('Arial', 27))
        About.setGeometry(330,250,285,155)
        About.setStyleSheet('background-image: url(about.png);')
        About.clicked.connect(self.aboutwindow)
        Damper = QPushButton('Damper ', self)
        Damper.setFont(QFont('Arial', 27))
        Damper.setGeometry(330,440,285,155)
        Damper.setStyleSheet('background-image: url(damper.png);')
        Damper.clicked.connect(self.damperwindow)
        #objgraph.show_refs(self, filename='sample-graph.png')
        self.show()

    def buttonWindow1_onClick(self):
        self.close()
        self.rgwindow = startwindow(self)
        self.rgwindow.show()
    def settingswindow(self):
        pass
        #self.close()
        #self.swindow = settingswindow()
        #self.swindow.show()
    def userswindow(self):
        self.close()
        self.uwindow = userswindow(self)
        self.uwindow.show()
    def resultswindow(self):
        self.close()
        self.rw=result_window(self)
        self.rw.show()
        #self.close()
        #self.rswindow = resultswindow()
        #self.rswindow.show()
    def aboutwindow(self):
        self.close()
        self.a_s=about_screen(self)
        self.a_s.show()
        #self.close()
        #self.abwindow = aboutwindow()
        #self.abwindow.show()
    def damperwindow(self):
        self.close()
        self.d_s=damper_screen(self)
        self.d_s.show()
        #self.close()
        #self.dwindow = damperwindow()
        #self.dwindow.show()

        #parent.destroy()
        #url.focusInEvent(QFocusEvent)
        #self.emit(SIGNAL("clicked()"))


class userswindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    #FROM, SUBJECT, DATE = range(3)
    top = 0
    def __init__(self,name):
       super().__init__()
        
       #parent=None
       #super(instrumentwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.insertfirsttime=0
       self.tablefirsttime=0
       self.m=name
       #self.e=name2
       #info.info1=2
       #print(info.info1)
       self.InitUI()
       #print(sys.getsizeof(instrumentwindow))
       #self.show()
    # def paintEvent(self, e):

    #     qp = QPainter()
    #     qp.begin(self)
    #     self.drawRectangles(qp)
    #     qp.end() 
    # def drawRectangles(self, qp):
      
    #     col = QColor(0, 0, 0)
    #     col.setNamedColor('#d4d4d4')
    #     qp.setPen(QPen(Qt.black, 2))
    #     #qp.setwidth(2)

    #     qp.setBrush(QColor(255, 255, 255))
    #     qp.drawRect(10, 185, 75, 54)

    #     qp.setBrush(QColor(255, 255, 255))
    #     qp.drawRect(85, 185, 225, 54)

    #     qp.setBrush(QColor(255, 255, 255))
    #     qp.drawRect(310, 185, 225, 54)

    #     qp.setBrush(QColor(255, 255, 255))
    #     qp.drawRect(510, 185, 225, 54) 

    #     qp.setBrush(QColor(255, 255, 255))
    #     qp.drawRect(730, 185, 225, 54)  
     
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Users Data',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,20,220,50)

        # self.refno = QLabel('Ref No',self)
        # self.refno.setFont(QFont('Arial', 16))
        # self.refno.setStyleSheet('background-color:#f7f7ff; color: black')
        # self.refno.move(14,200)
        
        # self.adduser = QLabel('User Name',self)
        # self.adduser.setFont(QFont('Arial', 19))
        # self.adduser.setStyleSheet('background-color:#f7f7ff; color: black;')
        # self.adduser.move(90,200)

        # self.e_id = QLabel('Employer Id',self)
        # self.e_id.setFont(QFont('Arial', 19))
        # self.e_id.setStyleSheet('background-color:#f7f7ff; color: black')
        # self.e_id.move(290,200)

        # self.contact = QLabel('Contact',self)
        # self.contact.setFont(QFont('Arial', 19))
        # self.contact.setStyleSheet('background-color:#f7f7ff; color: black')
        # self.contact.move(530,200)

        # self.designation = QLabel('Designation',self)
        # self.designation.setFont(QFont('Arial', 19))
        # self.designation.setStyleSheet('background-color:#f7f7ff; color: black')
        # self.designation.move(770,200)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,100,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_back)
        self.addnewuser = QPushButton('Add New User', self)
        self.addnewuser.setGeometry(30,100,240,70)
        self.addnewuser.setFont(QFont('Arial', 21))
        self.addnewuser.setStyleSheet('background-color:#4299ff; color: white')
        self.addnewuser.clicked.connect(self.call_add)
        self.edituser = QPushButton('Edit User', self)
        self.edituser.setGeometry(270,100,240,70)
        self.edituser.setFont(QFont('Arial', 21))
        self.edituser.setStyleSheet('background-color:#4299ff; color: white')
        self.edituser.clicked.connect(self.call_edit)
        self.deleteuser = QPushButton('Delete User', self)
        self.deleteuser.setGeometry(510,100,240,70)
        self.deleteuser.setFont(QFont('Arial', 21))
        self.deleteuser.setStyleSheet('background-color:#4299ff; color: white')
        self.deleteuser.clicked.connect(self.call_delete1)

# tree = QTreeView()
# tree.model = QtGui.QAbstractItemModel()
# tree.setModel(tree.model)

# size = QtCore.QSize(20, 20)
# index = tree.model.index(row, col)   # row, col are your own
# tree.model.setData(index, size, QtCore.Qt.SizeHintRole)

# delegate = MyDelegate()
# tree.setItemDelegate(delegate)

        self.dataView = QTreeWidget(self)
        #self.dataView.model=QAbstractItemModel()
        self.dataView.setRootIsDecorated(False)
        #self.dataView.setExpandsOnDoubleClick(True)
        #self.dataView.setContentsMargins(0,20,0,0)
        #self.dataView.setUniformRowHeights(True)
        #self.dataView.uniformRowHeights()
        #self.dataView.setAlternatingRowColors(True)
        self.dataView.setHeaderLabels(['Ref No','User Name','Employer Id','Contact','Designation'])
        #self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size: 21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        #item=QTreeWidgetItem(['Ref No','User Name','Employer Id','Contact','Designation'])
        #self.dataView.addTopLevelItem(item)
        #self.dataView.header().setStretchLastSection(False)
        #self.dataView.header().setResizeMode(6, QHeaderView.Stretch)
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        #self.dataView.header().setSelected(False)
        #self.dataView.header().setStretchLastSection(False)
        #self.dataView.header().sectionsMovable()
        #self.dataView.header().setResizeMode(0, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(3, QHeaderView.Stretch)
        #self.dataView.header().setResizeMode(4, QHeaderView.Stretch)
        #self.dataView.header().setSectionResizeMode(Fixed)
        #font=QFont()            
        #font.setPointSize(22)
        #self.dataView.setPointSize(24)
        #self.dataView.header().setFont(font)
        #tree=QtGui.QTreeWidget()
#tree.setHeaderLabels(['One','Two','Tree','Four','Five'])
# font=QtGui.QFont()            
# font.setPointSize(24)
# tree.header().setFont(font)
        #self.dataView.setHeaderHidden(True)
        #self.dataView.Header().setVisible(False)
       #self.dataView.header().setResizeMode(False)
        self.dataView.setColumnCount(5)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,100)
        self.dataView.setColumnWidth(1,230)
        self.dataView.setColumnWidth(2,230)
        self.dataView.setColumnWidth(3,230)
        self.dataView.setColumnWidth(4,280)
        self.dataView.setColumnWidth(5,0)
        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        #self.dataView.setIconSize(QSize(32,32))
        self.create_table()
        self.insert_data()

##        l=[['faisal111111111111111111','12345','',''],['faisal','','',''],['faisal','','','']]
##        for x in l:
##           QTreeWidgetItem(self.dataView,x) 

        self.dataView.setGeometry(10,200,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.show()
    @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(5)
        #print(getChildNode)
##            
##        #self.dataView.setResizable(True)
##        #self.dataView.horizontalScrollBar().setEnabled(true)
##        #self.scrollarea=QScrollBar(self.dataView)
##        #self.scrollarea.setEnabled(True)
##        #self.scrollarea.setMaximum(255)
##        #mainLayout = QVBoxLayout()
##        #mainLayout.addWidget(self.dataGroupBox)
##        #self.setLayout(mainLayout)

        
##    def __del__(self):
##        #print("destructor called")
##        self.destroy()
##        gc.collect()

    def create_table(self):
        if(self.tablefirsttime==0):
            self.tablefirsttime=1
            test = UsersTable("faisal.db")
            test.create_table()

        
    def insert_data(self):
        #if(self.insertfirsttime==0):
            self.insertfirsttime=1
            l=[]
            test = UsersTable("faisal.db")
            x=test.select("SELECT * FROM Userdata order by ActionKey DESC")
            for row in x:
                #print(row)
                l.append(row)
            for i,x in enumerate(l):
                #print(i,x)
                QTreeWidgetItem(self.dataView,[str(i),x[0],x[1],x[2],x[3],x[4]]) 
            

    def call_home(self):
        self.close()
        
        gc.collect() 
        self.destroy()
        
        self.svwindow = subwindow()
        self.svwindow.show()
    def call_back(self):
            self.close()
            self.destroy()
            gc.collect()
            self.m.show()
    
    def call_add(self):
        global getChildNode
        getChildNode=''
        adduserdata.username=''
        adduserdata.employerid=''
        adduserdata.contact=''
        adduserdata.designation=''
        self.close()
        self.destroy()
        gc.collect()
        self.y=adduser(self.m)
        self.y.show()
        #self.close()
        #self.destroy()
        #gc.collect()
        #y=adduser()                            
        #y.exec_()
        #self.destroy()
        
        #gc.collect() 
        #self.svwindow = adduser()
        #self.svwindow.show()
        #del self
    def call_delete1(self):
        global getChildNode
        #self.close()
        #self.svwindow = adduser()
        #self.svwindow.show()
        def call_no():
                a.close()
                gc.collect() 
                a.destroy()
        def call_delete():
            global getChildNode
            l=[]
            #sip.delete(getChildNode)
            self.dataView.clear()
            test = UsersTable("faisal.db")
            #y=test.delete(f"SELECT * from stufftoplot WHERE {temp_search} LIKE '{mg}%';") 
            y=test.delete(f"DELETE from Userdata where ActionKey={getChildNode}") 
            x=test.select("SELECT * FROM Userdata order by ActionKey DESC")
            for row in x:
                    #print(row)
                    l.append(row)
            for i,x in enumerate(l):
                    #print(i,x)
                    QTreeWidgetItem(self.dataView,[str(i),x[0],x[1],x[2],x[3],x[4]])

            a.close()
            a.destroy()
            gc.collect()
            getChildNode=''
            #def call_no(self):
                #a.close()
        try:
            if len(getChildNode)==0:
                raise ValueError 
                #self.m=popup1(name='    Please select any user to continue',name2='Okay!')
                #self.m.show()
                
            
            print(len(getChildNode))
            a=QFrame()
            a.setGeometry(237,209,550,350)
            a.setWindowModality(Qt.ApplicationModal)
            a.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
            
            #a.setFocus()
            #a.activateWindow()
            #a.setWindowModality(QtCore.Qt.ApplicationModal)
            #a.setWindowState(a.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
            a.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(a)
            self._gif.move(215,30)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("as4.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            #movie.setDuration(1000)
            #movie.setLoopCount(2)
            #movie.setStartValue(QColor(0, 0, 0))
            #movie.setEndValue(QColor(255, 255, 255))
            #print(movie.state())
            movie.start()
            label1 = QLabel('Error',a)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(236,130)
            label2 = QLabel('Are you sure you want to delete this user !',a)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            yes_delete = QPushButton('Yes !', a)
            yes_delete .setGeometry(50,240,240,90)
            yes_delete .setFont(QFont('Arial', 21))
            yes_delete .setStyleSheet('background-color:#d00403; color: white')
            yes_delete .clicked.connect(call_delete)
            no = QPushButton('No', a)
            no.setGeometry(270,240,240,90)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(call_no)
            a.show()
        except:
            print("error")
            self.popup1=popup1(name='    Please select any user to continue',name2='Okay!')
            self.popup1.show()

        
        #if( movie.frameCount()>=21):
            #movie.stop()
        #movie.stop()
        #movie.jumpToFrame(0)
        #label = QLabel('', self)
        #movie = QtGui.QMovie("as2.gif")
        #label.setMovie(movie)
        #movie.start() 
        
        
    def call_edit(self):
        global getChildNode
        try:
            if len(getChildNode)==0:
                raise ValueError 
            self.close()
            self.destroy()
            gc.collect() 
            #info.info1=getChildNode
            #self.e.show()
            keydata.editdata=getChildNode
            self.edituser=edituser(self.m,getChildNode)
            self.edituser.show()
            getChildNode=''
        except:
            print("error")
            self.popup1=popup1(name='      Please select any user to edit!',name2='Okay!')
            self.popup1.show()
##        try:
##            if len(getChildNode)==0:
##                raise ValueError 
##            self.close()
##            self.e.show()
##            #self.svwindow = edituser(getChildNode)
##            getChildNode=''
##            #self.svwindow.show()
##            gc.collect() 
##            self.destroy()
##        except ValueError:
##            print("error")
##            self.m=popup1(name='      Please select any user to edit!',name2='Okay!')
##            self.m.show()
    
        
class extQLineEdit(QLineEdit):
    def __init__(self,parent,get_entry):
        self.get_entry=get_entry
        QLineEdit.__init__(self,parent)
    def mousePressEvent(self,QMouseEvent):
        print("check",self.get_entry)
        if(self.get_entry=="e_user"):
            self.nk=numerickeyboard('')
            self.nk.show()
class extQLineEdit1(QLineEdit):
    #closeApp = pyqtSignal()
    #trigger = pyqtSignal()
    speak = Signal(str) 
    def __init__(self,parent):
          super(QLineEdit,self).__init__(parent)
    def mousePressEvent(self,QMouseEvent):
    #     self.trigger.emit()
         self.speak.emit('clicked()') 
         print("check")


class adduser(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    #FROM, SUBJECT, DATE = range(3)
    def __init__(self,name):
       #parent=None
       super().__init__() 
       #super(adduser,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.temp_user=''
       self.r=name
       self.InitUI()
       self.inserteditdata()
    def call_b(self,data):
        print("asdss",data)
        if(data=="a_user"):
            user_data=self.e_user.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            self.nk.show()
        elif(data=="a_employer"):
            user_data=self.e_employer.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            self.nk.show()
        elif(data=="a_contact"):
            user_data=self.e_contact.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=contactkeyboard(self.r,data,user_data)
            self.nk.show()
        elif(data=="a_designation"):
            user_data=self.e_designation.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            self.nk.show()
            
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('userscreen.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel('Add New User',self)
        self.label.setFont(QFont('Arial', 22))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.move(460,35)

        back = QPushButton('Back', self)
        back.setGeometry(755,447,190,75)
        back.setFont(QFont('Arial', 21))
        back.setStyleSheet('background-color:#4299ff; color: white')
        back.clicked.connect(self.call_back)

        self.addnewuser = QPushButton('Add User', self)
        self.addnewuser.setGeometry(535,447,200,75)
        self.addnewuser.setFont(QFont('Arial', 21))
        self.addnewuser.setStyleSheet('background-color:#4299ff; color: white')
        self.addnewuser.clicked.connect(self.call_add)


#self.entry = extQLineEdit(self,'entry2')
        self.e_user = extQLineEdit1(self)
        self.e_user.setFont(QFont('Arial', 21))
        self.e_user.setGeometry(469,140,493,53)
        self.e_user.setStyleSheet('background-color:white; color: black')
        self.e_user.setPlaceholderText('Enter User Name')
        self.e_user.speak.connect(partial(self.call_b,data='a_user'))
        #q.clicked.connect(partial(self.insert_text,data='q'))
        #self.e_user.speak.connect(self.call_b)
        #self.e_user.speak.emit("Hello everybody!")  
        #QtCore.QObject.connect(self.e_user, QtCore.SIGNAL('clicked()'), call_b) 
        #self.e_user.connect(self.call_b)

        self.e_employer = extQLineEdit1(self)
        self.e_employer.setFont(QFont('Arial', 21))
        self.e_employer.setGeometry(469,215,492,53)
        self.e_employer.setStyleSheet('background-color:white; color: black')
        self.e_employer.setPlaceholderText('Enter Employer Id')
        self.e_employer.speak.connect(partial(self.call_b,data='a_employer'))

        self.e_contact = extQLineEdit1(self)
        self.e_contact.setFont(QFont('Arial', 21))
        self.e_contact.setGeometry(469,285,493,53)
        self.e_contact.setStyleSheet('background-color:white; color: black')
        self.e_contact.setPlaceholderText('Enter Contact')
        self.e_contact.speak.connect(partial(self.call_b,data='a_contact'))

        self.e_designation = extQLineEdit1(self)
        self.e_designation.setFont(QFont('Arial', 21))
        self.e_designation.setGeometry(469,355,492,53)
        self.e_designation.setStyleSheet('background-color:white; color: black')
        self.e_designation.setPlaceholderText('Enter Designation')
        self.e_designation.speak.connect(partial(self.call_b,data='a_designation'))

        self.user = QLabel('Enter Name',self)
        self.user.setFont(QFont('Arial', 19))
        self.user.setStyleSheet('background-color:white; color: black')
        self.user.move(70,170)

        self.employer_id = QLabel('Enter Employer ID',self)
        self.employer_id.setFont(QFont('Arial', 19))
        self.employer_id.setStyleSheet('background-color:white; color: black')
        self.employer_id.move(70,240)

        self.contact = QLabel('Enter Contact',self)
        self.contact.setFont(QFont('Arial', 19))
        self.contact.setStyleSheet('background-color:white; color: black')
        self.contact.move(70,310)

        self.designation = QLabel('Enter Designation',self)
        self.designation.setFont(QFont('Arial', 19))
        self.designation.setStyleSheet('background-color:white; color: black')
        self.designation.move(70,380)
        #self.exec_()
##    def __del__(self):
##        #print("destructor called")
##        self.destroy()
##        gc.collect()
    def inserteditdata(self):
            self.e_user.setText(adduserdata.username)
            self.e_employer.setText(adduserdata.employerid)
            self.e_contact.setText(adduserdata.contact)
            self.e_designation.setText(adduserdata.designation)
    def call_back(self):
        #self.destroy()
        self.close()
        self.destroy()
        #weakref.ref(dialog, self.dialogs.remove)
        gc.collect() 
        self.m=userswindow(self.r)
        self.m.show()

        
        #dialog.destroyed.connect(self.on_destroyed)
        #self.dialogs.append(dialog)
        #self.m.exec_()
        #self.m.show()
        #del self
    def call_add(self):
        self.user_name = self.e_user.text()
        self.user_employerid = self.e_employer.text()
        self.user_contact = self.e_contact.text()
        self.user_designation = self.e_designation.text()
        try:
            if(len(self.user_name)==0 or len(self.user_employerid)==0):
               raise NameError
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute("Select Name from Userdata")
            for x in y:
                print(x)
                for n in x:
                    if (self.user_name.lower()==n.lower()):
                        #print('True')
                        self.temp_user=True
                #self.m=popup1(name='',name2='')
                #self.m.show()
            if(self.temp_user==True):
                self.temp_user=False
                raise ValueError
            currentDT = datetime.now()
            key_1=currentDT.strftime("%Y%m%d%H%M%S")
            print(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1)
            #conn = sqlite3.connect('faisal.db')
            #c = conn.cursor()
            c.execute("INSERT INTO Userdata(Name,Employerid,Contact,Designation,ActionKey) VALUES(?,?,?,?,?)",(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1))
            conn.commit()
            c.close()
            conn.close()
            self.close()
            self.destroy()
            gc.collect()
            self.swindow = userswindow(self.r)
            self.swindow.show()
            self.popup2=popup2(name='                User has been added !',name2='Close')
            self.popup2.show()
            
            
        except ValueError:
                print("error")
                self.popup1=popup1(name='           User is already present !',name2='Close')
                self.popup1.show()
        except NameError:
                print("error")
                self.popup1=popup1(name='            Please Enter All Values !',name2='Close')
                self.popup1.show()
            

class edituser(QDialog):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    #FROM, SUBJECT, DATE = range(3)
    def __init__(self,name,editdata):
       #parent=None
       super().__init__() 
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.r=name

       self.editdata=editdata
       self.temp_user=''
       
       

       #print(self.name)
       #print(instrumentwindow.top)
       self.InitUI()
       self.inserteditdata()
       
    def call_b(self,data):
        print("asdss",data)
        if(data=="e_user"):
            user_data=self.e_user.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            self.nk.show()
        elif(data=="e_employer"):
            user_data=self.e_employer.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            self.nk.show()
        elif(data=="e_contact"):
            user_data=self.e_contact.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=contactkeyboard(self.r,data,user_data)
            self.nk.show()
        elif(data=="e_designation"):
            user_data=self.e_designation.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            self.nk.show()
       

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#b3ccff;')
##        self.bg = QLabel(self)
##        #self.pixmap = QPixmap('header.png')
##        self.bg.setPixmap(QPixmap('userscreen.png'))
##        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel('Edit Current User',self)
        self.label.setFont(QFont('Arial', 22))
        self.label.setStyleSheet('background-color:#b3ccff; color: black')
        self.label.move(460,35)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(755,447,190,75)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_back)

        self.addnewuser = QPushButton('Edit User', self)
        self.addnewuser.setGeometry(535,447,200,75)
        self.addnewuser.setFont(QFont('Arial', 21))
        self.addnewuser.setStyleSheet('background-color:#4299ff; color: white')
        self.addnewuser.clicked.connect(self.call_edit)

        self.e_user = extQLineEdit1(self)
        self.e_user.setFont(QFont('Arial', 21))
        self.e_user.setGeometry(469,140,493,53)
        self.e_user.setStyleSheet('background-color:white; color: black')
        self.e_user.setPlaceholderText('Enter User Name')
        self.e_user.speak.connect(partial(self.call_b,data='e_user'))


        self.e_employer = extQLineEdit1(self)
        self.e_employer.setFont(QFont('Arial', 21))
        self.e_employer.setGeometry(469,215,492,53)
        self.e_employer.setStyleSheet('background-color:white; color: black')
        self.e_employer.setPlaceholderText('Enter Employer Id')
        self.e_employer.speak.connect(partial(self.call_b,data='e_employer'))

        self.e_contact = extQLineEdit1(self)
        self.e_contact.setFont(QFont('Arial', 21))
        self.e_contact.setGeometry(469,285,493,53)
        self.e_contact.setStyleSheet('background-color:white; color: black')
        self.e_contact.setPlaceholderText('Enter Contact')
        self.e_contact.speak.connect(partial(self.call_b,data='e_contact'))

        self.e_designation = extQLineEdit1(self)
        self.e_designation.setFont(QFont('Arial', 21))
        self.e_designation.setGeometry(469,355,492,53)
        self.e_designation.setStyleSheet('background-color:white; color: black')
        self.e_designation.setPlaceholderText('Enter Designation')
        self.e_designation.speak.connect(partial(self.call_b,data='e_designation'))

        self.user = QLabel('Enter Name',self)
        self.user.setFont(QFont('Arial', 19))
        self.user.setStyleSheet('background-color:#b3ccff; color: black')
        self.user.move(70,170)

        self.employer_id = QLabel('Enter Employer ID',self)
        self.employer_id.setFont(QFont('Arial', 19))
        self.employer_id.setStyleSheet('background-color:#b3ccff; color: black')
        self.employer_id.move(70,240)

        self.contact = QLabel('Enter Contact',self)
        self.contact.setFont(QFont('Arial', 19))
        self.contact.setStyleSheet('background-color:#b3ccff; color: black')
        self.contact.move(70,310)

        self.designation = QLabel('Enter Designation',self)
        self.designation.setFont(QFont('Arial', 19))
        self.designation.setStyleSheet('background-color:#b3ccff; color: black')
        self.designation.move(70,380)




##    def __del__(self):
##        #print("destructor called")
##        self.destroy()
##        gc.collect()

    def call_back(self):
        self.destroy()
        #weakref.ref(dialog, self.dialogs.remove)
        gc.collect() 

        self.close()
        self.m=userswindow(self.r)
        self.m.show()

    def inserteditdata(self):
        if(len(self.editdata)>0):
            l=[]
            
            try:
                test = UsersTable("faisal.db")
                y=test.select(f"Select * from Userdata where ActionKey={self.editdata}")
                for row in y:
                        print(row)
                        l.append(row)
                self.e_user.setText(l[0][0])
                self.e_employer.setText(l[0][1])
                self.e_contact.setText(l[0][2])
                self.e_designation.setText(l[0][3])
                keydata.username=self.e_user.text()
                keydata.employerid=self.e_employer.text()
                keydata.contact=self.e_contact.text()
                keydata.designation=self.e_designation.text()

            except:
                print('insideeditdataerror')
        else:
            self.e_user.setText(keydata.username)
            self.e_employer.setText(keydata.employerid)
            self.e_contact.setText(keydata.contact)
            self.e_designation.setText(keydata.designation)

            
    def call_edit(self):
        #test = UsersTable("faisal.db")
        #y=test.delete(f"SELECT * from stufftoplot WHERE {temp_search} LIKE '{mg}%';") 
        #y=test.delete(f"DELETE from Userdata where ActionKey={self.name}") 
        self.user_name = self.e_user.text()
        self.user_employerid = self.e_employer.text()
        self.user_contact = self.e_contact.text()
        self.user_designation = self.e_designation.text()
        try:
            if(len(self.user_name)==0 or len(self.user_employerid)==0):
               raise NameError
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute("Select Name from Userdata")
            for x in y:
                print(x)
                for n in x:
                    if (self.user_name.lower()==n.lower()):
                        #print('True')
                        self.temp_user=True
                #self.m=popup1(name='',name2='')
                #self.m.show()
            if(self.temp_user==True):
                self.temp_user=False
                raise ValueError
            currentDT = datetime.now()
            key_1=currentDT.strftime("%Y%m%d%H%M%S")
            #print(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1)
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            c.execute(f"DELETE from Userdata where ActionKey={keydata.editdata}") 
            c.execute("INSERT INTO Userdata(Name,Employerid,Contact,Designation,ActionKey) VALUES(?,?,?,?,?)",(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),keydata.editdata))
            conn.commit()
            c.close()
            conn.close()
            self.close()
            self.destroy()
            gc.collect()
            self.swindow = userswindow(self.r)
            self.swindow.show()
            self.popup2=popup2(name='                User has been edited !',name2='Close')
            self.popup2.show()

        except ValueError:
                print("error")
                self.popup1=popup1(name='           User is already present !',name2='Close')
                self.popup1.show()
        except NameError:
                print("error")
                self.popup1=popup1(name='            Please Enter All Values !',name2='Close')
                self.popup1.show()

class starttestdata():
    temperature=''
    hours=''
    minutes=''
    level=''
    fanspeed=''
    username=''
    key=''
class adduserdata():
    username=''
    employerid=''
    contact=''
    designation=''

class keydata():
    username=None
    employerid=''
    contact=''
    designation=''
    editdata=''
if __name__ == '__main__':
    import sys
    #from mem_top import mem_top
    #print(mem_top())
    app = QApplication(sys.argv)
    #gc.enable()
    w = subwindow2()
    w.show()
    sys.exit(app.exec_())
