from fpdf import FPDF

name = input("Name: ")

# Create shirtificate.pdf
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", style="B", size=50)
#  Top says "CS50 Shirtificate"ceneterd horizontally
pdf.cell(40,pdf.eph/4,"CS50 Shirtificate", align="C", center=True)
pdf.image("shirtificate.png", y =pdf.h/4, x=10, w = pdf.w-20, keep_aspect_ratio=True)
pdf.set_font("Helvetica", style="B", size=25)
pdf.set_text_color(255,255,255)
pdf.cell(40,pdf.eph,f"{name} took CS50", align="C", center=True)

# shirt immage centered horizontally
# name ontop os fhirt in white text
pdf.output("shirtificate.pdf")