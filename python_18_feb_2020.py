import sys

from functools import partial
from python_7_feb_2020 import Switch,AnalogGaugeWidget
from time import sleep
import sqlite3
import gc
from datetime import datetime
from PyQt5 import sip
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import math
from PyQt5 import QtWidgets, uic,sip
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
from PyQt5.QtWidgets import QScroller

# print("Try5: analoggaugewidget.py")
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
# QtWidgets -> QWidget
# QtWidgets -> QApplication

from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont
from PyQt5.QtGui import QPainter, QFontMetrics, QConicalGradient
# QtGui -> QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient

from PyQt5.QtCore import Qt ,QTime, QTimer, QPoint, QPointF, QRect, QSize
from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5.QtCore import QPropertyAnimation, QRectF, QSize, Qt, pyqtProperty
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import (
    QAbstractButton,
    QApplication,
    QHBoxLayout,
    QSizePolicy,
    QWidget,
)

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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"
##        self.top = 100
##        self.left = 100
##        self.width = 680
##        self.height = 500
##        self.InitUI()
        self.setStyleSheet('background-color:#f7f7ff;')
        #self.gauge=AnalogGaugeWidget()
        #self.gauge.use_timer_event=True
        #self.gauge.setGeometry(670,265,320, 340)
        #self.gauge.show()
        #self.gauge.show()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 1024, 768)
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('header.png'))
        self.label.setGeometry(0,0,1024,100)
        #self.layout = QGridLayout(self)
        #self.layout.addWidget(self.label, 0, 0)
        #self.layout.addWidget(self.gauge, 0, 1)
        self.mySubwindow=subwindow()
        #self.mySubwindow.createWindow(1024,668)
        self.mySubwindow.show()
        #self.gauge=AnalogGaugeWidget(self)
        #self.gauge.setGeometry(0,0,320, 340)
        #self.gauge.setStyleSheet("background-color:#f7f7ff;")
        #self.gauge.show()
        #self.pushButton = QPushButton(self)
        #self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        #self.pushButton.setText('Click me!')
        #self.pushButton.clicked.connect(self.goMainWindow)

           
    def goMainWindow(self):
            self.mySubwindow = subwindow()
            self.mySubwindow.createWindow(1024,668)
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
       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,150,320, 340)
        self.gauge.setStyleSheet("background-color:#f7f7ff;")
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
        self.show()

    def buttonWindow1_onClick(self):
        self.close()
        self.rgwindow = secondwindow()
        self.rgwindow.show()
    def settingswindow(self):
        self.close()
        self.swindow = settingswindow()
        self.swindow.show()
    def userswindow(self):
        self.close()
        self.uwindow = userswindow(self)
        self.uwindow.show()
    def resultswindow(self):
        self.close()
        self.rswindow = resultswindow()
        self.rswindow.show()
    def aboutwindow(self):
        self.close()
        self.abwindow = aboutwindow()
        self.abwindow.show()
    def damperwindow(self):
        self.close()
        self.dwindow = damperwindow()
        self.dwindow.show()

        #parent.destroy()
        #url.focusInEvent(QFocusEvent)
        #self.emit(SIGNAL("clicked()"))
