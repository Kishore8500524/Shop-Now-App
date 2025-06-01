from fpdf import FPDF
import tempfile
import os
from invoice_utils import print_invoice
def generate_invoice_pdf(cart_items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Invoice", ln=True, align='C')
    pdf.ln(10)

    total = 0
    for item in cart_items:
        name = item['name']
        price = item['price']
        quantity = item.get('quantity', 1)
        line_total = price * quantity
        total += line_total

        pdf.cell(200, 10, txt=f"{name} - ₹{price:.2f} x {quantity} = ₹{line_total:.2f}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total: ₹{total:.2f}", ln=True)

    # Save PDF to a temporary file
    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, "invoice.pdf")
    pdf.output(pdf_path)
    return pdf_path
