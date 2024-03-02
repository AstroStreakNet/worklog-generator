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

def calculate_total_time(data):
    total_minutes = 0

    for entry in data:
        if len(entry) > 2:
            time_str = entry[2]
            hours, minutes = map(int, time_str.split(":"))
            total_minutes += hours * 60 + minutes

    total_hours, remaining_minutes = divmod(total_minutes, 60)
    total_time = "{:02d}:{:02d}".format(total_hours, remaining_minutes)
    return total_time

def generate(name, sID, week, c_tasks, n_tasks, summary):
    doc = SimpleDocTemplate(
        f"{sID}_week-{week}.pdf", 
        pagesize=A4, 
        rightMargin=inch/2, 
        leftMargin=inch/2,
        topMargin=0
    )

    elements = []
    spacer = Spacer(1, 0.3 * inch)
    spacer_small = Spacer(1, 0.1 * inch)
    light_red = colors.HexColor('#ff7f7f') 
    
    c_tasks.insert(0, ["TASKS", "STATUS", "TIME SPENT", "ACTION ITEM/NOTE"])
    n_tasks.insert(0, ["TASKS PLANNED FOR NEXT WEEK", "EXPECTED\nCOMPLETION"])

    ###
    ### Document Title
    swinny_icon = "swin-logo.png"
    image = Image(swinny_icon, width=50, height=100)
    image.hAlign = 'LEFT'

    title_style = ParagraphStyle(
        name='Title', 
        fontName='Helvetica-Bold', 
        fontSize=16, 
        textColor=colors.black,
        alignment=2
    )
    
    title_head_style = ParagraphStyle(
        name='Title Head',
        fontName='Helvetica-Bold', 
        fontSize=22, 
        textColor=colors.black,
        alignment=2 
    )

    title_text1 = "EAT40005 Engineering Technology Project A"
    title_text2 = "Individual Work Log"
    title_text3 = f"Week {week}"
    title1  = Paragraph(title_text1, style=title_style)
    title2 = Paragraph(title_text2, style=title_head_style)
    title3 = Paragraph(title_text3, style=title_style)

    title_table = Table([[title1],[spacer_small],[title2],[spacer],[title3]])

    # Constructing the title table with image and paragraphs
    header_table = Table(
        [[Image("swin-logo.png", width=60, height=120), title_table]],
        colWidths=[50, '*']
    )

    header_table.setStyle(TableStyle(
        [('VALIGN', (0, 0), (0, 0), 'TOP')])
    )

    elements.append(header_table)
    elements.append(spacer)

    ###
    ### User Information
    identification = [
        ["PROJECT NAME:", "47. Send us your (satellite) streaks"],
        ["STUDENT NAME:", name],
        ["STUDENT ID:", sID]
    ]

    identification_table = Table(identification, colWidths=[100, 413])
    identification_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (-1, -1), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BACKGROUND', (0, 0), (0, -1), light_red),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    identification_table.setStyle(identification_style)
    elements.append(identification_table)
    elements.append(spacer)


    ###
    ### Worklog Table
    worklog_table = Table(c_tasks, colWidths=[243, 70, 70, 130])
    worklog_style = TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-2, -1), 'CENTER'), 
        ('ALIGN', (-1, 0), (-1, -1), 'LEFT'), 
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('BACKGROUND', (0, 0), (-1, 0), light_red),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    worklog_table.setStyle(worklog_style)
    elements.append(worklog_table)
    elements.append(spacer_small)

    ###
    ### Total Hours
    total_time = calculate_total_time(c_tasks[1:])
    time_style = ParagraphStyle(
        name='hours', 
        fontName='Helvetica-Bold', 
        fontSize=13, 
        textColor=colors.black,
        alignment=2
    )
    time_text = f"Total Time: {total_time}"
    time_para = Paragraph(time_text, style=time_style)
    elements.append(time_para)
    elements.append(spacer)


    ###
    ### Tasks for next week 
    next_week_table = Table(n_tasks, colWidths=[413, 100])
    next_week_style = TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('BACKGROUND', (0, 0), (-1, 0), light_red),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    next_week_table.setStyle(next_week_style)
    elements.append(next_week_table)
    elements.append(spacer) 

    ###
    ### Summary
    # Summary Heading
    summary_hstyle = ParagraphStyle(
        name='Summary', 
        fontName='Helvetica-Bold', 
        fontSize=16, 
        textColor=colors.black
    )
    summary_htext = f"Summary/weekly reflection for Week {week}"
    summary_head = Paragraph(summary_htext, style=summary_hstyle)
    elements.append(summary_head)
    elements.append(spacer)

    # Summary Text 
    summary_tstyle = ParagraphStyle(
        name='SummaryContent', 
        fontName='Helvetica', 
        fontSize=12, 
        textColor=colors.black,
        alignment=4
    )
    summary_text = Paragraph(summary, style=summary_tstyle)
    elements.append(summary_text)

    # Build the document with all elements
    doc.build(elements)

    print("\n\n\033[31mpdf generated")

