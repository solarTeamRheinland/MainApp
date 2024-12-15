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
    QPushButton, QSizePolicy, QStatusBar, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QGridLayout, QHBoxLayout, QStyle)

import re

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(800, 600)

        # Central widget
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")

        # Main layout
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(15)

        # Logo
        self.lb_logo = QLabel(self.centralwidget)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setPixmap(QPixmap("logo.jpg"))
        self.lb_logo.setScaledContents(True)
        self.lb_logo.setMaximumSize(QSize(200, 60))

        self.main_layout.addWidget(self.lb_logo, alignment=Qt.AlignLeft)

        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)  # Remove unnecessary margins
        self.header_layout.setSpacing(5)  # Minimal spacing between label and button

        self.lb_kunden = QLabel(self.centralwidget)
        self.lb_kunden.setObjectName(u"lb_kunden")
        self.lb_kunden.setText("Kunden")
        self.lb_kunden.setFont(QFont("Arial", 12, QFont.Bold))

        self.bt_refresh = QPushButton(self.centralwidget)
        self.bt_refresh.setObjectName(u"bt_refresh")
        self.bt_refresh.setText("Aktualisieren")
        refresh_icon = self.style().standardIcon(QStyle.SP_BrowserReload)
        self.bt_refresh.setIcon(QIcon(refresh_icon))
        self.bt_refresh.setFont(QFont("Arial", 10, QFont.Bold))
        self.bt_refresh.setFixedWidth(120)  # Fix the button width
        self.bt_refresh.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Prevent it from stretching

        # Add label and button to the horizontal layout
        self.header_layout.addWidget(self.lb_kunden)
        self.header_layout.addWidget(self.bt_refresh)

        # Align the layout to the left
        self.header_layout.addStretch()  # Add a stretch to ensure the button stays close to the label

        # Add the horizontal layout to the main layout
        self.main_layout.addLayout(self.header_layout)

        self.table_widget = QTableWidget(self.centralwidget)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setColumnCount(3)  # Example column count
        self.table_widget.setHorizontalHeaderLabels(["ID", "Name", "Adresse"])
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setSelectionBehavior(QTableWidget.SelectRows)

        # Adding some placeholder data to the table
        for i in range(5):  # Example rows
            self.table_widget.insertRow(i)
            self.table_widget.setItem(i, 0, QTableWidgetItem(f"Kunde {i+1}"))
            self.table_widget.setItem(i, 1, QTableWidgetItem("Max Mustermann"))
            self.table_widget.setItem(i, 2, QTableWidgetItem("Musterstr. 1"))

        self.main_layout.addWidget(self.table_widget)

        # Customer Details Section
        self.lb_customer_details = QLabel(self.centralwidget)
        self.lb_customer_details.setText("Kundendaten")
        self.lb_customer_details.setFont(QFont("Arial", 10, QFont.Bold))

        self.main_layout.addWidget(self.lb_customer_details)

        # Create a grid layout for customer details
        self.grid_layout = QGridLayout()
        self.grid_layout.setHorizontalSpacing(20)  # Add spacing between left and right sections

        self.customer_fields = {}
        self.liste_daten_fields = {}

        self.customer_field_definitions = [
            ("Kundennr:", "edit_kundennr"),
            ("Name:", "edit_name"),
            ("Vorname:", "edit_vorname"),
            ("Strasse:", "edit_strasse"),
            ("Hausnummer:", "edit_hausnr"),
            ("PLZ:", "edit_plz"),
            ("Ort:", "edit_ort"),
        ]

        for row, (label_text, object_name) in enumerate(self.customer_field_definitions):
            self.customer_fields[object_name] = self.create_field(self.grid_layout, label_text, object_name, row, 0)

        # Create liste_daten fields (right)
        self.liste_daten_field_definitions = [
            ("Wechselrichter Hersteller:", "edit_wr_hersteller"),
            ("Wechselrichter Modell:", "edit_wr_modell"),
            ("Anzahl Wechselrichter:", "edit_wr_anzahl"),
            ("Scheinleistung (kVA):", "edit_wr_scheinleistung"),
            ("Wirkleistung (kW):", "edit_wr_wirkleistung"),
            ("PV-Leistung (kWp):", "edit_pv_leistung"),
        ]

        for row, (label_text, object_name) in enumerate(self.liste_daten_field_definitions):
            self.liste_daten_fields[object_name] = self.create_field(self.grid_layout, label_text, object_name, row, 2)

        # Add grid layout to the main layout
        self.main_layout.addLayout(self.grid_layout)

        # Store lists for further referencing
        self.liste_kunde = list(self.customer_fields.values())
        self.liste_daten = list(self.liste_daten_fields.values())

        # Add PDF Button
        self.bt_pdf_erstellen = QPushButton(self.centralwidget)
        self.bt_pdf_erstellen.setObjectName(u"bt_pdf_erstellen")
        self.bt_pdf_erstellen.setText("PDF Erstellen")
        self.bt_pdf_erstellen.setFont(QFont("Arial", 10, QFont.Bold))
        self.main_layout.addWidget(self.bt_pdf_erstellen, alignment=Qt.AlignRight)

        frm_main.setCentralWidget(self.centralwidget)

        # Menu and Status Bar
        self.menubar = QMenuBar(frm_main)
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setTitle("Datei")
        self.menuStammdaten = QMenu(self.menubar)
        self.menuStammdaten.setTitle("Stammdaten")
        frm_main.setMenuBar(self.menubar)

        self.actionBeenden = QAction("Beenden", frm_main)
        self.actionKunden_verwalten = QAction("Kunden verwalten", frm_main)
        self.actionTechnische_Daten_verwalten = QAction("Technische Daten verwalten", frm_main)

        self.menuDatei.addAction(self.actionBeenden)
        self.menuStammdaten.addAction(self.actionKunden_verwalten)
        self.menuStammdaten.addAction(self.actionTechnische_Daten_verwalten)

        self.menubar.addMenu(self.menuDatei)
        self.menubar.addMenu(self.menuStammdaten)

        self.statusbar = QStatusBar(frm_main)
        frm_main.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(frm_main)

    def create_field(self, layout, label_text, object_name, row, column):
        """Helper function to create and add a labeled field to the layout."""
        label = QLabel(self.centralwidget)
        label.setText(label_text)
        label.setFont(QFont("Arial", 10))
        layout.addWidget(label, row, column, alignment=Qt.AlignRight)

        line_edit = QLineEdit(self.centralwidget)
        line_edit.setObjectName(object_name)
        line_edit.setFixedWidth(200)
        layout.addWidget(line_edit, row, column + 1)

        return line_edit



    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.actionBeenden.setText(QCoreApplication.translate("frm_main", u"Beenden", None))
        self.actionKunden_verwalten.setText(QCoreApplication.translate("frm_main", u"Kunden verwalten", None))
        self.actionTechnische_Daten_verwalten.setText(QCoreApplication.translate("frm_main", u"Technische Daten verwalten", None))
        self.bt_pdf_erstellen.setText(QCoreApplication.translate("frm_main", u"PDF erstellen", None))

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
