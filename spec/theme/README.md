# Global Theme — Sociognosis Design System

> The shared visual language for every Sociognosis surface. It is a dark, scholarly, *"Oxford Common Room"* aesthetic: a deep indigo-black canvas, warm gilt (copper) bookbinding edges, parchment text, and a muted Senior Common Room palette for categorical color.

**Source of truth:** [`docs/idx/index.html`](../../docs/idx/index.html) (`:root` token block, lines ~13–65). `docs/idx/edit.html` shares the same tokens; both must stay in sync. Any new page or component **must** derive its styling from the tokens below, never from one-off colors.

## Design Principles

1. **Dark scholarly canvas.** Pure deep indigo-black backgrounds, depth conveyed by shadow rather than glow. No textures, grids, or busy gradients on the canvas itself.
2. **Gilt bookbinding.** Copper is the signature accent — reserved for selection, focus, eyebrows, active states, and fine 1–2px "gilt edges". Use it sparingly; it loses meaning if everything is copper.
3. **Three voices of type.** *Cormorant Garamond* italic speaks (titles, eyebrows, names); *Inter* explains (body, descriptions); *JetBrains Mono* measures (labels, data, metadata).
4. **Matte over neon.** Categorical colors are muted, low-saturation ("velvet buttons on dark wool"). Never use pure-saturated hues.
5. **Progressive disclosure.** Dense information, revealed by zoom band and interaction — labels, edges, and silhouettes appear only when contextually meaningful.
6. **Quiet motion.** `cubic-bezier(.22,1,.36,1)` easing, ~300–600ms for structural transitions. Respect `prefers-reduced-motion`.

## Color Tokens

### Canvas & surfaces

| Token | Value | Usage |
| --- | --- | --- |
| `--bg-void` | `#0b0e14` | Primary canvas / page background. Pure deep indigo-black. |
| `--bg-surface` | `#11151e` | Sidebar, detail panel, modal header top of gradient. |
| `--bg-card` | `#161b26` | Cards, raised containers. |
| `--bg-elevated` | `#1d2330` | Floating controls, elevated menus. Glass base (`rgba(31,35,45,0.85)` + `backdrop-filter: blur(20px)`). |
| `--bg-hover` | `rgba(255,255,255,0.04)` | Hover wash on rows/items. |

Panels gradient *downward* into the void: `linear-gradient(180deg, var(--bg-surface) 0%, var(--bg-void) 100%)`.

### Signature accents

| Token | Value | Usage |
| --- | --- | --- |
| `--gilt` | `#C4B998` | The "fine bookbinding" gilt edge. **Selected-node ring**, gilt underlines. |
| `--parchment` | `#D6D1C4` | Warm off-white for canvas labels and gilt selection text. |
| `--thread` | `#4a4a4a` | Faint warm graphite for edges/threads (graphite on dark paper). |

### Text hierarchy

| Token | Value | Usage |
| --- | --- | --- |
| `--text-primary` | `#f4f3f1` | Headings, primary content. |
| `--text-secondary` | `#a8a5b0` | Body, descriptions, default labels. |
| `--text-muted` | `#9290aa` | Metadata, mono captions, eyebrows. |
| `--text-ghost` | `#82809a` | Placeholders, tertiary info, arrows. |

### Accent system (refined)

| Token | Hex | Semantic role |
| --- | --- | --- |
| `--accent-copper` | `#c9956c` | **Primary accent.** Focus, selection, active, eyebrows, gilt edges. (Legacy alias: `--accent-gold`.) |
| `--accent-copper-light` | `#dbb08a` | Hover/lightened copper; emphasized values. |
| `--accent-sage` | `#7ba388` | **Success / confidence / positive.** |
| `--accent-plum` | `#9b7eb0` | **Layer / taxonomic** badges, kv-keys. |
| `--accent-rose` | `#c47d8a` | **Destructive / close-hover / warning / missing target.** |
| `--accent-amber` | `#d4a857` | Caution / attention. |
| `--accent-steel` | `#6b8caa` | Neutral informative. |
| `--accent-cyan` | `#4dd4c4` | **External links** (with `1px` underline at 30% alpha). |

Accent usage at low alpha is idiomatic — e.g. focus ring `0 0 0 3px rgba(201,149,108,0.1)`, group dividers `rgba(201,149,108,0.08)`, scrollbar thumbs `rgba(201,149,108,0.16)`, the time-fill at `0.9` with a `0 0 10px rgba(201,149,108,0.2)` glow.

### Borders

