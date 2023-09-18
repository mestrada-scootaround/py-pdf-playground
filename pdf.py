import PyPDF2
import sys

inputs = sys.argv[1:]

# with open('dummy.pdf', "rb") as file: ### we need to open in "rb" mode converts file object to binary mode
#   reader = PyPDF2.PdfFileReader(file)
#   page = reader.getPage(0)
#   page.rotateCounterClockwise(90)
#   writer = PyPDF2.PdfFileWriter()
#   writer.addPage(page)
#   with open('tilt.pdf', 'wb') as new_file:
#     writer.write(new_file)

### Exercise: merge pdfs
def pdf_combiner(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    print(pdf)
    merger.append(pdf)

  merger.write('super.pdf')

### Exercise: add watermark
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)

# pdf_combiner(inputs)