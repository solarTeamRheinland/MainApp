from pypdf import PdfReader, PdfWriter
from spire.pdf import *
import pyodbc

#aus Ordner GUI (im selben Verzeichnis wie main.py) Klasse UI_frm_main aus py datei b.py (GUI) importieren
from frm_main import Ui_frm_main
from frm_kundenkartei import Ui_frm_kundenkartei


#qapplication = Klasse die Anwendung steuer, QMainwindow = Hauptfenster
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtSql
from PySide6.QtGui import QIcon

#designer öffnen: Terminal: pyside6-designer
#wenn GUI Datei im Designer erstellt und gespeichert wurde, kann diese in eine Py-Datei konvertiert werden:
#in Terminal: pyside6-uic frm_main.ui -o frm_main.py


def resource_path(relative_path):
    """
    Get the absolute path to a resource, accounting for PyInstaller bundling.
    - During development: Looks for the file directly (no _internal folder).
    - After bundling: Adjusts to PyInstaller's structure (_MEIPASS or similar).
    """
    if getattr(sys, 'frozen', False):  # If running as a PyInstaller bundle
        base_path = sys._MEIPASS  # Temporary extraction folder created by PyInstaller
    else:
        base_path = os.path.abspath(".")  # Current directory during development
    return os.path.join(base_path, relative_path)

def ausfuellen(pdfdaten):
    pdf_path = resource_path("e2.pdf")

    # Check if the file exists before proceeding
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Required PDF file not found: {pdf_path}")

    reader = PdfReader(pdf_path)
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

    # Define the output folder
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists

    # Define the output file path
    output_filename = f"e2_ausgefuellt_{pdfdaten[0]}.pdf"
    output_path = os.path.join(output_folder, output_filename)

    with open(output_path, "wb") as output_stream:
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

        self.setWindowTitle("AutoPV")
        self.setWindowIcon(QIcon(resource_path("logo.png")))
        #aus eigener Instanz (GUI) setupUI Methode aufrufen
        self.setupUi(self)
        self.bt_pdf_erstellen.clicked.connect(self.pdf_erstellen)
        self.table_widget.itemSelectionChanged.connect(self.on_row_selected)

    def on_row_selected(self):
        """
        Prints the value of the second column of the selected row.
        """
        selected_row = self.table_widget.currentRow()  # Get the index of the selected row
        if selected_row >= 0:  # Ensure a valid row is selected
            id = self.table_widget.item(selected_row, 0).text()  
            vorname = self.table_widget.item(selected_row, 2).text()  
            name = self.table_widget.item(selected_row, 3).text()  
            strasse = self.table_widget.item(selected_row, 4).text()  
            hausNr = self.table_widget.item(selected_row, 5).text()
            plz = self.table_widget.item(selected_row, 6).text()
            ort = self.table_widget.item(selected_row, 7).text()

            self.customer_fields["edit_kundennr"].setText(id)
            self.customer_fields["edit_name"].setText(name)
            self.customer_fields["edit_vorname"].setText(vorname)
            self.customer_fields["edit_strasse"].setText(strasse)
            self.customer_fields["edit_hausnr"].setText(hausNr)
            self.customer_fields["edit_plz"].setText(plz)
            self.customer_fields["edit_ort"].setText(ort)

            self.liste_daten_fields["edit_wr_hersteller"].setText("Kostal")
            self.liste_daten_fields["edit_wr_modell"].setText("Piko 6")
            self.liste_daten_fields["edit_wr_anzahl"].setText("1")
            self.liste_daten_fields["edit_wr_wirkleistung"].setText("6")
            self.liste_daten_fields["edit_wr_scheinleistung"].setText("6")
            self.liste_daten_fields["edit_pv_leistung"].setText("8,2")

    from PySide6.QtWidgets import QMessageBox

    def pdf_erstellen(self):
        try:
            # Collecting the data
            pdfdaten = (
                self.customer_fields["edit_name"].text(),
                self.customer_fields["edit_vorname"].text(),
                self.customer_fields["edit_strasse"].text(),
                self.customer_fields["edit_hausnr"].text(),
                self.customer_fields["edit_plz"].text(),
                self.customer_fields["edit_ort"].text(),
                self.liste_daten_fields["edit_wr_hersteller"].text(),
                self.liste_daten_fields["edit_wr_modell"].text(),
                self.liste_daten_fields["edit_wr_anzahl"].text(),
                self.liste_daten_fields["edit_wr_scheinleistung"].text(),
                self.liste_daten_fields["edit_wr_wirkleistung"].text(),
                self.liste_daten_fields["edit_pv_leistung"].text(),
            )

            # Attempt to fill and flatten the PDF
            ausfuellen(pdfdaten)

            # Show success dialog
            success_dialog = QMessageBox()
            success_dialog.setIcon(QMessageBox.Information)
            success_dialog.setWindowTitle("Erfolg")
            success_dialog.setWindowIcon(QIcon(resource_path("logo.png")))
            success_dialog.setText("PDF wurde erfolgreich erstellt!")
            success_dialog.setInformativeText("Die Datei wurde im Ausgabeverzeichnis gespeichert.")
            success_dialog.exec()

        except Exception as e:
            # Show an error dialog with the exception message
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("An error occurred while creating the PDF.")
            error_dialog.setInformativeText(str(e))
            error_dialog.exec()


def fetch_data_from_db():
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
        query = "SELECT TOP 10 * FROM dbo.Clients"
        cursor.execute(query)

        # Fetch all rows and column names
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        # Convert to a list of dictionaries or objects
        result = [dict(zip(column_names, row)) for row in rows]

        # Close the connection
        conn.close()

        return result

    except Exception as e:
        print("Error:", e)
        return []

#Objekte anlegen: app=Anwendung, frm = Formular
data_list = fetch_data_from_db()

app = QApplication()
frm_main = Frm_main()
frm_main.populate_table_with_data(data_list)
frm_main.show()

#Anwendung ausführen
app.exec()