| Token | Value | Usage |
| --- | --- | --- |
| `--border-subtle` | `rgba(255,255,255,0.05)` | Inner section dividers, card edges. |
| `--border-medium` | `rgba(255,255,255,0.08)` | Panel borders, floating controls. |
| `--border-strong` | `rgba(255,255,255,0.12)` | Hover borders, prominent boundaries. |

### Categorical palette — "Senior Common Room"

Twelve muted scholarly tones (~10–25% saturation, 20–35% lightness). Categories map **deterministically** to these via an FNV-1a hash of the category name (see `categoryColorIndex` in `docs/idx/index.html`), so colors are stable across reloads and decoupled from the fixed category list.

| # | Hex | Name | Visual reference |
| --- | --- | --- | --- |
| 1 | `#3D5A5C` | Faded teal | Old copper roofs |
| 2 | `#704E4A` | Dusty burgundy | Burgundy leather |
| 3 | `#4A4B5C` | Deep slate blue | Academic gown |
| 4 | `#5C5A3D` | Olive | Aged parchment |
| 5 | `#4E4A60` | Muted plum | Plum |
| 6 | `#5C4E3D` | Warm dark oak | Oak |
| 7 | `#3D4E5C` | Desaturated navy | Navy |
| 8 | `#4E5C4A` | Moss | Moss |
| 9 | `#4A4A4E` | Charcoal | **Fallback** (`FALLBACK_COLOR`) |
| 10 | `#5C574E` | Taupe | Taupe |
| 11 | `#3D5C57` | Petrol | Petrol |
| 12 | `#5C4E54` | Muted maroon | Maroon |

When a **confidence gradient** lens is active, a node's category color is desaturated toward luminance-gray proportionally to `(1 − confidence)` (see `blendWithConfidence`). Low-confidence nodes also *ghost* (opacity 0.06–0.15) under the observability lens.

## Typography

### Type families

| Token | Family | Role |
| --- | --- | --- |
| `--font-display` | `'Cormorant Garamond', serif` | Titles, eyebrows, names, section heads. **Always italic, light weight (300–400).** |
| `--font-body` | `'Inter', sans-serif` | Body copy, descriptions, UI labels. Weights 300/400/500/600. |
| `--font-mono` | `'JetBrains Mono', monospace` | Data, metrics, metadata captions, badges, table heads. Weights 300/400/500. |

Fonts load from Google Fonts with `display=swap`. Render with `-webkit-font-smoothing: antialiased`, `text-rendering: optimizeLegibility`, body `letter-spacing: 0.015em`.

### Type scale (derived from actual usage)

| Role | Family / style | Size | Notes |
| --- | --- | --- | --- |
| Page title (`.sb-title`) | display italic 300 | `1.9rem` | Gilt underline: `linear-gradient(90deg, copper, transparent) bottom left / 60% 1px`. |
| Detail title (`.dp-title`) | display italic 400 | `1.6rem` | `line-height: 1.15`. |
| Modal title (`.stats-title`) | display italic 300 | `1.5rem` | |
| Section title (`.dp-section-title`, `.stats-section-title`) | display italic 400 | `0.82rem` | `▾` chevron right-aligned, hover → copper-light. |
| Eyebrow (`.sb-eyebrow`, `.stats-eyebrow`) | display italic 400 | `0.7rem` | Copper at 0.75 alpha, `letter-spacing: 0.06em`. |
| Body (`.dp-field-value`) | body 400 | `0.78rem` | `line-height: 1.6`. |
| Caption / description | body 400 | `0.68rem` | `line-height: 1.5–1.55`. |
| Mono data (`.stats-card-value`) | mono 500 | `1rem` | copper-light. |
| Meta label (mono caption) | mono 400 | `0.5–0.58rem` | `text-transform: uppercase; letter-spacing: 0.06–0.12em`. |

**Rule:** mono captions are uppercase with wide tracking (`0.06–0.12em`); display titles are italic; never set Inter italic.

## Geometry

### Radii

| Token | Value | Usage |
| --- | --- | --- |
| `--radius-sm` | `5px` | Small chips, tags, toggles, buttons. |
| `--radius-md` | `8px` | Inputs, controls, tooltips, dropdowns. |
| `--radius-lg` | `12px` | Modals, large containers. |

Tooltip convention: `border-radius: 0 var(--radius-md) var(--radius-md) var(--radius-md)` (square top-left corner, as if pinned).

### Shadows (depth, not glow)

| Token | Value |
| --- | --- |
| `--shadow-sm` | `0 2px 8px rgba(0,0,0,0.15)` |
| `--shadow-md` | `0 8px 24px rgba(0,0,0,0.2)` |
| `--shadow-lg` | `0 16px 48px rgba(0,0,0,0.25)` |

