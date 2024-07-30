from fpdf import FPDF



def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(text='CS50 Shirtificate', border=0, ln='DEPRECATED', align="C", fill=False, link='', center=True, markdown=False)
    pdf.ln(80)
    pdf.image("shirtificate.png", x="C", y=30, w=0, h=200)
    name = input("What is your name? ")
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(text=f"{name} took CS50", border=0, ln='DEPRECATED', align="C", fill=False, link='', center=True, markdown=False)

    pdf.output("shirtificate.pdf")
if __name__ == "__main__":
    main()
