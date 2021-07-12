from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import pygame
import sys

class ImageWidget(QtWidgets.QWidget):
    def __init__(self,surface, setPixmap, parent=None):
        super(ImageWidget,self).__init__(parent)
        w=surface.get_width()
        h=surface.get_height()
        self.data=surface.get_buffer().raw
        self.image=QtGui.QImage(self.data,w,h,QtGui.QImage.Format_RGB32)
        pixmap = QPixmap.fromImage(self.image)
        self.setPixmap(pixmap)
    def paintEvent(self,event):
        qp=QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,surface,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setCentralWidget(ImageWidget(surface, setPixmap))



pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.set_mode((800, 600))
    s=pygame.Surface((640,480))
    s.fill((64,128,192,224))
    pygame.draw.circle(s,(255,255,255,255),(100,100),50)
    pygame.display.flip()
app=QtWidgets.QApplication(sys.argv)
w=MainWindow(s)
w.show()
app.exec_()