Signature "copper bleed" shadow on elevated containers (tooltips, dropdowns, search, modals):

```css
box-shadow: var(--shadow-lg), -12px 0 32px -16px rgba(201,149,108,0.45);
border-left: 2px solid var(--accent-copper);
```

## Layout

- **App shell:** CSS grid `320px 1fr 0` (sidebar | canvas | detail), height `100vh`, `overflow: hidden`. Columns animate via `grid-template-columns` over `.5s cubic-bezier(.22,1,.36,1)`:
  - `.sidebar-collapsed` → `0 1fr 0`
  - `.detail-open` → `320px 1fr 400px`
  - both → `0 1fr 400px`
- **Canvas:** `main.canvas-area` is `position: relative; overflow: hidden` over `--bg-void`. A `::after` radial vignette (`radial-gradient(ellipse at 50% 50%, transparent 45%, rgba(0,0,0,0.55) 100%)`) darkens the edges to draw the eye inward.
- **Panels:** side-gradient surfaces with `1px var(--border-medium)` divider to the canvas. Padding rhythm `22–28px`.

## Selection & Scrollbars

- **Text selection (gilt):** `::selection { background: rgba(201,149,108,0.28); color: var(--parchment); }`
- **Scrollbars:** thin (`scrollbar-width: thin`), thumb `rgba(255,255,255,0.08)` → hover `rgba(201,149,108,0.4)`, 6–8px wide, transparent track. Panel-specific thumbs use `rgba(201,149,108,0.16)`.

## Components

### Controls & buttons
- Floating canvas controls: `38×38px`, `var(--radius-md)`, glass (`rgba(31,35,45,0.85)` + `blur(20px)`), `1px var(--border-medium)`. Hover → copper-light text, copper-tinted border, `-1px` lift, `--shadow-md`.
- Primary buttons: `linear-gradient(135deg, copper, #b8855d)`.
- Close/dismissive buttons: muted `×`, hover → rose on `rgba(196,125,138,0.08)`.

### Inputs
- `.search-box`: `rgba(18,20,26,0.9)`, `1px var(--border-medium)`, `border-radius: 6px`, inset shadow `0 1px 2px rgba(0,0,0,0.22)`. Placeholder: italic, `--text-ghost`. Focus: copper border + `0 0 0 3px rgba(201,149,108,0.1)`.

### Toggles / checkboxes
- `12×12px` checkmark, `1px solid rgba(255,255,255,0.18)`. Checked: copper-tinted (`border rgba(201,149,108,0.6)`, `bg rgba(201,149,108,0.12)`) with a centered 3px copper dot.

### Badges & chips
- `.dp-badge`: pill (`border-radius: 10px`), mono `0.56rem`, key uppercase muted / val colored. Layer val = plum, confidence val = sage.
- `.dp-tag`: `3px` radius, copper-tinted (`rgba(201,149,108,0.06)` on `0.12` border).

### Cards / event blocks
- `rgba(0,0,0,0.15–0.2)` on `1px var(--border-subtle)`. Events get a `2px solid rgba(201,149,108,0.3)` left rule. Hover lifts and copper-tints the border.

### Modals & overlays
- Overlay: `rgba(11,14,20,0.7)` + `blur(4px)`, fade `.3s`.
- Modal: top-gradient surface, `1px var(--border-medium)`, **`2px solid var(--accent-copper)` left border**, `--radius-lg`, copper bleed shadow. Enter: `translate(-50%,-48%) scale(.96)` → `translate(-50%,-50%) scale(1)` over `.3s cubic-bezier(.22,1,.36,1)`.

### Tooltips
- Glass `rgba(31,35,45,0.98)` + `blur(20px)`, `2px solid var(--accent-copper)` left, `260px` width, `padding 14px 16px`. Header: category dot + mono caption; title in display italic; meta row separated by `1px solid rgba(255,255,255,0.08)`.

### Graph rendering (deck.gl / socio-graph)
- Layered pipeline: **(1) community silhouettes → (2) edges → (3) nodes → (4) labels**.
- Nodes are matte velvet fills with drop shadows; **selected ring** is `2px #C4B998` (gilt), hover ring is `1px rgba(255,255,255,0.25)`.
- Edges are graphite threads (`#4a4a4a`) at weight-proportional alpha (0.1–0.3); incident edges adopt the focused node's category tint at 0.6.
- Labels: parchment (`#D6D1C4`) with a `#0b0e14` mask shadow (blur 4) — readability by shadow, not glow. Tier + zoom band gate visibility (always/meso/micro).
- Semantic zoom bands: **macro** (`viewportCoverage > 0.7`), **meso** (`0.2–0.7`), **micro** (`< 0.2`).

