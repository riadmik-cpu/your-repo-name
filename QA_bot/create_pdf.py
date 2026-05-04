# Create a simple PDF file with basic structure
import os

# Define the PDF content with basic PDF structure
pdf_content = b"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj

2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj

3 0 obj
<< /Type /Page /Parent 2 0 R /Resources << /Font << /F1 4 0 R >> >> /MediaBox [0 0 612 792] /Contents 5 0 R >>
endobj

4 0 obj
<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
endobj

5 0 obj
<< /Length 380 >>
stream
BT
/F1 24 Tf
50 700 Td
(Introduction to AI) Tj
ET
BT
/F1 12 Tf
50 650 Td
(Artificial Intelligence Overview) Tj
ET
BT
/F1 11 Tf
50 600 Td
(Artificial Intelligence (AI) is a rapidly evolving field that focuses on creating machines and) Tj
50 580 Td
(software capable of performing tasks that typically require human intelligence. These tasks) Tj
50 560 Td
(include learning from experience, recognizing patterns, understanding language, and making) Tj
50 540 Td
(decisions. AI technologies are transforming industries from healthcare and finance to) Tj
50 520 Td
(transportation and entertainment, making our world more efficient and connected than ever) Tj
50 500 Td
(before. As AI continues to advance, its impact on society and business will only grow stronger.) Tj
ET
endstream
endobj

xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000273 00000 n 
0000000355 00000 n 
trailer
<< /Size 6 /Root 1 0 R >>
startxref
786
%%EOF"""

# Define the path
pdf_path = "test_document.pdf"

# Write the PDF file
with open(pdf_path, 'wb') as f:
    f.write(pdf_content)

print(f"PDF created successfully at: {os.path.abspath(pdf_path)}")
print(f"File size: {os.path.getsize(pdf_path)} bytes")
