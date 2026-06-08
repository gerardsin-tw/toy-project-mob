## Context

The trivia app is a single-backend FastAPI service that serves two Jinja2 HTML templates: `index.html` (category/type selection) and `quiz.html` (question display and grading). Both templates use inline `<style>` blocks with a hard-coded light theme (`background: #f9f7f1`, `color: #222`). There is no shared CSS file or JS module — all styling is self-contained per template. No build toolchain exists; changes are plain HTML/CSS/JS.

## Goals / Non-Goals

**Goals:**
- Add a toggle button to the top-right corner on both pages
- Switch the page between light and dark color schemes on click
- Persist the chosen theme across page loads using `localStorage`
- Keep implementation entirely client-side (no backend changes)

**Non-Goals:**
- Respecting `prefers-color-scheme` media query (out of scope for this change)
- Extracting styles into a shared CSS file or build step
- Supporting themes beyond light and dark

## Decisions

### CSS custom properties (variables) for theming

**Decision**: Use CSS custom properties defined on `:root` (light default) with a `.dark` class on `<body>` to override them.

**Rationale**: A class toggle on `<body>` is the simplest mechanism that requires no framework. Variables centralise colour values and make the dark overrides a concise block. Inlining them inside `<style>` keeps the zero-build-toolchain constraint.

**Alternatives considered**:
- Separate `<link>` stylesheet swap: more moving parts, no benefit at this scale.
- `data-theme` attribute: functionally equivalent; class is slightly more idiomatic for toggle patterns.

### `localStorage` for persistence

**Decision**: On page load, read `localStorage.getItem('theme')`. If `'dark'`, add `.dark` to `<body>` and set the toggle button label accordingly.

**Rationale**: `localStorage` is synchronous, universally available, and requires no server round-trip. Theme flicker on load is acceptable given the inline-script approach.

**Alternatives considered**:
- `sessionStorage`: does not persist across tabs/sessions; worse UX.
- Cookie: requires server-side reading to avoid flash; over-engineered for a static preference.

### Duplicate implementation per template

**Decision**: Reproduce the toggle button markup, CSS variables, and JS in both `index.html` and `quiz.html` independently.

**Rationale**: There is no shared template layer or build step. Extracting to a shared file would require refactoring the template architecture, which is out of scope. The duplicated code is small (~30 lines total per file).

## Risks / Trade-offs

- **Flash of unstyled content (FOUC)** → The theme-restore script runs inline before body paint, minimising but not eliminating flicker. Mitigation: place the script in `<head>` or as the first `<body>` child.
- **Duplication across templates** → If a third page is added later, the toggle must be copied again. Mitigation: document this in a follow-up task to extract to a shared JS/CSS file.

## Open Questions

- None — scope is fully defined for this change.
