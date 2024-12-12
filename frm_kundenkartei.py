# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_kundenkartei.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_frm_kundenkartei(object):
    def setupUi(self, frm_kundenkartei):
        if not frm_kundenkartei.objectName():
            frm_kundenkartei.setObjectName(u"frm_kundenkartei")
        frm_kundenkartei.resize(881, 419)
        self.tb_kunden = QTableView(frm_kundenkartei)
        self.tb_kunden.setObjectName(u"tb_kunden")
        self.tb_kunden.setGeometry(QRect(0, 40, 881, 321))
        self.lb_kundenkartei = QLabel(frm_kundenkartei)
        self.lb_kundenkartei.setObjectName(u"lb_kundenkartei")
        self.lb_kundenkartei.setGeometry(QRect(0, 10, 881, 20))
        font = QFont()
        font.setPointSize(12)
        self.lb_kundenkartei.setFont(font)
        self.lb_kundenkartei.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bt_fertig = QPushButton(frm_kundenkartei)
        self.bt_fertig.setObjectName(u"bt_fertig")
        self.bt_fertig.setGeometry(QRect(790, 380, 75, 24))

        self.retranslateUi(frm_kundenkartei)

        QMetaObject.connectSlotsByName(frm_kundenkartei)
    # setupUi

    def retranslateUi(self, frm_kundenkartei):
        frm_kundenkartei.setWindowTitle(QCoreApplication.translate("frm_kundenkartei", u"Form", None))
        self.lb_kundenkartei.setText(QCoreApplication.translate("frm_kundenkartei", u"Kundenkartei verwalten", None))
        self.bt_fertig.setText(QCoreApplication.translate("frm_kundenkartei", u"Fertig", None))
    # retranslateUi

