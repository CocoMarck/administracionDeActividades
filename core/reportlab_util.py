from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

from core import text_util
import os
from utils import ResourceLoader

# Ruta donde guardar archivos.
resource_loader = ResourceLoader()

# Crear ruta de reportes.
REPORT_DIR = resource_loader.get_base_path( "reports" )
if REPORT_DIR.is_dir():
    pass
else:
    os.mkdir( REPORT_DIR )




# Funciones para generar constantes
def gen_report_dict( report_lab_list: list ):
    report_lab_dict = {}
    number = 0
    for style, text in report_lab_list:
        report_lab_dict.update( {number : [style, text] } )
        number += 1
    
    return report_lab_dict




# Constantes
DEFAULT_REPORT_NAME = "report"
REPORTLAB_PARAGRAPH_LIST = [
    ["Heading1", "Reporte"],
    ["Normal", "Parrafo normalon"],
    ["Heading2", "Subtitulo"],
    ["Normal", "Un poco mas de texto"]
]
REPORTLAB_PARAGRAPH_DICT = gen_report_dict( REPORTLAB_PARAGRAPH_LIST )
REPORTLAB_STYLES = getSampleStyleSheet()





def create_report(
    name: str=DEFAULT_REPORT_NAME, 
    reportlab_paragraph_list: dict=REPORTLAB_PARAGRAPH_LIST
) -> bool:
    # Establecer archivo
    # Establecer tamaños de todo
    report_file = REPORT_DIR.joinpath( f"{name}.pdf" )
    
    size=LETTER
    width, height = size

    # Inicializar canvas | Contenido
    # Establecer contenido.
    doc = SimpleDocTemplate( str(report_file), pagesize=size )

    content = []
    for style, value in reportlab_paragraph_list:
        if style in REPORTLAB_STYLES:
            text = value
            content.append(
                Paragraph( text.replace( "\n", "<br/>"), REPORTLAB_STYLES[ style ]  )
            )
        elif style == "Table":
            columns = value
            col_widths = [width*0.9 / len(columns[0])] * len(columns[0]) # No me gusto
            
            # Establecer texto como tipo Paragraph
            table_data = []
            for row in columns:
                new_list = []
                for cell in row:
                    new_list.append( Paragraph(str(cell), REPORTLAB_STYLES["Normal"]) )
                table_data.append( new_list )
            
            # Generar tabla
            t = Table( table_data, colWidths=col_widths)
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ]))
            content.append( t )
    
    # Devolver
    try:
        doc.build(content)
        return True, report_file
    except:
        return False, report_file