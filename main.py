# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# ---------- Palette ----------
INK = colors.HexColor("#1a1a1a")
SLATE = colors.HexColor("#4a4a4a")
ACCENT = colors.HexColor("#2b4c7e")
LIGHT_LINE = colors.HexColor("#c9c9c9")

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name", fontName="Helvetica-Bold", fontSize=24, textColor=INK,
    spaceAfter=2, leading=28,
)
title_style = ParagraphStyle(
    "RoleTitle", fontName="Helvetica", fontSize=12.5, textColor=ACCENT,
    spaceAfter=8, leading=15,
)
contact_style = ParagraphStyle(
    "Contact", fontName="Helvetica", fontSize=9.3, textColor=SLATE,
    spaceAfter=0, leading=13,
)
section_style = ParagraphStyle(
    "Section", fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT,
    spaceBefore=7, spaceAfter=2, leading=12.5, letterSpacing=0.6,
)
body_style = ParagraphStyle(
    "Body", fontName="Helvetica", fontSize=9.3, textColor=INK,
    leading=12.6, spaceAfter=2, alignment=TA_LEFT,
)
job_title_style = ParagraphStyle(
    "JobTitle", fontName="Helvetica-Bold", fontSize=10, textColor=INK,
    leading=12, spaceAfter=0.5,
)
job_meta_style = ParagraphStyle(
    "JobMeta", fontName="Helvetica-Oblique", fontSize=8.6, textColor=SLATE,
    leading=11, spaceAfter=2.5,
)
bullet_style = ParagraphStyle(
    "Bullet", fontName="Helvetica", fontSize=9, textColor=INK,
    leading=12, leftIndent=12, spaceAfter=2, bulletIndent=0,
)
skills_cat_style = ParagraphStyle(
    "SkillsCat", fontName="Helvetica-Bold", fontSize=9.5, textColor=INK,
    leading=13,
)

doc = SimpleDocTemplate(
    "Joshua_Uduma_Resume.pdf",
    pagesize=letter,
    topMargin=0.45 * inch,
    bottomMargin=0.4 * inch,
    leftMargin=0.65 * inch,
    rightMargin=0.65 * inch,
    title="Joshua Uduma - Resume",
)

story = []

def hr():
    story.append(HRFlowable(width="100%", thickness=0.8, color=LIGHT_LINE, spaceBefore=2, spaceAfter=6))

def bullets(items):
    for it in items:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{it}", bullet_style))

# ---------- Header ----------
story.append(Paragraph("Joshua Uduma", name_style))
story.append(Paragraph("Full-Stack Developer &amp; Framework Author", title_style))
story.append(Paragraph(
    "[email@example.com]  |  [+234 000 000 0000]  |  Lagos, Nigeria  |  "
    "github.com/Danieljosh-uduma  |  [LinkedIn / Portfolio URL]",
    contact_style
))
story.append(Spacer(1, 5))
hr()

# ---------- Summary ----------
story.append(Paragraph("SUMMARY", section_style))
story.append(Paragraph(
    "Full-stack developer and framework author with a track record of building developer "
    "tooling from first principles alongside client-facing web products. Designed and built "
    "Omni, a custom runtime interpreter framework that compiles a proprietary <b>.omni</b> file "
    "format into reactive web applications through a full tokenizer &rarr; parser &rarr; resolver "
    "&rarr; renderer pipeline, and Zen, a Go HTTP framework built directly on <b>net/http</b> "
    "primitives with custom routing and graceful shutdown handling. Combines this systems-level "
    "depth with delivery of production marketing sites, branded design assets, and full web "
    "applications for freelance clients.",
    body_style
))

# ---------- Featured Projects ----------
story.append(Paragraph("FEATURED PROJECTS", section_style))

story.append(Paragraph("Omni Framework &mdash; Runtime Interpreter Framework", job_title_style))
story.append(Paragraph("Personal / Open Source &middot; JavaScript, Node.js", job_meta_style))
bullets([
    "Architected a custom <b>.omni</b> file format and a full compilation pipeline "
    "(tokenizer &rarr; parser &rarr; resolver &rarr; renderer) that turns source files into "
    "working web applications.",
    "Built a dual-engine architecture with a semantic element system, differentiating the "
    "framework from conventional templating approaches.",
    "Implemented a reactive scripting subsystem with live DOM updates, verified end-to-end "
    "through real Node.js test runs.",
    "Identified and tracked remaining engineering gaps (subscription memory leaks, "
    "<b>oninput</b>/<b>onchange</b> wiring, parameterless functions) as part of an ongoing "
    "hardening phase.",
])

