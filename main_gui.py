import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_widget
import sys
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtGui import *
import os


class myWindow(QtWidgets.QMainWindow, Ui_widget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # QtCreater 设计界面.ui->.py pyuic5 -o mainwindow.py mainwindow.ui
        self.setupUi(self)
        self.directory_img = 'img'
        self.directory_video = 'video'
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率

        self.cap = cv2.VideoCapture()

        self.colors = [self.color_1, self.color_2,
                       self.color_3, self.color_4, self.color_5]

        self.nocolors = [self.nocolor_1, self.nocolor_2,
                         self.nocolor_3, self.nocolor_4, self.nocolor_5]
        self.color_labels = [self.color_txt_1, self.color_txt_2,
                             self.color_txt_3, self.color_txt_4, self.color_txt_5]

        self.nocolor_labels = [self.nocolor_txt_1, self.nocolor_txt_2,
                               self.nocolor_txt_3, self.nocolor_txt_4, self.nocolor_txt_5]
        self.slot_init()

    def slot_init(self):
        self.pushButton_video.clicked.connect(self.open_vedio)
        self.timer_camera.timeout.connect(
            self.OpenFrame)  # 定时器结束，则调用show_camera()
        self.handle_buttons()
        self.pushButton_boxplot_force.clicked.connect(
            lambda: self.show_one_img('force boxplot'))
        self.pushButton_boxplot_time.clicked.connect(
            lambda: self.show_one_img('time boxplot'))
        self.pushButton_red.clicked.connect(
            lambda: self.show_one_img('red voxel-removed'))

        self.pushButton_quit.clicked.connect(
            QtCore.QCoreApplication.instance().quit)
        self.pushButton_color_1.clicked.connect(
            lambda: self.openImage(1, color=1))
        self.pushButton_color_2.clicked.connect(
            lambda: self.openImage(2, color=1))
        self.pushButton_color_3.clicked.connect(
            lambda: self.openImage(3, color=1))
        self.pushButton_color_4.clicked.connect(
            lambda: self.openImage(4, color=1))
        self.pushButton_color_5.clicked.connect(
            lambda: self.openImage(5, color=1))
        self.pushButton_color_6.clicked.connect(
            lambda: self.openImage(6, color=1))
        self.pushButton_color_7.clicked.connect(
            lambda: self.openImage(7, color=1))
        self.pushButton_color_8.clicked.connect(
            lambda: self.openImage(8, color=1))
        self.pushButton_color_9.clicked.connect(
            lambda: self.openImage(9, color=1))
        self.pushButton_color_10.clicked.connect(
            lambda: self.openImage(10, color=1))

        self.pushButton_nocolor_1.clicked.connect(
            lambda: self.openImage(1, color=0))
        self.pushButton_nocolor_2.clicked.connect(
            lambda: self.openImage(2, color=0))
        self.pushButton_nocolor_3.clicked.connect(
            lambda: self.openImage(3, color=0))
        self.pushButton_nocolor_4.clicked.connect(
            lambda: self.openImage(4, color=0))
        self.pushButton_nocolor_5.clicked.connect(
            lambda: self.openImage(5, color=0))
        self.pushButton_nocolor_6.clicked.connect(
            lambda: self.openImage(6, color=0))
        self.pushButton_nocolor_7.clicked.connect(
            lambda: self.openImage(7, color=0))
        self.pushButton_nocolor_8.clicked.connect(
            lambda: self.openImage(8, color=0))
        self.pushButton_nocolor_9.clicked.connect(
            lambda: self.openImage(9, color=0))
        self.pushButton_nocolor_10.clicked.connect(
            lambda: self.openImage(10, color=0))

    def all_label_freash(self):
        self.video.clear()

        for i in range(5):
            self.nocolors[i].clear()
            self.colors[i].clear()

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            QtWidgets.QMessageBox.warning(
                self, 'message', "Load video successd!")
            self.timer_camera.start(30)  # 定时器开始计时,每30ms从摄像头读取一帧图像
            self.pushButton_play.setText('Display')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.video.clear()
            self.pushButton_play.setText('Play')

    def saveImage(self):  # 保存图片到本地
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.label_image.winId())
        fd, type = QFileDialog.getSaveFileName(
            self.groupBox, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        pix.save(fd)

    def openDirectory(self):  # 打开文件夹（目录）
        fd = QFileDialog.getExistingDirectory(self.groupBox, "选择文件夹", "")
        # self.label_directoryPath.setText(fd)
        self.detect_img(fd)

    # this function is for read image,the input is directory name

    def read_directory(self, button_num, color):
        array_of_img_path = []  # this if for store all of the image data
        # this loop is for read each image in this foder,directory_name is the foder name with images.
        if color == 1:
            dir_path = r"./"+self.directory_img+f'/part{button_num}/color'
            for filename in os.listdir(dir_path):
                array_of_img_path.append(dir_path + "/" + filename)

        else:
            dir_path = r"./"+self.directory_img+f'/part{button_num}/noncolor'
            for filename in os.listdir(dir_path):
                array_of_img_path.append(dir_path + "/" + filename)
        print(array_of_img_path)
        return array_of_img_path

    def openImage(self, button_num, color):  # 选择本地图片上传
        imgName = self.read_directory(button_num, color)
        if len(imgName) != 5:
            QMessageBox.warning(self, 'warning', 'The image num is not right！')
        else:
            QMessageBox.warning(self, 'message', 'Load image successd！')
            self.show_color_img(color, imgName)

    def show_one_img(self, str_num):  # 选择本地图片上传
        self.all_label_freash()
        array_of_img_path = []
        dir_path = r"./"+self.directory_img+f'/{str_num}'
        for filename in os.listdir(dir_path):
            array_of_img_path.append(dir_path + "/" + filename)
        imgName = array_of_img_path[0]
        QMessageBox.warning(self, 'message', 'Load image successd！')
        png = QtGui.QPixmap(imgName).scaled(
            self.video.width(), self.video.height())
        self.video.setPixmap(png)

    def select_label_show(self, color, i, img_path):
        self.video.clear()
        if color == 1:
            png = QtGui.QPixmap(img_path).scaled(
                self.colors[i].width(), self.colors[i].height())
            self.colors[i].setPixmap(png)
            self.color_labels[0].setText(f"P0-L{1}")
            self.color_labels[1].setText(f"P0-L{3}")
            self.color_labels[2].setText(f"P2-L{2}")
            self.color_labels[3].setText(f"P4-L{2}")
            self.color_labels[4].setText(f"P7-L{1}")

        else:
            png = QtGui.QPixmap(img_path).scaled(
                self.nocolors[i].width(), self.nocolors[i].height())
            self.nocolors[i].setPixmap(png)
            self.nocolor_labels[0].setText(f"P1-L{1}")
            self.nocolor_labels[1].setText(f"P1-L{3}")
            self.nocolor_labels[2].setText(f"P2-L{1}")
            self.nocolor_labels[3].setText(f"P4-L{1}")
            self.nocolor_labels[4].setText(f"P7-L{3}")

    def show_color_img(self, color, img_list):
        if color == 1:
            for i in range(len(img_list)):
                # image = np.array(Image.open(img).convert('RGB'))
                self.select_label_show(color, i, img_list[i])
        else:
            for i in range(len(img_list)):
                # image = np.array(Image.open(img).convert('RGB'))
                self.select_label_show(color, i, img_list[i])

    # 所有Button的消息与槽的通信

    def handle_buttons(self):
        self.pushButton_play.clicked.connect(self.button_open_camera_clicked)
        self.pushButton_record.clicked.connect(self.Btn_Stop)

    def Btn_Start(self):
        # 定时器开启，每隔一段时间，读取一帧
        # self.open_vedio()
        self.timer_camera.start(1000)
        self.timer_camera.timeout.connect(self.OpenFrame)
        # self.result_label.setText("正在播放")

    def Btn_Stop(self):
        # self.cap.release()
        self.timer_camera.stop()
        # self.result_label.setText("停止播放，按下start再次播放")

    def open_vedio(self):
        array_of_img_path = []
        dir_path = r"./"+self.directory_video
        for filename in os.listdir(dir_path):
            array_of_img_path.append(dir_path + "/" + filename)
        self.cap = cv2.VideoCapture(array_of_img_path[0])

    def OpenFrame(self):
        ret, show_img = self.cap.read()
        if ret:
            if len(show_img.shape) == 3:
                image = cv2.cvtColor(show_img, cv2.COLOR_BGR2RGB)
                vedio_img = QtGui.QImage(
                    image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
            show_img = cv2.cvtColor(show_img, cv2.COLOR_BGR2RGB)
            h, w, ch = show_img.shape
            bytesPerLine = ch * w
            show_roi = QtGui.QImage(
                show_img.data, show_img.shape[1], show_img.shape[0], bytesPerLine, QtGui.QImage.Format_RGB888)
            self.video.setPixmap(QtGui.QPixmap.fromImage(show_roi))
            # self.video.setPixmap(QPixmap(vedio_img))
            self.video.setScaledContents(True)  # 自适应窗口
        else:
            self.cap.release()
            self.video.clear()
            self.timer_camera.stop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec())
