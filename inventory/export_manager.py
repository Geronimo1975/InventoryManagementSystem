import pandas as pd
from fpdf import FPDF
from io import BytesIO
from graphviz import Digraph

class InventoryExporter:
    @staticmethod
    def to_excel(products):
        """Exports the product list to an Excel file and returns the buffer."""
        if not isinstance(products, list):
            raise ValueError("Expected a list of dictionaries for export.")
        
        df = pd.DataFrame(products)
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Inventory')
        buffer.seek(0)
        return buffer

    @staticmethod
    def to_pdf(products):

        """Exports the product list to a PDF file and returns the buffer."""
        if not isinstance(products, list):
            raise ValueError("Expected a list of dictionaries for export.")
        
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Inventory Report", ln=True, align='C')

        pdf.set_font("Arial", size=12)
        pdf.ln(10)

        for product in products:
            pdf.cell(200, 10, txt=f"{product.get('name', 'Unknown')} - ${product.get('price', 0.00):.2f} - {product.get('quantity', 0)} pcs", ln=True)

        buffer = BytesIO()
        pdf.output(buffer)
        buffer.seek(0)
        return buffer

        class ProjectDiagram:
            @staticmethod
            def draw_diagram():
                dot = Digraph(comment='Inventory Management System')
                
                dot.node('A', 'InventoryExporter')
                dot.node('B', 'to_excel')
                dot.node('C', 'to_pdf')
                
                dot.edges(['AB', 'AC'])
                
                return dot

        # Example usage:
        # diagram = ProjectDiagram.draw_diagram()
        # diagram.render('/home/dci-student/Projects/InventoryManagementSystem/inventory/project_diagram', format='png')
    