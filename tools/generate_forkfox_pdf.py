#!/usr/bin/env python3
"""Generate a branded PDF from the ForkFox markdown plan without external deps."""
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "ForkFox_Master_GTM_and_Portal_Plan.md"
OUT = ROOT / "docs" / "ForkFox_Full_Detailed_Plan.pdf"

PAGE_W, PAGE_H = 612, 792  # US Letter
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 54, 64, 54
FONT_SIZE = 11
LINE_H = 15
MAX_CHARS = 92

# Brand-inspired palette (based on forkfox.ai visual identity)
FOX_ORANGE = (0.95, 0.44, 0.12)
INK = (0.10, 0.11, 0.13)
MUTED = (0.28, 0.30, 0.34)


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def wrap_markdown(md_text: str):
    lines = []
    for raw in md_text.splitlines():
        if raw.startswith("```"):
            lines.append(("text",""))
            continue
        s = raw.rstrip()
        if not s:
            lines.append(("text",""))
            continue

        indent = ""
        bullet = ""
        content = s
        if s.lstrip().startswith("- "):
            indent = "  "
            bullet = "• "
            content = s.lstrip()[2:]
        elif s.lstrip()[:2].isdigit() and ". " in s.lstrip()[:5]:
            indent = "  "
            n = s.lstrip().split(". ", 1)[0]
            bullet = f"{n}. "
            content = s.lstrip().split(". ", 1)[1]
        elif s.startswith("#"):
            # keep heading as-is but strip markdown markers
            content = s.lstrip("#").strip().upper()
            lines.append(("heading", content))
            continue

        wrapped = textwrap.wrap(content, width=MAX_CHARS - len(indent) - len(bullet)) or [""]
        for i, chunk in enumerate(wrapped):
            prefix = indent + (bullet if i == 0 else " " * len(bullet))
            lines.append(("text", prefix + chunk))
    return lines


def render_pages(flow_lines):
    pages = []
    current = []
    y = PAGE_H - MARGIN_TOP

    def new_page():
        return [
            "q",
            f"{INK[0]:.3f} {INK[1]:.3f} {INK[2]:.3f} rg",
            "Q",
            "BT",
            f"/F1 {FONT_SIZE} Tf",
        ]

    current = new_page()

    # page header bar
    def draw_header(cmds, page_num):
        cmds.extend([
            "q",
            f"{FOX_ORANGE[0]:.3f} {FOX_ORANGE[1]:.3f} {FOX_ORANGE[2]:.3f} rg",
            f"0 {PAGE_H-18} {PAGE_W} 18 re f",
            "Q",
            "BT",
            "/F2 11 Tf",
            f"{MARGIN_X} {PAGE_H-13} Td",
            f"({pdf_escape('ForkFox · Full Detailed Strategy Plan')}) Tj",
            "ET",
            "BT",
            "/F1 9 Tf",
            f"{PAGE_W-MARGIN_X-40} {PAGE_H-13} Td",
            f"({page_num}) Tj",
            "ET",
            "BT",
            f"/F1 {FONT_SIZE} Tf",
        ])

    page_num = 1
    draw_header(current, page_num)

    for kind, text in flow_lines:
        needed = LINE_H * (1.4 if kind == "heading" else 1)
        if y - needed < MARGIN_BOTTOM:
            current.append("ET")
            pages.append("\n".join(current))
            page_num += 1
            current = new_page()
            draw_header(current, page_num)
            y = PAGE_H - MARGIN_TOP

        if kind == "heading":
            y -= int(LINE_H * 1.2)
            current.extend([
                "ET",
                "BT",
                "/F2 13 Tf",
                f"{FOX_ORANGE[0]:.3f} {FOX_ORANGE[1]:.3f} {FOX_ORANGE[2]:.3f} rg",
                f"{MARGIN_X} {y} Td",
                f"({pdf_escape(text)}) Tj",
                "ET",
                "BT",
                f"/F1 {FONT_SIZE} Tf",
                f"{MUTED[0]:.3f} {MUTED[1]:.3f} {MUTED[2]:.3f} rg",
            ])
            y -= int(LINE_H * 0.6)
        else:
            y -= LINE_H
            current.extend([
                f"1 0 0 1 {MARGIN_X} {y} Tm",
                f"({pdf_escape(text)}) Tj",
            ])

    current.append("ET")
    pages.append("\n".join(current))
    return pages


def build_pdf(page_streams):
    objs = []

    def add_obj(content: bytes):
        objs.append(content)
        return len(objs)

    font1 = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    font2 = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    content_ids = []
    for s in page_streams:
        b = s.encode("latin-1", "replace")
        content_ids.append(add_obj(f"<< /Length {len(b)} >>\nstream\n".encode() + b + b"\nendstream"))

    page_ids = []
    pages_kids = []
    pages_id_placeholder = len(objs) + 1 + len(content_ids) + 1

    for cid in content_ids:
        page_dict = (
            f"<< /Type /Page /Parent {pages_id_placeholder} 0 R "
            f"/MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Resources << /Font << /F1 {font1} 0 R /F2 {font2} 0 R >> >> "
            f"/Contents {cid} 0 R >>"
        ).encode("latin-1")
        pid = add_obj(page_dict)
        page_ids.append(pid)
        pages_kids.append(f"{pid} 0 R")

    pages_obj = add_obj(f"<< /Type /Pages /Kids [{' '.join(pages_kids)}] /Count {len(page_ids)} >>".encode())
    catalog_obj = add_obj(f"<< /Type /Catalog /Pages {pages_obj} 0 R >>".encode())

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for i, obj in enumerate(objs, start=1):
        offsets.append(len(out))
        out.extend(f"{i} 0 obj\n".encode())
        out.extend(obj)
        out.extend(b"\nendobj\n")

    xref_start = len(out)
    out.extend(f"xref\n0 {len(objs)+1}\n".encode())
    out.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode())
    out.extend(
        f"trailer\n<< /Size {len(objs)+1} /Root {catalog_obj} 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode()
    )
    return out


def main():
    if not SRC.exists():
        raise SystemExit(f"Source markdown not found: {SRC}")
    content = SRC.read_text(encoding="utf-8")
    flow = wrap_markdown(content)
    pages = render_pages(flow)
    pdf_bytes = build_pdf(pages)
    OUT.write_bytes(pdf_bytes)
    print(f"Generated: {OUT} ({len(pages)} pages)")


if __name__ == "__main__":
    main()
