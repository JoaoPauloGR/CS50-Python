from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 24)
        # print title
        self.cell(200, 20, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)
        # Rendering logo:
        self.image("shirtificate.png", y = 50, w = 175, h = 225)


pdf = PDF()
pdf.add_page()
username = input("Name: ")
pdf.set_font("Times", size=36)
pdf.set_text_color(255)
pdf.cell(175, 200, f"{username} took CS50", border=0, align="C")
pdf.output("shirtificate.pdf")