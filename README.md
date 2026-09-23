# Break My Method — five-slide pitch

An offline, self-contained HTML pitch deck adapted from [agdestein/SlidesEccomas2026](https://github.com/agdestein/SlidesEccomas2026), reference revision `251e233aef0e797faa32268e294ebe5a00f923bb`.

The design retains the reference's ice-paper background, petrol serif typography, amber emphasis, 1280×720 slide stage, keyboard/swipe navigation, hash links and print layout. The pitch content, data and five layouts are specific to Break My Method. No source research figures, funding claims or author affiliations are reused. Slide 2 distinguishes live GPT-OSS-120B planning from previously executed Qwen3-30B email answers.

## Present

Public presentation: https://xinyuanwang283.github.io/break-my-method-pitch/

Open `index.html` in any browser, online or offline. No installation or network dependency is needed for the slides. The live demo itself needs internet access. `workflow-replay.gif` is a local recording-based illustration of clean audit run 1, copied from the app’s verified workflow asset; it also works offline.

- Arrow keys or Page Up/Down: previous/next slide.
- Home / End: first/last slide.
- F: fullscreen.
- N: speaker notes; Escape closes notes.
- D: open the live demo in a new tab. The title on slide 3 is also a demo link.
- G: open the 28-second recorded workflow GIF in a new tab; use it as a demo explanation or fallback.
- `#s1` through `#s5`: direct links to individual slides.
- Print to PDF: landscape 16:9, all five slides, no browser headers/footers. `pitch.pdf` is the prepared fallback.

The public HTML link is viewable without login. Viewers have no editing rights to this repository. This is an HTML presentation, not a Google Slides document.

## Source and build

```sh
python3 build.py src/pitch.tpl.html index.html
```

`build.py` is reused from the reference. It injects `assets/data.json` into the template and rejects unresolved tokens. `assets/manifest.json` and `assets/math.json` are intentionally empty; this deck requires no external image or math assets. All content remains editable in HTML. `build_pdf.py` creates the selectable-text PDF fallback using ReportLab and macOS Georgia/Arial fonts. `speaker-notes.md` includes the timed speaking script.

## Evidence

Metrics come from the frozen clean audit `20260923T105229532804Z`. Only the small aggregate summary needed by the deck is included. No API key, raw customer fixture, historical/mixed-V1 cache, or new experiment is included.

- Fresh planner runs: 2, 2, 1 test families.
- Exact random expectation: 3.5 families, full search without replacement.
- Within two tests: Nebius 3/3; random 33.3%.
- Prompt injection: production V1 40%, candidate V2 0%, a 40 pp drop.
- Small synthetic demonstration, n=3. This is not evidence of general superiority or statistical significance.

The planner budget is three; the random discovery expectation covers all six families. Live results vary and must not be substituted for the audited benchmark. The speaker notes retain these qualifications and distinguish proposed business/roadmap plans from implemented capabilities.

## Timing

0:00–0:45 Problem; 0:45–1:20 Product + Nebius; 1:20–2:40 Live demo; 2:40–3:40 Evidence; 3:40–4:30 Company; 4:30–5:00 Close/buffer.
