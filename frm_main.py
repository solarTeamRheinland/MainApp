# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget, QTableWidget, QTableWidgetItem)

import re

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(778, 529)
        self.actionBeenden = QAction(frm_main)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.actionKunden_verwalten = QAction(frm_main)
        self.actionKunden_verwalten.setObjectName(u"actionKunden_verwalten")
        self.actionTechnische_Daten_verwalten = QAction(frm_main)
        self.actionTechnische_Daten_verwalten.setObjectName(u"actionTechnische_Daten_verwalten")
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_pdf_erstellen = QPushButton(self.centralwidget)
        self.bt_pdf_erstellen.setObjectName(u"bt_pdf_erstellen")
        self.bt_pdf_erstellen.setGeometry(QRect(660, 440, 100, 30))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.bt_pdf_erstellen.setFont(font)
        self.dp_kunden = QComboBox(self.centralwidget)
        self.dp_kunden.addItem("")
        self.dp_kunden.addItem("")
        self.dp_kunden.addItem("")
        self.dp_kunden.setObjectName(u"dp_kunden")
        self.dp_kunden.setGeometry(QRect(30, 155, 150, 30))
        self.lb_kunden = QLabel(self.centralwidget)
        self.lb_kunden.setObjectName(u"lb_kunden")
        self.lb_kunden.setGeometry(QRect(30, 130, 111, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.lb_kunden.setFont(font1)
        self.dp_prozess = QComboBox(self.centralwidget)
        self.dp_prozess.addItem("")
        self.dp_prozess.addItem("")
        self.dp_prozess.addItem("")
        self.dp_prozess.addItem("")
        self.dp_prozess.setObjectName(u"dp_prozess")
        self.dp_prozess.setGeometry(QRect(280, 155, 150, 30))
        self.lb_prozess = QLabel(self.centralwidget)
        self.lb_prozess.setObjectName(u"lb_prozess")
        self.lb_prozess.setGeometry(QRect(280, 130, 111, 16))
        self.lb_prozess.setFont(font1)
        self.lb_name = QLabel(self.centralwidget)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setGeometry(QRect(30, 290, 49, 16))
        self.lb_strasse = QLabel(self.centralwidget)
        self.lb_strasse.setObjectName(u"lb_strasse")
        self.lb_strasse.setGeometry(QRect(30, 350, 49, 16))

        self.table_widget = QTableWidget(self.centralwidget)
        self.table_widget.setGeometry(50, 10, 670, 80)  # Set geometry for visibility
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setSelectionBehavior(QTableWidget.SelectRows)


        self.line_oben = QFrame(self.centralwidget)
        self.line_oben.setObjectName(u"line_oben")
        self.line_oben.setGeometry(QRect(0, 100, 780, 20))
        self.line_oben.setFrameShape(QFrame.Shape.HLine)
        self.line_oben.setFrameShadow(QFrame.Shadow.Sunken)
        self.lb_ort = QLabel(self.centralwidget)
        self.lb_ort.setObjectName(u"lb_ort")
        self.lb_ort.setGeometry(QRect(30, 440, 49, 16))
        self.lb_plz = QLabel(self.centralwidget)
        self.lb_plz.setObjectName(u"lb_plz")
        self.lb_plz.setGeometry(QRect(30, 410, 49, 16))
        self.lb_hausnr = QLabel(self.centralwidget)
        self.lb_hausnr.setObjectName(u"lb_hausnr")
        self.lb_hausnr.setGeometry(QRect(30, 380, 91, 16))
        self.lb_vorname = QLabel(self.centralwidget)
        self.lb_vorname.setObjectName(u"lb_vorname")
        self.lb_vorname.setGeometry(QRect(30, 320, 71, 16))
        self.lb_kundennr = QLabel(self.centralwidget)
        self.lb_kundennr.setObjectName(u"lb_kundennr")
        self.lb_kundennr.setGeometry(QRect(30, 260, 101, 16))
        self.lb_wr_hersteller = QLabel(self.centralwidget)
        self.lb_wr_hersteller.setObjectName(u"lb_wr_hersteller")
        self.lb_wr_hersteller.setGeometry(QRect(300, 260, 141, 16))
        self.lb_wr_scheinleistung = QLabel(self.centralwidget)
        self.lb_wr_scheinleistung.setObjectName(u"lb_wr_scheinleistung")
        self.lb_wr_scheinleistung.setGeometry(QRect(300, 350, 171, 16))
        self.lb_wr_anzahl = QLabel(self.centralwidget)
        self.lb_wr_anzahl.setObjectName(u"lb_wr_anzahl")
        self.lb_wr_anzahl.setGeometry(QRect(300, 320, 131, 16))
        self.lb_wr_wirkleistung = QLabel(self.centralwidget)
        self.lb_wr_wirkleistung.setObjectName(u"lb_wr_wirkleistung")
        self.lb_wr_wirkleistung.setGeometry(QRect(300, 380, 171, 16))
        self.lb_wr_modell = QLabel(self.centralwidget)
        self.lb_wr_modell.setObjectName(u"lb_wr_modell")
        self.lb_wr_modell.setGeometry(QRect(300, 290, 131, 16))
        self.lb_pv_leistung = QLabel(self.centralwidget)
        self.lb_pv_leistung.setObjectName(u"lb_pv_leistung")
        self.lb_pv_leistung.setGeometry(QRect(300, 410, 131, 16))
        self.edit_kundennr = QLineEdit(self.centralwidget)
        self.edit_kundennr.setObjectName(u"edit_kundennr")
        self.edit_kundennr.setGeometry(QRect(130, 260, 130, 16))
        self.edit_name = QLineEdit(self.centralwidget)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setGeometry(QRect(130, 290, 130, 16))
        self.edit_vorname = QLineEdit(self.centralwidget)
        self.edit_vorname.setObjectName(u"edit_vorname")
        self.edit_vorname.setGeometry(QRect(130, 320, 130, 16))
        self.edit_strasse = QLineEdit(self.centralwidget)
        self.edit_strasse.setObjectName(u"edit_strasse")
        self.edit_strasse.setGeometry(QRect(130, 350, 130, 16))
        self.edit_hausnr = QLineEdit(self.centralwidget)
        self.edit_hausnr.setObjectName(u"edit_hausnr")
        self.edit_hausnr.setGeometry(QRect(130, 380, 130, 16))
        self.edit_plz = QLineEdit(self.centralwidget)
        self.edit_plz.setObjectName(u"edit_plz")
        self.edit_plz.setGeometry(QRect(130, 410, 130, 16))
        self.edit_ort = QLineEdit(self.centralwidget)
        self.edit_ort.setObjectName(u"edit_ort")
        self.edit_ort.setGeometry(QRect(130, 440, 130, 16))
        self.edit_wr_hersteller = QLineEdit(self.centralwidget)
        self.edit_wr_hersteller.setObjectName(u"edit_wr_hersteller")
        self.edit_wr_hersteller.setGeometry(QRect(480, 260, 130, 16))
        self.edit_wr_modell = QLineEdit(self.centralwidget)
        self.edit_wr_modell.setObjectName(u"edit_wr_modell")
        self.edit_wr_modell.setGeometry(QRect(480, 290, 130, 16))
        self.edit_wr_anzahl = QLineEdit(self.centralwidget)
        self.edit_wr_anzahl.setObjectName(u"edit_wr_anzahl")
        self.edit_wr_anzahl.setGeometry(QRect(480, 320, 130, 16))
        self.edit_wr_scheinleistung = QLineEdit(self.centralwidget)
        self.edit_wr_scheinleistung.setObjectName(u"edit_wr_scheinleistung")
        self.edit_wr_scheinleistung.setGeometry(QRect(480, 350, 130, 16))
        self.edit_wr_wirkleistung = QLineEdit(self.centralwidget)
        self.edit_wr_wirkleistung.setObjectName(u"edit_wr_wirkleistung")
        self.edit_wr_wirkleistung.setGeometry(QRect(480, 380, 130, 16))
        self.edit_pv_leistung = QLineEdit(self.centralwidget)
        self.edit_pv_leistung.setObjectName(u"edit_pv_leistung")
        self.edit_pv_leistung.setGeometry(QRect(480, 410, 130, 16))
        self.line_unten = QFrame(self.centralwidget)
        self.line_unten.setObjectName(u"line_unten")
        self.line_unten.setGeometry(QRect(-10, 200, 791, 20))
        self.line_unten.setMaximumSize(QSize(10000000, 16777215))
        self.line_unten.setFrameShape(QFrame.Shape.HLine)
        self.line_unten.setFrameShadow(QFrame.Shadow.Sunken)
        self.lb_logo = QLabel(self.centralwidget)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setEnabled(True)
        self.lb_logo.setGeometry(QRect(30, 20, 160, 60))
        self.lb_logo.setMaximumSize(QSize(100000, 1000000))
        self.lb_logo.setPixmap(QPixmap(u"../../logo_neu-removebg-preview.png"))
        self.lb_logo.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 230, 91, 16))
        font2 = QFont()
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 230, 131, 16))
        self.label_2.setFont(font2)
        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 778, 22))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuStammdaten = QMenu(self.menubar)
        self.menuStammdaten.setObjectName(u"menuStammdaten")
        frm_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main)
        self.statusbar.setObjectName(u"statusbar")
        frm_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuStammdaten.menuAction())
        self.menuDatei.addAction(self.actionBeenden)
        self.menuStammdaten.addAction(self.actionKunden_verwalten)
        self.menuStammdaten.addAction(self.actionTechnische_Daten_verwalten)

        self.retranslateUi(frm_main)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.actionBeenden.setText(QCoreApplication.translate("frm_main", u"Beenden", None))
        self.actionKunden_verwalten.setText(QCoreApplication.translate("frm_main", u"Kunden verwalten", None))
        self.actionTechnische_Daten_verwalten.setText(QCoreApplication.translate("frm_main", u"Technische Daten verwalten", None))
        self.bt_pdf_erstellen.setText(QCoreApplication.translate("frm_main", u"PDF erstellen", None))
        self.dp_kunden.setItemText(0, QCoreApplication.translate("frm_main", u"Siegbert Sonnenschein", None))
        self.dp_kunden.setItemText(1, QCoreApplication.translate("frm_main", u"Lisa Licht", None))
        self.dp_kunden.setItemText(2, QCoreApplication.translate("frm_main", u"Neu", None))

        self.lb_kunden.setText(QCoreApplication.translate("frm_main", u"Kunden ausw\u00e4hlen:", None))
        self.dp_prozess.setItemText(0, QCoreApplication.translate("frm_main", u"Netzanmeldeformular", None))
        self.dp_prozess.setItemText(1, QCoreApplication.translate("frm_main", u"VOT-Protokoll", None))
        self.dp_prozess.setItemText(2, QCoreApplication.translate("frm_main", u"DC-Inbetriebnahme-Protokoll", None))
        self.dp_prozess.setItemText(3, QCoreApplication.translate("frm_main", u"AC-Inbetriebnahme-Protokoll", None))

        self.lb_prozess.setText(QCoreApplication.translate("frm_main", u"Prozess ausw\u00e4hlen:", None))
        self.lb_name.setText(QCoreApplication.translate("frm_main", u"Name:", None))
        self.lb_strasse.setText(QCoreApplication.translate("frm_main", u"Stra\u00dfe:", None))
        self.lb_ort.setText(QCoreApplication.translate("frm_main", u"Ort:", None))
        self.lb_plz.setText(QCoreApplication.translate("frm_main", u"PLZ:", None))
        self.lb_hausnr.setText(QCoreApplication.translate("frm_main", u"Hausnummer:", None))
        self.lb_vorname.setText(QCoreApplication.translate("frm_main", u"Vorname:", None))
        self.lb_kundennr.setText(QCoreApplication.translate("frm_main", u"Kundennummer:", None))
        self.lb_wr_hersteller.setText(QCoreApplication.translate("frm_main", u"Hersteller Wechselrichter:", None))
        self.lb_wr_scheinleistung.setText(QCoreApplication.translate("frm_main", u"Scheinleistung Wechselrichter:", None))
        self.lb_wr_anzahl.setText(QCoreApplication.translate("frm_main", u"Anzahl Wechselrichter:", None))
        self.lb_wr_wirkleistung.setText(QCoreApplication.translate("frm_main", u"Wirkleistung Wechselrichter:", None))
        self.lb_wr_modell.setText(QCoreApplication.translate("frm_main", u"Modell Wechselrichter:", None))
        self.lb_pv_leistung.setText(QCoreApplication.translate("frm_main", u"Leistung PV-Modul:", None))
        self.lb_logo.setText("")
        self.label.setText(QCoreApplication.translate("frm_main", u"Kundendaten:", None))
        self.label_2.setText(QCoreApplication.translate("frm_main", u"Technische Daten:", None))
        self.menuDatei.setTitle(QCoreApplication.translate("frm_main", u"Datei", None))
        self.menuStammdaten.setTitle(QCoreApplication.translate("frm_main", u"Stammdaten", None))
    # retranslateUi

    def to_normal_case(self, text):
        """
        Converts camelCase or snake_case to Normal Case.
        """
        # Convert camelCase to spaces
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
        # Replace underscores with spaces
        text = text.replace("_", " ")
        # Capitalize the first letter of each word
        return text.title()

    def populate_table_with_data(self, data_list):
        """
        Populates the table with a list of dictionaries.
        :param data_list: List of dictionaries with keys as column names and values as row data.
        """
        if not data_list:
            print("No data to display")
            return

        # Extract column names from the first dictionary
        column_names = [self.to_normal_case(col) for col in data_list[0].keys()]

        # Set up the table dimensions
        self.table_widget.setColumnCount(len(column_names))
        self.table_widget.setHorizontalHeaderLabels(column_names)
        self.table_widget.setRowCount(len(data_list))

        # Populate the table
        for row_index, row_data in enumerate(data_list):
            for col_index, (key, value) in enumerate(row_data.items()):
                self.table_widget.setItem(row_index, col_index, QTableWidgetItem(str(value)))
