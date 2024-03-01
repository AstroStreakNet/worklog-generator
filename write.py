# write.py

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, 
    Paragraph, 
    Spacer, 
    Image, 
    Table, 
    TableStyle
)

def generate(name, studentID, week, current_entries, next_entries, summary_content):
    doc = SimpleDocTemplate(f"{studentID}_week-{week}.pdf", pagesize=A4, rightMargin=inch/2, leftMargin=inch/2)

    # Document Title
    swinny_icon = "swin-logo.png"
    image = Image(swinny_icon, width=100, height=200)
    image.hAlign = 'LEFT'

    title_style = ParagraphStyle(
        name='Title', 
        fontName='Helvetica-Bold', 
        fontSize=16, 
        textColor=colors.black,
        leftIndent=110  # Adjust the left indent to align text with image
    )

    title_text1 = "EAT40005 Engineering Technology Project A"
    title_text2 = "Individual Work Log"
    title_text3 = f"\nWeek {week}"
    title = Paragraph(title_text1, style=title_style)
    title2 = Paragraph(title_text2, style=title_style)
    title3 = Paragraph(title_text3, style=title_style)

    # Spacer for separation
    spacer = Spacer(1, 0.5 * inch)

    # Worklog Table
    worklog_table = Table(current_entries, colWidths=(doc.width - inch) / len(current_entries[0]))  # Adjust the width
    worklog_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    worklog_table.setStyle(worklog_style)

    # Coming Week Plan Table
    next_week_table = Table(next_entries, colWidths=(doc.width - inch) / len(next_entries[0]))  # Adjust the width
    next_week_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    next_week_table.setStyle(next_week_style)

    # Summary
    summary_head_style = ParagraphStyle(
        name='Summary', 
        fontName='Helvetica-Bold', 
        fontSize=18, 
        textColor=colors.black
    )
    summary_head_text = f"Summary/weekly reflection for Week {week}"
    summary_head = Paragraph(summary_head_text, style=summary_head_style)

    summary_content_style = ParagraphStyle(
        name='SummaryContent', 
        fontName='Helvetica', 
        fontSize=12, 
        textColor=colors.black
    )
    summary_content = Paragraph(summary_content, style=summary_content_style)

    # Content layout
    content = [
        image, title,
        title2,
        title3,
        spacer,
        worklog_table,
        spacer,
        next_week_table,
        spacer,
        summary_head,
        summary_content
    ]

    # Build the document
    doc.build(content)

if __name__ == "__main__":
    summary = "hello world"
    c_entries = [
        ["title", "status", "time", "note"],
        ["title", "status", "time", "note"],
        ["title", "status", "time", "note"]
    ]
    n_entries = [
        ["title", "time"],
        ["title", "time"],
        ["title", "time"]
    ]

    generate("Snoop Monke", 12345678, 10, c_entries, n_entries, summary)
    print("PDF created successfully")