class numerickeyboard(QWidget):
    def __init__(self,entry_numeric):
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
        if(self.previouswindow=='e_user' ):
            self.labelshow="Enter User Name"
        elif(self.previouswindow=='e_employer' ):
            self.labelshow="Enter Employer ID"
        elif(self.previouswindow=='e_designation' ):
            self.labelshow="Enter Designation"
        elif(self.previouswindow=='e_contact' ):
            self.labelshow="Enter Contact"

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('numeric2.png'))
        self.bg.setGeometry(0,0,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;')
        self.label.setGeometry(20,16,220,85)
        self.entry = extQLineEdit(self,'entry2')
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black')
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setFocusPolicy(QtCore.Qt.NoFocus)
        #lineedit = QtGui.QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,133,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('background-color:white; color: black')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,133,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('background-color:white; color: black')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,133,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('background-color:white; color: black')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,237,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('background-color:white; color: black')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,237,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('background-color:white; color: black')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,237,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('background-color:white; color: black')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,341,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('background-color:white; color: black')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,341,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('background-color:white; color: black')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,341,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('background-color:white; color: black')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,445,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('background-color:white; color: black')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,445,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('background-color:white; color: black')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,445,297,100)
        kpo.setFont(QFont('Arial', 24))
        kpo.setStyleSheet('background-color:white; color: black')
        kpo.clicked.connect(self.insert_text)
        
        kabc = QPushButton('abc', self)
        kabc.setGeometry(45,549,296,100)
        kabc.setFont(QFont('Arial', 24))
        kabc.setStyleSheet('background-color:white; color: black')
        kabc.clicked.connect(self.change_abc)
        
        kspace = QPushButton('space', self)
        kspace.setGeometry(358,549,296,100)
        kspace.setFont(QFont('Arial', 24))
        kspace.setStyleSheet('background-color:white; color: black')
        kspace.clicked.connect(self.space1)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(670,549,297,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('background-color:#4299ff;color: black')
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

    def change_abc(self):
        self.close()
        self.destroy()
        gc.collect()
        self.capital_keyboard1=keyboard(self.entry.text())
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
        if(self.previouswindow=='e_user' ):
            self.labelshow="Enter User Name"
        elif(self.previouswindow=='e_employer' ):
            self.labelshow="Enter Employer ID"
        elif(self.previouswindow=='e_designation' ):
            self.labelshow="Enter Designation"
        elif(self.previouswindow=='e_contact' ):
            self.labelshow="Enter Contact"


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('DA_1217key1.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 18))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;')
        self.label.setGeometry(20,16,220,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black')
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setText(self.entry_1)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('q', self)
        q.setGeometry(59,149,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('background-color:white; color: black')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('w', self)
        self.w.setGeometry(149,149,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('background-color:white; color: black')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('e', self)
        self.e.setGeometry(240,149,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('background-color:white; color: black')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('r', self)
        self.r.setGeometry(331,149,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('background-color:white; color: black')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('t', self)
        self.t.setGeometry(422,149,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('background-color:white; color: black')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('y', self)
        self.y.setGeometry(513,149,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('background-color:white; color: black')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('u', self)
        self.u.setGeometry(604,149,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('background-color:white; color: black')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('i', self)
        self.i.setGeometry(695,149,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('background-color:white; color: black')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('o', self)
        self.o.setGeometry(786,149,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('background-color:white; color: black')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('p', self)
        self.p.setGeometry(877,149,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('background-color:white; color: black')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('a', self)
        self.a.setGeometry(59,280,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('background-color:white; color: black')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('s', self)
        self.s.setGeometry(149,280,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('background-color:white; color: black')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('d', self)
        self.d.setGeometry(240,280,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('background-color:white; color: black')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('f', self)
        self.f.setGeometry(331,280,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('background-color:white; color: black')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('g', self)
        self.g.setGeometry(422,280,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('background-color:white; color: black')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('h', self)
        self.h.setGeometry(513,280,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('background-color:white; color: black')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('j', self)
        self.j.setGeometry(604,280,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('background-color:white; color: black')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('k', self)
        self.k.setGeometry(695,280,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('background-color:white; color: black')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('l', self)
        self.l.setGeometry(786,280,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('background-color:white; color: black')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,280,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('background-color:white; color: black')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,414,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('background-color:white; color: black')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('z', self)
        self.z.setGeometry(149,413,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('background-color:white; color: black')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('x', self)
        self.x.setGeometry(240,413,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('background-color:white; color: black')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('c', self)
        self.c.setGeometry(331,413,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('background-color:white; color: black')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('v', self)
        self.v.setGeometry(422,413,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('background-color:white; color: black')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('b', self)
        self.b.setGeometry(513,413,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('background-color:white; color: black')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('n', self)
        self.n.setGeometry(604,413,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('background-color:white; color: black')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('m', self)
        self.m.setGeometry(695,413,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('background-color:white; color: black')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,413,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('background-color:white; color: black')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,413,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('background-color:white; color: black')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,538,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('background-color:white; color: black')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,538,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('background-color:white; color: black')
        self.dash.clicked.connect(self.insert_text)
        
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,538,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('background-color:white; color: black')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,538,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('background-color:#4299ff; color: white')
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
        self.numerickeyboard1=numerickeyboard(self.entry.text())
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
        if(self.previouswindow=='e_user' ):
            self.labelshow="Enter User Name"
        elif(self.previouswindow=='e_employer' ):
            self.labelshow="Enter Employer ID"
        elif(self.previouswindow=='e_designation' ):
            self.labelshow="Enter Designation"
        elif(self.previouswindow=='e_contact' ):
            self.labelshow="Enter Contact"
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('DA_1217key1.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;')
        self.label.setGeometry(20,16,220,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,16,750,85)
        self.entry.setStyleSheet('background-color:white; color: black')
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setText(self.entrys)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('Q', self)
        q.setGeometry(59,149,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('background-color:white; color: black')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('W', self)
        self.w.setGeometry(149,149,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('background-color:white; color: black')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('E', self)
        self.e.setGeometry(240,149,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('background-color:white; color: black')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('R', self)
        self.r.setGeometry(331,149,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('background-color:white; color: black')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('T', self)
        self.t.setGeometry(422,149,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('background-color:white; color: black')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('Y', self)
        self.y.setGeometry(513,149,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('background-color:white; color: black')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('U', self)
        self.u.setGeometry(604,149,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('background-color:white; color: black')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('I', self)
        self.i.setGeometry(695,149,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('background-color:white; color: black')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('O', self)
        self.o.setGeometry(786,149,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('background-color:white; color: black')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('P', self)
        self.p.setGeometry(877,149,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('background-color:white; color: black')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('A', self)
        self.a.setGeometry(59,280,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('background-color:white; color: black')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('S', self)
        self.s.setGeometry(149,280,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('background-color:white; color: black')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('D', self)
        self.d.setGeometry(240,280,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('background-color:white; color: black')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('F', self)
        self.f.setGeometry(331,280,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('background-color:white; color: black')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('G', self)
        self.g.setGeometry(422,280,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('background-color:white; color: black')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('H', self)
        self.h.setGeometry(513,280,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('background-color:white; color: black')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('J', self)
        self.j.setGeometry(604,280,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('background-color:white; color: black')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('K', self)
        self.k.setGeometry(695,280,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('background-color:white; color: black')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('L', self)
        self.l.setGeometry(786,280,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('background-color:white; color: black')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,280,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('background-color:white; color: black')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,414,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('background-color:white; color: black')
        self.shift.clicked.connect(self.shift1)
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('Z', self)
        self.z.setGeometry(149,413,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('background-color:white; color: black')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('X', self)
        self.x.setGeometry(240,413,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('background-color:white; color: black')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('C', self)
        self.c.setGeometry(331,413,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('background-color:white; color: black')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('V', self)
        self.v.setGeometry(422,413,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('background-color:white; color: black')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('B', self)
        self.b.setGeometry(513,413,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('background-color:white; color: black')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('N', self)
        self.n.setGeometry(604,413,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('background-color:white; color: black')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('M', self)
        self.m.setGeometry(695,413,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('background-color:white; color: black')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,413,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('background-color:white; color: black')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,413,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('background-color:white; color: black')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,538,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('background-color:white; color: black')
        self.change.clicked.connect(self.change_numeric)
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,538,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('background-color:white; color: black')
        self.dash.clicked.connect(self.insert_text)
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,538,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('background-color:white; color: black')
        self.space.clicked.connect(self.space1)
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,538,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('background-color:#4299ff; color: white')
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
        self.numerickeyboard1=numerickeyboard(self.entry.text())
        self.numerickeyboard1.show()

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

       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint  | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('User Data',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,20,220,50)

        self.adduser = QLabel('User Name',self)
        self.adduser.setFont(QFont('Arial', 19))
        self.adduser.setStyleSheet('background-color:#f7f7ff; color: black')
        self.adduser.setGeometry(30,190,240,50)

        self.e_id = QLabel('Employer Id',self)
        self.e_id.setFont(QFont('Arial', 19))
        self.e_id.setStyleSheet('background-color:#f7f7ff; color: black')
        self.e_id.setGeometry(270,190,240,50)

        self.contact = QLabel('Contact',self)
        self.contact.setFont(QFont('Arial', 19))
        self.contact.setStyleSheet('background-color:#f7f7ff; color: black')
        self.contact.setGeometry(510,190,240,50)

        self.designation = QLabel('Designation',self)
        self.designation.setFont(QFont('Arial', 19))
        self.designation.setStyleSheet('background-color:#f7f7ff; color: black')
        self.designation.setGeometry(750,190,240,50)

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



        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        #self.dataView.setAlternatingRowColors(True)
        #self.dataView.setHeaderLabels(['','','',''])
        self.dataView.setHeaderHidden(True)
        #self.dataView.Header().setVisible(False)
        self.dataView.setColumnCount(5)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,20)
        self.dataView.setColumnWidth(1,250)
        self.dataView.setColumnWidth(2,250)
        self.dataView.setColumnWidth(3,250)
        self.dataView.setColumnWidth(4,250)
        self.dataView.setColumnWidth(5,0)
        self.dataView.setStyleSheet('background-color:white;color: black;')
        self.dataView.setFont(QFont('Arial', 21))
        #self.dataView.setIconSize(QSize(32,32))
        self.create_table()
        self.insert_data()
##        l=[['faisal111111111111111111','12345','',''],['faisal','','',''],['faisal','','','']]
##        for x in l:
##           QTreeWidgetItem(self.dataView,x) 

        self.dataView.setGeometry(10,240,1010,425)
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
    def call_b(self,data):
        print("asdss",data)
        if(data=="e_user"):
            user_data=self.e_user.text()
            self.close()
            self.destroy()
            gc.collect()
            self.nk=keyboard(user_data)
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
        self.e_user.speak.connect(partial(self.call_b,data='e_user'))
        #q.clicked.connect(partial(self.insert_text,data='q'))
        #self.e_user.speak.connect(self.call_b)
        #self.e_user.speak.emit("Hello everybody!")  
        #QtCore.QObject.connect(self.e_user, QtCore.SIGNAL('clicked()'), call_b) 
        #self.e_user.connect(self.call_b)

        self.e_employer = extQLineEdit(self,'e_employer')
        self.e_employer.setFont(QFont('Arial', 21))
        self.e_employer.setGeometry(469,215,492,53)
        self.e_employer.setStyleSheet('background-color:white; color: black')

        self.e_contact = extQLineEdit(self,'e_contact')
        self.e_contact.setFont(QFont('Arial', 21))
        self.e_contact.setGeometry(469,285,493,53)
        self.e_contact.setStyleSheet('background-color:white; color: black')

        self.e_designation = extQLineEdit(self,'e_designation')
        self.e_designation.setFont(QFont('Arial', 21))
        self.e_designation.setGeometry(469,355,492,53)
        self.e_designation.setStyleSheet('background-color:white; color: black')

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
            self.nk=keyboard(self.r,data,user_data)
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
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('userscreen.png'))
        self.bg.setGeometry(0,0,1024,668)

        self.label = QLabel('Edit Current User',self)
        self.label.setFont(QFont('Arial', 22))
        self.label.setStyleSheet('background-color:white; color: black')
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
        self.e_user.speak.connect(partial(self.call_b,data='e_user'))


        self.e_employer = extQLineEdit1(self)
        self.e_employer.setFont(QFont('Arial', 21))
        self.e_employer.setGeometry(469,215,492,53)
        self.e_employer.setStyleSheet('background-color:white; color: black')
        self.e_employer.speak.connect(partial(self.call_b,data='e_employer'))

        self.e_contact = extQLineEdit1(self)
        self.e_contact.setFont(QFont('Arial', 21))
        self.e_contact.setGeometry(469,285,493,53)
        self.e_contact.setStyleSheet('background-color:white; color: black')
        self.e_contact.speak.connect(partial(self.call_b,data='e_contact'))

        self.e_designation = extQLineEdit1(self)
        self.e_designation.setFont(QFont('Arial', 21))
        self.e_designation.setGeometry(469,355,492,53)
        self.e_designation.setStyleSheet('background-color:white; color: black')
        self.e_designation.speak.connect(partial(self.call_b,data='e_designation'))

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
class keydata():
    username=None
    employerid=''
    contact=''
    designation=''
    editdata=''
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gc.enable()
    w = Window()
    w.show()
    sys.exit(app.exec_())
