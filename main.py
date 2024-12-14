from pypdf import PdfReader, PdfWriter
from spire.pdf import *
import pyodbc

#aus Ordner GUI (im selben Verzeichnis wie main.py) Klasse UI_frm_main aus py datei b.py (GUI) importieren
from frm_main import Ui_frm_main
from frm_kundenkartei import Ui_frm_kundenkartei


#qapplication = Klasse die Anwendung steuer, QMainwindow = Hauptfenster
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql

#designer öffnen: Terminal: pyside6-designer
#wenn GUI Datei im Designer erstellt und gespeichert wurde, kann diese in eine Py-Datei konvertiert werden:
#in Terminal: pyside6-uic frm_main.ui -o frm_main.py

parameter = ["name",
             "strasse",
             "ort",
             "herstellerwr",
             "typwr",
             "anzahlwr",
             "scheinleistungwr",
             "wirkleistungwr",
             "leistungmodule",]

kunde_neu = ["Neu",
           "",
           "",
           "",
           "SMA",
           "Sunny Tripower Core1",
           "1",
           "50",
           "50",
           "54,8"]

kunde_1 = ["41163",
            "Sonnenschein",
           "Siegbert",
           "Sonnenallee",
           "4",
           "12345",
           "Sonnenhausen",
           "SMA",
           "Sunny Tripower X12",
           "1",
           "12",
           "12",
           "13,4"]

kunde_2 = ["56483",
           "Licht",
           "Lisa",
           "An der Sonne",
           "2",
           "45678",
           "Lichtenfels",
           "Kostal",
           "Piko 6",
           "1",
           "6",
           "6",
           "8,2"]

kunden = [kunde_1, kunde_2]


def ausfuellen(pdfdaten):
    reader = PdfReader("e2.pdf")
    writer = PdfWriter()

    # Sonst \Acroform-Error
    writer.clone_reader_document_root(reader)

    page = reader.pages[0]
    fields = reader.get_fields()

    #Kundendaten:
    # Vorname, Name
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text1": pdfdaten[1] + " " +pdfdaten[0]},
        auto_regenerate=False,
    )

    # Straße, Hausnummer
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text2": pdfdaten[2]+" "+pdfdaten[3]},
        auto_regenerate=False,
    )

    # PLZ, Ort
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text3": pdfdaten[4]+ " "+pdfdaten[5]},
        auto_regenerate=False,
    )


    # Technische Daten:
    # Hersteller
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text6": pdfdaten[6]},
        auto_regenerate=False,
    )

    # Modell
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text7": pdfdaten[7]},
        auto_regenerate=False,
    )

    # Anzahl baugleicher Einheiten
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text8": pdfdaten[8]},
        auto_regenerate=False,
    )

    # Umrichter Scheinleistung
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text9": pdfdaten[9]},
        auto_regenerate=False,
    )

    # Umrichter Wirkleistung
    writer.update_page_form_field_values(
        writer.pages[0],
        {"Text1": pdfdaten[10]},
        auto_regenerate=False,
    )

    # Modulleistung
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text10": pdfdaten[11]},
        auto_regenerate=False,
    )


    # Bemerkung 1
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Text14": "Diese PDF wurde automatisch erstellt mit autoPV"},
        auto_regenerate=False,
    )

    # Energieart - Sonne
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Check Box15": "/Ja"},
        auto_regenerate=False,
    )

    # Einspeiseart - Drehstrom
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Check Box25": "/Ja"},
        auto_regenerate=False,
    )


    # Group - Inselbetrieb
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Group26": "/Auswahl2"},
        auto_regenerate=False,
    )

    # Group - Motorischer Anlauf
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Group27": "/Auswahl3"},
        auto_regenerate=False,
    )

    # Group - Überschusseinspeisung
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Group28": "/Auswahl1"},
        auto_regenerate=False,
    )

    # Group - Volleinspeisung
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Group29": "/Auswahl3"},
        auto_regenerate=False,
    )

    # Blindleistungskompensation
    writer.update_page_form_field_values(
        writer.pages[0],
        {"E2_Check Box27": "/Ja"},
        auto_regenerate=False,
    )

    with open("e2_ausgefuellt_" + pdfdaten[0] + ".pdf", "wb") as output_stream:
        writer.write(output_stream)
def flatten(name):
    # Specify the input and output PDF file paths
    inputFile = "e2_ausgefuellt_" + name + ".pdf"
    outputFile = "e2_ausgefuellt_" + name + ".pdf"

    # Create an object of the PdfDocument class
    doc = PdfDocument()
    # Load the PDF file
    doc.LoadFromFile(inputFile)

    # Flatten the form fields in the file
    doc.Form.IsFlatten = True

    # Save the resulting file
    doc.SaveToFile(outputFile)
    doc.Close()



#Klasse UI_frm_main aus frm_main.py Datei importieren aus Ordner GUI
#import sys
#sys.path.insert(0, 'GUI')
#from benutzerober import Ui_frm_main


class Frm_kundenkartei(QMainWindow, Ui_frm_kundenkartei):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Datenmodell von QT (spiegelt Datenbank) als Objekt definieren -> relationale Tabelle
        mod_pv_rheinland = QtSql.QSqlRelationalTableModel()

        # Verknüpfung zu Tabelle aus Datenbank erzeugen
        mod_pv_rheinland.setTable("Kunden")
        mod_pv_rheinland.select()
        self.tb_kunden.setModel(mod_pv_rheinland)


