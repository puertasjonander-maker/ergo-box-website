# ERGO BOX — Design system

Single-surface landing page. Mode: **Persuade** — the visitor's success is a booked
diagnostic or a downloaded guide.

Everything lives in `index.html` (inline `<style>`, inline `<script>`). There is no
build step. Fonts are self-hosted under `assets/fonts/`.

---

## Type

Three families, three roles. A role is never carried by two families.

| Role | Family | Where it is used |
|---|---|---|
| **Editorial** | Piazzolla (variable 100–900, roman + italic) | Display headlines, ledes, long-form prose, pull quote |
| **UI** | Archivo (variable 100–900) | Nav, buttons, form controls, list and card copy, footer |
| **Spec** | DM Mono (400, 500) | Section numbers, eyebrow, proof chips, step numbers, price note, badge |

Tokens: `--font-editorial`, `--font-ui`, `--font-spec`. Named by role, not by
classification — the editorial face sets both display *and* body prose.

### Why these

Piazzolla is a text-and-display serif drawn with Spanish in mind, sturdy rather than
fashionable — it carries the magazine structure the page is built on without the
fragility of a Didone, which suits a business about iron and grit. Archivo is a
grotesque with enough width and weight range to stay legible in small UI copy on both
the cream and the near-black surfaces. DM Mono earns its place only where the content
is genuinely a measurement or an index.

Replaced Fraunces / Inter / JetBrains Mono in July 2026. Those were flagged as
category-default faces; the page now loads no third-party font origin.

### Scale and weight

- `--w-display: 800`. Piazzolla's 900 is heavier than the previous face at the same
  nominal value; 800 holds the same optical presence.
- Display sizes are `clamp()`-based and respond to viewport. Body sizes are fixed.
- Body floor is 16px. Functional text never goes below 11px.
- Tracking: display `-0.012em` to `-0.015em`; spec labels `+1.2px` to `+2px`
  with uppercase. Piazzolla sets narrower than the previous face — do not
  re-tighten display tracking past `-0.02em`.
- `font-optical-sizing: auto` is on; Piazzolla's `opsz` axis handles display vs text.
- Editorial prose on dark surfaces takes one step more weight (450 vs 400).

### Measure

Prose stays in 45–75ch. Measured: manifesto 66ch, problem descriptions 74ch,
offer 46ch, booking 49ch. `.manifesto-content` is capped at `66ch` explicitly.

---

## Color

| Token | Value | Rule |
|---|---|---|
| `--ink` | `#0f0e0c` | Page text on paper; dark section backgrounds |
| `--paper` | `#f5f1e8` | Page background |
| `--paper-warm` | `#ede6d8` | Secondary surface |
| `--amber` | `#d97b29` | **Fills, rules and dots only.** Fails AA as text on every light surface |
| `--amber-text` | `#9c4f08` | Amber *as text* on paper / paper-warm / white |
| `--amber-soft` | `#f6c088` | Amber *as text* on ink / green |
| `--steel` | `#4a4a48` | Secondary text on paper only — fails on ink |
| `--green` | `#2a5d3a` | Lead-magnet section |
| `--on-ink` | `rgba(245,241,232,.78)` | Body text on ink |
| `--on-ink-quiet` | `rgba(245,241,232,.65)` | Metadata on ink |

**The rule that matters:** `--amber` is a fill, not a text color. Reaching for it on
text is how the page accumulated 17 contrast failures. Use `--amber-text` or
`--amber-soft` depending on the surface underneath.

Do not express secondary text as `opacity` on a colored parent — it compounds
invisibly. Use the `--on-ink*` tokens.

Verified: 0 WCAG AA failures at 390 / 768 / 1440.

---

## Icons

Authored inline SVG, `24×24` viewBox, `stroke-width: 1.5`, `currentColor`,
round caps and joins. No emoji, no icon font, no external library.
Decorative icons carry `aria-hidden="true"`.

---

## Motion

One `prefers-reduced-motion` block disables the lot. Transitions are colour and
transform only — never `width`, `height`, `padding` or `margin`.

---

## Layout

- Sections: `120px 80px` desktop, `20px` horizontal on mobile.
- Content max-width `1200px`; booking column `900px`.
- Fixed nav is transparent over the hero and becomes an opaque surface past 40px of
  scroll (`nav.is-scrolled`). It must never paint a translucent veil over the dark
  sections below.
- `scroll-padding-top: 96px` and `section[id] { scroll-margin-top: 96px }` keep
  anchor targets clear of the nav.
- Interactive targets are ≥44px; nothing functional below 24px.

---

## Section labels

There are none, and that is the decision. Sections are not announced — no
`01 — Manifiesto`, no eyebrow chip above the `h1`. Each section is introduced by its
own heading and nothing else.

Navigation names what the visitor is looking for, not what we call the section:
**Qué falla · Qué incluye · Cómo trabajamos · Guía gratuita**. Four entries, not
five — the manifesto is the first thing below the hero and does not need an index
entry.

If a label ever feels necessary, make it descriptive of the content. Do not
reintroduce numbering or a tracked-caps chip.

---

## Deliberate exceptions to the impeccable floor

These two fire on the detector and are kept on purpose. Do not "fix" them without
asking.

- **Oversized `h1`** (`oversized-h1`). Persuade surface; display type carries the
  voice. The primary CTA is still above the fold at 1440×900 — that is the constraint
  that matters, and it is checked.
- **Cream page background** (`cream-palette`). The brand's paper.

---

## Known gaps

Not design defects — missing inputs. Listed so nobody mistakes them for finished work.

- No social proof anywhere: no testimonial, no named box, no photo of Jon, no surname.
- No price for the ongoing (paid) service, no insurance/liability statement, no
  cancellation policy.
- No `aviso legal` and no `política de privacidad`, both of which the gift form's data
  collection requires in Spain.
