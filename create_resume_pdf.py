from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).parent
OUTPUT = ROOT / "resume.pdf"
styles = getSampleStyleSheet()

title = ParagraphStyle("ResumeTitle", parent=styles["Title"], alignment=TA_CENTER,
                       fontName="Helvetica-Bold", fontSize=22, leading=26,
                       textColor=colors.HexColor("#1F2937"))
subtitle = ParagraphStyle("ResumeSubtitle", parent=styles["Normal"], alignment=TA_CENTER,
                          fontSize=11, leading=15, textColor=colors.HexColor("#3B82F6"))
heading = ParagraphStyle("ResumeHeading", parent=styles["Heading2"], fontName="Helvetica-Bold",
                         fontSize=14, leading=18, textColor=colors.HexColor("#1F2937"),
                         spaceBefore=10, spaceAfter=6)
body = ParagraphStyle("ResumeBody", parent=styles["BodyText"], fontSize=9.2, leading=12,
                      textColor=colors.HexColor("#1F2937"))
small = ParagraphStyle("ResumeSmall", parent=body, fontSize=8.5, leading=11)


def p(text, style=body):
    return Paragraph(text, style)


story = [
    p("Khushi Patel", title),
    p("Computer Information Technology Student", subtitle),
    Spacer(1, 0.12 * inch),
    p("khushi-akshay.patel.610@my.csun.edu &nbsp;|&nbsp; (747) 366-2891", small),
    Spacer(1, 0.08 * inch),
    p("Computer Information Technology student at California State University, Northridge, with a minor in Business Analytics. Interested in information technology, database systems, web development, and business analytics.", body),
    p("Work Experience", heading),
]

work_rows = [
    [p("<b>Student Assistant</b><br/>David Nazarian College of Business and Economics<br/>Present", small),
     p("Processed impact journal publication awards and check requests for faculty. Created room reservations, maintained office supply inventory, provided key cards, and regulated college postings.", small)],
    [p("<b>Social Media Manager</b><br/>March 2021 - August 2022", small),
     p("Created written content, edited images, designed infographics, responded to clients, and analyzed current trends.", small)],
]
work = Table(work_rows, colWidths=[2.05 * inch, 4.85 * inch], hAlign="LEFT")
work.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
]))
story += [work,
          p("Academic Projects", heading),
          p("<b>Flight Reservation System</b> (January 2026 - May 2026)<br/>Developed a JavaFX application connected to Supabase PostgreSQL using REST APIs. Implemented flight search, dynamic pricing, seat availability, booking confirmation, and an admin panel.", body),
          Spacer(1, 0.06 * inch),
          p("<b>IT Help Desk Ticketing System</b> (August 2025 - December 2025)<br/>Designed a support workflow with ticket submission, priority categorization, status tracking, SQL database management, and Python backend logic.", body),
          p("Education", heading),
          p("<b>California State University, Northridge</b><br/>Bachelor of Science in Computer Information Technology<br/>Minor in Business Analytics<br/>Expected Graduation: Spring 2027 &nbsp;|&nbsp; Current GPA: 3.32", body),
          p("Leadership Experience", heading),
          p("<b>College Fair Server</b> - David Nazarian College of Business and Economics (September 2024 - Present)<br/>Led stations, distributed school resources, and supported an event serving 500 students.", body),
          p("<b>Teacher Assistant</b> - Humankind NGO (September 2022 - December 2022)<br/>Assisted students with grading, scheduling, technical issues, and computer-based tests.", body),
          p("Skills", heading),
          p("<b>Languages:</b> English and Hindi<br/><b>Software:</b> Microsoft Office Suite, Google Workspace, macOS, Windows, and Linux<br/><b>Technical:</b> Python, SQL, MySQL, HTML, CSS, TCP/IP, DNS, DHCP, network troubleshooting, printer and scanner operation", body),
]

doc = SimpleDocTemplate(str(OUTPUT), pagesize=letter, rightMargin=0.55 * inch,
                        leftMargin=0.55 * inch, topMargin=0.5 * inch,
                        bottomMargin=0.5 * inch, title="Khushi Patel Resume")
doc.build(story)
print(OUTPUT)