## Motion

| Transition | Duration / easing |
| --- | --- |
| Panel / sidebar / detail | `0.5s cubic-bezier(.22,1,.36,1)` |
| Modal open | `0.3s cubic-bezier(.22,1,.36,1)` (opacity + transform) |
| Hover lifts / colors | `0.2–0.3s ease` |
| Camera tween (fit/fly-to) | `600ms`, cubic-bezier ease (custom in `tweenCamera`) |
| Label fade | per-frame lerp `cur += (target − cur) * 0.15` |
| Loader dots | `1.4s ease-in-out` pulse, staggered `0.16s` |

All motion collapses to `0.01ms` under `@media (prefers-reduced-motion: reduce)`.

## Accessibility

- **Contrast:** `--text-primary` (#f4f3f1) on `--bg-void` (#0b0e14) ≈ 17:1; `--text-secondary` (#a8a5b0) ≈ 7:1. Both exceed WCAG AAA. Avoid `--text-muted`/`--text-ghost` for body copy.
- **Color-independence:** category membership is also conveyed by labels and legend text, never by color alone. Confidence uses opacity/ghosting in addition to desaturation.
- **Focus:** visible `2px solid var(--accent-copper)` outline (or the 3px 0.1-alpha ring) on all interactive elements.
- **ARIA:** detail panel is `aria-live="polite"`; modals are `role="dialog"` with `aria-label`; icon-only buttons carry `aria-label` and `title`.
- **Keyboard:** `F` fits view, `S` opens stats; canvas supports pan/zoom; tab order follows the visual order.

## Canonical token block

Copy verbatim into any new page's `:root`. This is the single source; do not introduce variants.

```css
:root {
  --bg-void: #0b0e14;
  --bg-surface: #11151e;
  --bg-card: #161b26;
  --bg-elevated: #1d2330;
  --bg-hover: rgba(255, 255, 255, 0.04);

  --gilt: #C4B998;
  --parchment: #D6D1C4;
  --thread: #4a4a4a;

  --text-primary: #f4f3f1;
  --text-secondary: #a8a5b0;
  --text-muted: #9290aa;
  --text-ghost: #82809a;

  --accent-copper: #c9956c;
  --accent-copper-light: #dbb08a;
  --accent-sage: #7ba388;
  --accent-plum: #9b7eb0;
  --accent-rose: #c47d8a;
  --accent-amber: #d4a857;
  --accent-steel: #6b8caa;
  --accent-cyan: #4dd4c4;
  --accent-gold: #c9956c; /* legacy alias for --accent-copper */

  --border-subtle: rgba(255, 255, 255, 0.05);
  --border-medium: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(255, 255, 255, 0.12);

  --font-display: 'Cormorant Garamond', serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 5px;
  --radius-md: 8px;
  --radius-lg: 12px;

  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.15);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.2);
  --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.25);
}
```

Categorical palette (JS array, see `COMMUNITY_COLORS` in `docs/idx/index.html`):

```js
const COMMUNITY_COLORS = [
  '#3D5A5C', '#704E4A', '#4A4B5C', '#5C5A3D', '#4E4A60', '#5C4E3D',
  '#3D4E5C', '#4E5C4A', '#4A4A4E', '#5C574E', '#3D5C57', '#5C4E54'
];
const FALLBACK_COLOR = COMMUNITY_COLORS[8]; // charcoal
```

## Implementation rules

1. **Single source of truth.** The canonical `:root` above is the only palette. Do not hardcode hex values in components — always reference a token. New tokens are added here first, with a documented semantic role.
2. **Copper is rationed.** Reserve `--accent-copper` for focus, selection, active, eyebrows, and gilt edges. Use sage/plum/rose/cyan for their semantic roles. Do not copper-tint arbitrary decoration.
3. **Category color is computed, not chosen.** Always derive categorical color via the `categoryColorIndex` hash → `COMMUNITY_COLORS` lookup. Never hand-assign category colors.
4. **Depth by shadow, not glow.** Matte velvet nodes; graphite threads; dark mask shadows behind labels. The only permitted "glow" is the copper time-fill and the copper-bleed box-shadow on elevated containers.
5. **Keep pages in sync.** `index.html` and `edit.html` render identically by importing the shared renderer (`docs/idx/vendor/socio-graph.js`) and the same `:root`. Any token change must be applied to **both** HTML files (and any future page) simultaneously.
6. **Verify contrast.** Before merging a new text/background pairing, confirm ≥ 4.5:1 (AA) for body, ≥ 3:1 for large display text.