#Formular von Klasse QMainWindow ableiten -> alle Eigenschaften vererben + UI Klasse (GUI Py Datei) initialisieren
class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):

        #Aufruf Konstruktor von übergeordneter Klasse (also von QMainWindow und Ui_frm_main),
        # dadurch werden alle Attribute von übergeordneter Klasse initialisiert
        super().__init__()

        #aus eigener Instanz (GUI) setupUI Methode aufrufen
        self.setupUi(self)

        #Liste der Klasse erstellen mit allen edit-feldern
        self.liste_kunde=[self.edit_kundennr, self.edit_name, self.edit_vorname, self.edit_strasse, self.edit_hausnr, self.edit_plz, self.edit_ort]
        self.liste_daten=[self.edit_wr_hersteller, self.edit_wr_modell, self.edit_wr_anzahl, self.edit_wr_scheinleistung, self.edit_wr_wirkleistung, self.edit_pv_leistung]

        self.dp_kunden.activated.connect(self.ausfuellen)
        self.bt_pdf_erstellen.clicked.connect(self.pdf_erstellen)
        self.bt_kundenkartei.clicked.connect(self.kundenkartei_anzeigen)


    def ausfuellen(self):
        if self.dp_kunden.currentText() == 'Siegbert Sonnenschein':
            self.edit_kundennr.setText(kunde_1[0])
            self.edit_name.setText(kunde_1[1])
            self.edit_vorname.setText(kunde_1[2])
            self.edit_strasse.setText(kunde_1[3])
            self.edit_hausnr.setText(kunde_1[4])
            self.edit_plz.setText(kunde_1[5])
            self.edit_ort.setText(kunde_1[6])

            self.edit_wr_hersteller.setText(kunde_1[7])
            self.edit_wr_modell.setText(kunde_1[8])
            self.edit_wr_anzahl.setText(kunde_1[9])
            self.edit_wr_wirkleistung.setText(kunde_1[10])
            self.edit_wr_scheinleistung.setText(kunde_1[11])

            self.edit_pv_leistung.setText(kunde_1[12])


            #for i in self.liste_kunde:
                #self.liste_kunde.setText(kunde_1)

        elif self.dp_kunden.currentText() == 'Lisa Licht':
            self.edit_kundennr.setText(kunde_2[0])
            self.edit_name.setText(kunde_2[1])
            self.edit_vorname.setText(kunde_2[2])
            self.edit_strasse.setText(kunde_2[3])
            self.edit_hausnr.setText(kunde_2[4])
            self.edit_plz.setText(kunde_2[5])
            self.edit_ort.setText(kunde_2[6])

            self.edit_wr_hersteller.setText(kunde_2[7])
            self.edit_wr_modell.setText(kunde_2[8])
            self.edit_wr_anzahl.setText(kunde_2[9])
            self.edit_wr_wirkleistung.setText(kunde_2[10])
            self.edit_wr_scheinleistung.setText(kunde_2[11])

            self.edit_pv_leistung.setText(kunde_2[12])


        elif self.dp_kunden.currentText() == 'Neu':
            self.edit_kundennr.clear()
            self.edit_name.clear()
            self.edit_vorname.clear()
            self.edit_strasse.clear()
            self.edit_hausnr.clear()
            self.edit_plz.clear()
            self.edit_ort.clear()

            self.edit_wr_hersteller.clear()
            self.edit_wr_modell.clear()
            self.edit_wr_anzahl.clear()
            self.edit_wr_wirkleistung.clear()
            self.edit_wr_scheinleistung.clear()
            self.edit_pv_leistung.clear()

            self.edit_wr_hersteller.setText(kunde_2[7])
            self.edit_wr_modell.setText(kunde_2[8])
            self.edit_wr_anzahl.setText(kunde_2[9])
            self.edit_wr_wirkleistung.setText(kunde_2[10])
            self.edit_wr_scheinleistung.setText(kunde_2[11])
            self.edit_pv_leistung.setText(kunde_2[12])

    def pdf_erstellen(self):
        if self.dp_kunden.currentText() == 'Siegbert Sonnenschein':
            pdfdaten = kunde_1[1:13]
        elif self.dp_kunden.currentText() == 'Lisa Licht':
            pdfdaten = kunde_2[1:13]
        elif self.dp_kunden.currentText() == 'Neu':
            pdfdaten = self.edit_name.text(),self.edit_vorname.text(), self.edit_strasse.text(), self.edit_hausnr.text(), self.edit_plz.text(), self.edit_ort.text(),self.edit_wr_hersteller.text(), self.edit_wr_modell.text(), self.edit_wr_anzahl.text(), self.edit_wr_scheinleistung.text(), self.edit_wr_wirkleistung.text(), self.edit_pv_leistung.text()

        ausfuellen(pdfdaten)
        flatten(pdfdaten[0])

    def kundenkartei_anzeigen(self):
        frm_kundenkartei.show()


#Verknüpfung Datenbank, in Klammern = Treiber der DB unterstützt
# Connection string for Azure SQL Database
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=tcp:solarteamrheinland.database.windows.net,1433;"
    "DATABASE=strDb;"
    "UID=stradmin;"
    "PWD=-u-D%-g2)?6$yzB;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    # Connect to the database
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connected to the database successfully!")

    # Example query
    cursor.execute("SELECT TOP 10 * FROM dbo.Clients")
    for row in cursor.fetchall():
        print(row)

    # Close the connection
    conn.close()
except Exception as e:
    print("Error:", e)


#Objekte anlegen: app=Anwendung, frm = Formular
app = QApplication()

frm_kundenkartei = Frm_kundenkartei()
frm_main = Frm_main()
#Formular anzeigen
frm_main.show()

#Anwendung ausführen
app.exec()







