from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QLabel, QMainWindow, QWidget, QPushButton, QFileDialog, QHBoxLayout

import sys
sys.path.append("./")

from utils.feature import Feature
from utils.scenedet import SceneDetector
from utils.selector import Summarizer

class AppWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Summarize - Video Summarizer'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout = QHBoxLayout(self)

        self.button = QPushButton('Generate Summary', self)
        self.button.setToolTip('Click to generate summary')
        self.button.clicked.connect(self.on_click)

        self.label = QLabel('Browse File', self)
        
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.show()

    def on_click(self):
        options = QFileDialog.Options()
        print(options)
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:

            self.label.setText("Processing...")

            f = Feature(fileName, verbose=True)
            summarizer = Summarizer(duration=120)
            summarizer.set_feature_extractor(f)
            summarizer.summarize()

            self.label.setText("Sucess!")



if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = AppWindow()
    # window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)