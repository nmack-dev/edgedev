import sys
import boto3
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setFixedWidth(1024)
        self.setFixedHeight(768)

        self.label = QLabel("Normal Status")
        self.label.setFont(QFont('Arial', 30))
        self.label.setStyleSheet('color: black')
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

device_name = os.uname().nodename
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '~/.aws/credentials'
s3_client = boto3.client('s3')
db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('fall_status')
response = table.scan()

alert_tags = []

for item in len(response):
    if (item['fall_status'] == 'True' and item['node_id'] not in alert_tags):
        alert_tags.append(item['node_id'])
    else:
        continue

if (alert_tags):
    alert_string = 'ALERT: Check Residents:'
    for tag in alert_tags:
        alert_string += ' ' + tag + ' '
    
    window.label = QLabel(alert_string)
    window.label.setStyleSheet('color: red')
    window.show()
