import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.uic import *
import sys
import os
import mysql.connector


#Loginwindow
MainUI,_=loadUiType('login.ui')
class omar(QMainWindow , MainUI) :
    def __init__(self,parent=None):
        super(omar,self).__init__(parent)
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.pushButton_20.clicked.connect(self.qac)
        self.dbconnect()

###########################################################################################
#Data base Login Connect
    def dbconnect(self):
        self.db=mysql.connector.connect(user='root', password='Om19ha17ar&',
                         host="localhost", db='db')
        self.cur=self.db.cursor()                 
        print('connc')    
############################################################################################

#incorrect password
    def qac(self):
        msg = QMessageBox()
        em=self.lineEdit_21.text()
        en=self.lineEdit_19.text()
   

        self.cur.execute("""SELECT * FROM users """)
        data = self.cur.fetchall()
        print(data)
        for row in data:
            if row[1]== em and row[2]== en:
                self.hide()
                crc=Main()
                crc.show()
            else:
                msg.setText('Incorrect Password')
                msg.exec_()        
        


            app.exec_()
##############################################################################################        
#main Window info        
MainUI,_=loadUiType('mainwindow.ui')
class Main(QMainWindow , MainUI) :
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.PU()
        self.UI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.nu)
        self.timer.timeout.connect(self.nu1)
        self.timer.timeout.connect(self.nu2)
        self.dbconnect()

        


################################################################################################

#tab bar hide
    def UI(self):
        self.tabWidget.tabBar().setVisible(False)






#################################################################################################

#buttons 
    def PU(self):
        self.pushButton.clicked.connect(self.homep)
        self.pushButton_2.clicked.connect(self.insertp)
        self.pushButton_3.clicked.connect(self.reportp)
        self.pushButton_4.clicked.connect(self.settingp)
        self.pushButton_5.clicked.connect(self.profilep)
        self.pushButton_22.clicked.connect(self.cap)
        self.pushButton_7.clicked.connect(self.cap1)
        self.pushButton_10.clicked.connect(self.cap2)
        self.pushButton_19.clicked.connect(self.adduser)


###################################################################################################
#connect to data base    

    def dbconnect(self):
        self.db=mysql.connector.connect(user='root', password='Om19ha17ar&',
                         host="localhost", db='db')
        self.cur=self.db.cursor()

###################################################################################################


#Home page info
    def homep(self):
        self.tabWidget_2.setCurrentIndex(0)

        self.tabWidget.setCurrentIndex(0)


##################################################################################################

#insert page info
    def insertp(self):
        self.tabWidget_3.setCurrentIndex(0)

        self.tabWidget.setCurrentIndex(1)

##################################################################################################     

#report Info
    def reportp(self):
        self.tabWidget.setCurrentIndex(2)

###################################################################################################


    def settingp(self):
        self.tabWidget.setCurrentIndex(3)


##################################################################################################



    def profilep(self):
        self.tabWidget.setCurrentIndex(4)
##################################################################################################
#Take Picture 
    def nu(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_31.setPixmap(QPixmap.fromImage(qImg))

##################################################################################################


    def cap(self):

        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text

        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text



##########################################################################

    def nu1(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_12.setPixmap(QPixmap.fromImage(qImg))


##############################################################################################


    def cap1(self):

        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text

        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
##############################################################################
    def nu2(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_18.setPixmap(QPixmap.fromImage(qImg))

###################################################################################






    def cap2(self):

        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text

        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text

###############################################################################
    def adduser(self):
        username=self.lineEdit_18.text()
        upassowrd=self.lineEdit_17.text()
        self.cur.execute( ''' INSERT INTO users(name , password)
        VALUES(%s,%s)
            ''',(username,upassowrd))
        self.db.commit()





def main():
    app=QApplication(sys.argv)
    window=omar()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()































