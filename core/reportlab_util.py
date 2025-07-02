from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from functools import partial

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





def draw_header_footer( 
        header_text: str, footer_text: str, multipler:int=0.95, page_number:bool=True
    ):
    '''
    Para objetos tipo SimpleDocTemplate
    '''
    def _inner(canvas, doc):
        width, height = doc.pagesize
        canvas.saveState()

        # Margen
        diferrence_xy = [width -width*multipler, height -height*multipler]
        
        # Establecer header, footer y numero de pagina en footer.
        if header_text:
            canvas.drawString( diferrence_xy[0], height*multipler, f"{header_text}")
        if footer_text:
            final_text = footer_text
            canvas.drawString( diferrence_xy[0], diferrence_xy[1], final_text)
        if page_number:
            canvas.drawRightString(width -diferrence_xy[0], diferrence_xy[1], f"{doc.page}")
        canvas.restoreState()
    return _inner





def create_report(
    name: str=DEFAULT_REPORT_NAME, size: str=LETTER, ninety_degree_turn: bool=False, 
    header: str=None, footer: str=None, page_number:bool=False,
    reportlab_paragraph_list: list=REPORTLAB_PARAGRAPH_LIST
) -> bool:
    # Establecer archivo
    # Establecer tamaños de todo
    report_file = REPORT_DIR.joinpath( f"{name}.pdf" )
    
    if ninety_degree_turn:
        size=( size[1], size[0] )
    width, height = size
    
    
    # Inicializar canvas | Contenido
    doc = SimpleDocTemplate( str(report_file), pagesize=size )
    
    # Header y footer
    header_footer = draw_header_footer(header, footer, page_number=page_number)

    # Establecer contenido.
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
        doc.build(content, onFirstPage=header_footer, onLaterPages=header_footer)
        return True, report_file
    except:
        return False, report_file