# Install FPDF if you haven't already:
# pip install fpdf

from fpdf import FPDF

# This is the text we want to save to a PDF.
text_to_save = """\
Below is a simple illustrative model showing one way to estimate how long it might take
for a small group of ultra-rich individuals (“the billionaires”) to end up owning essentially
all the world’s assets under straightforward (though somewhat extreme) assumptions.
The goal here is not to claim this will definitely happen but to walk through how one
might model it mathematically.

----------------------------------------------------
1. KEY ASSUMPTIONS
----------------------------------------------------
1) Initial total wealth (worldwide): W_0
   ...
[Cut for brevity—replace with the full explanation text you want in the PDF]
...
Hence, t ≈ 31.8 years.

----------------------------------------------------
5. SUMMARY OF THE MODEL
----------------------------------------------------
Fraction of wealth at time t:
    f(t) = f_0 * ((1 + r)/(1 + g))^t

Years until the richest own it all:
    t = ln(1/f_0) / ln((1 + r)/(1 + g))
"""

# Create a PDF object
pdf = FPDF()
pdf.add_page()

# Set the font and size
pdf.set_font("Arial", size=12)

# Write the text. multi_cell automatically wraps lines.
pdf.multi_cell(0, 10, text_to_save)

# Output the PDF file
pdf.output("billionaire_model.pdf")

print("PDF saved as 'billionaire_model.pdf'.")