story.append(Paragraph("Studio Framer &mdash; Web Framework", job_title_style))
story.append(Paragraph("Personal / Open Source &middot; JavaScript", job_meta_style))
bullets([
    "Designed and maintained a JavaScript web framework as a comparison baseline against "
    "Omni, informing architectural decisions around file formats and rendering strategy.",
    "Published and maintained the project publicly under the Danieljosh-uduma GitHub account.",
])

story.append(Paragraph("Zen &mdash; Go HTTP Framework", job_title_style))
story.append(Paragraph("Personal / Open Source &middot; Go", job_meta_style))
bullets([
    "Built a Go web framework from scratch on top of <b>net/http</b>, including a custom "
    "<b>ServeMux</b> with wildcard routing and the <b>Handler</b> interface.",
    "Implemented server lifecycle management with graceful shutdown and dependency injection "
    "patterns using an <b>App</b> struct and <b>Store</b> interface.",
    "Extended the framework with a working web server (Chirpy), adding a <b>/healthz</b> "
    "endpoint, a fileserver with prefix stripping, and an atomic request counter exposed via "
    "<b>/metrics</b> and <b>/reset</b> endpoints.",
])

# ---------- Client Work ----------
story.append(Paragraph("CLIENT &amp; FREELANCE WORK", section_style))

story.append(Paragraph("LockIn &mdash; Video Conferencing App", job_title_style))
story.append(Paragraph("Freelance &middot; Design &amp; Web", job_meta_style))
bullets([
    "Produced promotional and brand graphics to support product marketing and user acquisition.",
])

story.append(Paragraph("Sourcegrove &mdash; Procurement Platform", job_title_style))
story.append(Paragraph("Freelance &middot; Web Development &amp; Design", job_meta_style))
bullets([
    "Built a full procurement website, delivered in multiple color variants to meet brand "
    "guidelines and stakeholder preferences.",
])

story.append(Paragraph("Dsenda &mdash; Financial Intelligence Company", job_title_style))
story.append(Paragraph("Freelance &middot; Brand &amp; Logo Design", job_meta_style))
bullets([
    "Designed the company logo and supporting brand identity elements.",
])

story.append(Paragraph("Dlytics &mdash; Data Analytics Company", job_title_style))
story.append(Paragraph("Freelance &middot; Web Development", job_meta_style))
bullets([
    "Built a complete marketing website from a detailed product requirements document (PRD), "
    "covering structure, content implementation, and responsive design.",
])

# ---------- Skills ----------
story.append(Paragraph("SKILLS", section_style))
skills_table_data = [
    [Paragraph("Languages &amp; Runtimes", skills_cat_style),
     Paragraph("JavaScript, Node.js, Go", body_style)],
    [Paragraph("Frameworks &amp; Tooling", skills_cat_style),
     Paragraph("Custom framework/interpreter design, net/http, REST API design", body_style)],
    [Paragraph("Core Concepts", skills_cat_style),
     Paragraph("Tokenizers &amp; parsers, reactive rendering, DOM diffing/updates, "
               "routing, dependency injection, server lifecycle management", body_style)],
    [Paragraph("Web &amp; Design", skills_cat_style),
     Paragraph("Responsive web development, marketing sites, brand identity &amp; "
               "logo design, event/promotional graphics", body_style)],
]
skills_table = Table(skills_table_data, colWidths=[1.55 * inch, 5.15 * inch])
skills_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
]))
story.append(skills_table)

# ---------- Education / Additional ----------
story.append(Paragraph("ADDITIONAL", section_style))
bullets([
    "Active open-source contributor; GitHub: github.com/Danieljosh-uduma",
    "Comfortable owning projects end-to-end: architecture, implementation, testing, and "
    "client-facing delivery.",
])

doc.build(story)
print("done")