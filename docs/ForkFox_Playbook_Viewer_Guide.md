# How to View the ForkFox Playbook

If you want the fastest path, use **Option 1**.

## Option 1 (Fastest): Open in VS Code markdown preview
1. Open `docs/ForkFox_Master_GTM_and_Portal_Plan.md`.
2. Press `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac).
3. Use the markdown outline to jump between sections (Gates, Wireframes, Channel Tactics, KPI plan).

## Option 2: Read in terminal (quick skim)
```bash
sed -n '1,140p' docs/ForkFox_Master_GTM_and_Portal_Plan.md
sed -n '141,260p' docs/ForkFox_Master_GTM_and_Portal_Plan.md
sed -n '261,420p' docs/ForkFox_Master_GTM_and_Portal_Plan.md
```

## Option 3: Export to PDF for sharing
If `pandoc` is installed:
```bash
pandoc docs/ForkFox_Master_GTM_and_Portal_Plan.md \
  -o docs/ForkFox_Master_GTM_and_Portal_Plan.pdf
```

## Option 4: Present it as a slide flow (manual)
Treat these as slide sections:
1. Executive Read / Pipeline Status
2. Site Review + Conversion Gaps
3. Gate 1–4 Product Roadmap
4. Wireframes (5 screens)
5. Channel Tactics (Owned/Social/Partnership/Paid)
6. KPI Framework + 14-Day Sprint
7. Investor Narrative + Risks

## Suggested first-pass reading order (10 minutes)
1. `## 0` Executive Read
2. `## 3` Build Roadmap by Gate
3. `## 4` Wireframes by Function and Phase
4. `## 8` Immediate 14-Day Tactical Sprint

## Site review scope used for this plan
- `https://forkfox.ai/`
- `https://forkfox.ai/privacy/index.html`

If you want, next I can package this into:
- a **1-page exec brief**, and
- a **12-slide investor/ops deck draft** with speaker notes.
