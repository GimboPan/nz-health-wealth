# Project working instructions

- This is a static Chinese-language NZ Health & Wealth field guide.
- Read `docs/EDITORIAL.md` before editing claims and `docs/ARCHITECTURE.md` before changing data flow.
- Update structured content in `content/entries.json`; never write a separate hidden copy in UI code.
- Preserve stable entry IDs, clear source attribution, verification dates and limitations.
- A retrieved podcast transcript is not a verified fact, and retrieving all transcripts is not reviewing all episodes.
- Keep complete transcripts, audio, SQLite databases, credentials and personal records out of the public repository and deployment.
- Build with `python3 scripts/build.py`; syntax-check `src/app.js` with Node if available. Verify meaningful reader interactions and mobile layout after UI changes.
- Do not create a remote repository, publish content, schedule updates or send messages unless the user authorizes that action.

- Every programme citation must retain real speaker-block boundaries, role (basis/background), a segment hash and an explicit no-audio-check boundary. Run `scripts/validate_evidence.py` with local inventories after citation edits.
- Official-only supplements must say the reviewed programme material did not cover them; never invent a timestamp.
- `src/page.template.html` is the build template; `src/index.html` routes readers to the generated page.
