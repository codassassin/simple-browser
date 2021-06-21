import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://mad4souvik.ml'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://mad4souvik.ml'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        common_sites = ['google', 'facebook', 'twitter', 'duckduckgo']
        if url in common_sites:
            url = 'https://' + url + '.com'
        elif url not in common_sites and not ('http:' in url or 'https:' in url) and not ('.' in url):
            url = 'https://duckduckgo.com/?q=' + url
        elif 'http:' in url:
            url_l = url.split(':')
            url = 'https:' + url_l[1]
        # elif 'ftp:' or 'smtp:' in url:
        #     url = url
        elif 'http:' or 'https:' not in url:
            url = 'https://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('codassassin')
window = MainWindow()
app.exec_()

