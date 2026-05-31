"""Generate course submission PDF: cover info, emulator screenshots, source code."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCREENSHOTS_DIR = PROJECT_ROOT / "docs" / "screenshots"
MAIN_DART = PROJECT_ROOT / "lib" / "main.dart"
OUTPUT_PDF = PROJECT_ROOT / "Malak_ElAasar_211004130_Quote_App_Submission.pdf"

STUDENT = {
    "name": "Malak Ahmed ElAasar",
    "id": "211004130",
    "email": "malakelaasar11@gmail.com",
    "phone": "+201111880184",
    "github": "https://github.com/malakelaasar/Quote-App",
    "project": "Quote App V2 — Daily Inspiration (Flutter)",
}


def build_pdf() -> None:
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50,
        title="Quote App V2 Submission",
        author=STUDENT["name"],
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=22,
        textColor=colors.HexColor("#13756A"),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    )
    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=16,
        textColor=colors.HexColor("#13756A"),
        spaceBefore=16,
        spaceAfter=12,
        fontName="Helvetica-Bold",
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=11,
        leading=16,
        spaceAfter=6,
    )
    caption_style = ParagraphStyle(
        "Caption",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.HexColor("#4F6360"),
        alignment=TA_CENTER,
        spaceAfter=14,
    )
    code_style = ParagraphStyle(
        "Code",
        parent=styles["Code"],
        fontSize=7.5,
        leading=9,
        fontName="Courier",
        leftIndent=0,
    )

    story = []

    # --- Cover / student info ---
    story.append(Paragraph("Mobile Application — Assignment Submission", title_style))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph(STUDENT["project"], body_style))
    story.append(Spacer(1, 0.25 * inch))

    info_lines = [
        f"<b>Name:</b> {STUDENT['name']}",
        f"<b>Student ID:</b> {STUDENT['id']}",
        f"<b>Email:</b> {STUDENT['email']}",
        f"<b>Phone:</b> {STUDENT['phone']}",
        f"<b>GitHub:</b> {STUDENT['github']}",
    ]
    for line in info_lines:
        story.append(Paragraph(line, body_style))

    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "This document includes emulator screenshots of the running app "
            "and the complete source code for <b>lib/main.dart</b>.",
            body_style,
        )
    )
    story.append(PageBreak())

    # --- Screenshots ---
    story.append(Paragraph("Part 1 — App Screenshots (Emulator Output)", heading_style))
    story.append(
        Paragraph(
            "Screenshots below show the Quote App running on the Android emulator, "
            "cycling through all five inspirational quotes.",
            body_style,
        )
    )
    story.append(Spacer(1, 0.1 * inch))

    labels = [
        "Quote 1 — Small steps every day lead to big results.",
        "Quote 2 — Your attitude determines your direction.",
        "Quote 3 — Stay patient and trust your journey.",
        "Quote 4 — Discipline is choosing what you want most over what you want now.",
        "Quote 5 — Great things never come from comfort zones.",
    ]

    max_width = 4.8 * inch
    for i in range(1, 6):
        img_path = SCREENSHOTS_DIR / f"screenshot-{i}.png"
        if not img_path.exists():
            story.append(Paragraph(f"[Missing: {img_path.name}]", body_style))
            continue

        img = Image(str(img_path))
        aspect = img.imageHeight / float(img.imageWidth)
        img.drawWidth = max_width
        img.drawHeight = max_width * aspect
        if img.drawHeight > 6.5 * inch:
            img.drawHeight = 6.5 * inch
            img.drawWidth = img.drawHeight / aspect

        story.append(Paragraph(labels[i - 1], caption_style))
        story.append(img)
        story.append(Spacer(1, 0.15 * inch))
        if i in (2, 4):
            story.append(PageBreak())

    story.append(PageBreak())

    # --- Source code ---
    story.append(Paragraph("Part 2 — Source Code (lib/main.dart)", heading_style))
    story.append(
        Paragraph(
            "Full source code copied from the project entry point.",
            body_style,
        )
    )
    story.append(Spacer(1, 0.1 * inch))

    source = MAIN_DART.read_text(encoding="utf-8")
    numbered_lines = []
    for num, line in enumerate(source.splitlines(), start=1):
        numbered_lines.append(f"{num:4}| {line}")
    numbered_source = "\n".join(numbered_lines)

    # Split code across pages (reportlab Preformatted handles long text)
    chunk_size = 85
    lines = numbered_source.split("\n")
    for start in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[start : start + chunk_size])
        story.append(Preformatted(chunk, code_style))
        if start + chunk_size < len(lines):
            story.append(PageBreak())

    doc.build(story)
    print(f"Created: {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
