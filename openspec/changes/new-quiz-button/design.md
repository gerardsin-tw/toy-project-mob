## Context

The quiz page (`quiz.html`) loads questions by reading `category`, `type`, and `amount` from the URL query string and calling the `/trivia` API. After grading, users must manually navigate back to the index page to replay. The page has no shared JS modules or build step — all logic is inline.

## Goals / Non-Goals

**Goals:**
- Add a "New Quiz" button that re-fetches and re-renders questions using the same URL parameters
- Reset the grading state (scores, card highlights) before loading the new questions

**Non-Goals:**
- Changing the URL or navigating away from the quiz page
- Shuffling or deduplicating questions across quiz attempts
- Adding a "Back" button or any other navigation

## Decisions

### Re-invoke `loadQuiz()` rather than reloading the page

**Decision**: The "New Quiz" button calls the existing `loadQuiz()` function directly and resets UI state (clears result text, removes grade highlights).

**Rationale**: `loadQuiz()` already handles all fetching and rendering. Re-using it avoids duplicating logic. A full page reload (`window.location.reload()`) would also work but would re-trigger the theme-restore script and briefly flash, and is less controllable (e.g., can't clear the score first).

**Alternatives considered**:
- `window.location.reload()`: simpler but less clean; cannot sequence UI resets before the reload.
- Navigating back to index and auto-submitting: over-engineered; breaks the single-page quiz flow.

### Button placement

**Decision**: Place the "New Quiz" button adjacent to the existing "Check Answers" button.

**Rationale**: Both actions relate to the current quiz state and belong together visually.

## Risks / Trade-offs

- **Stale fireworks overlay** → If the fireworks GIF is still visible when "New Quiz" is clicked, it must be removed. Mitigation: clear any `.firework` element before calling `loadQuiz()`.
- **Double-fetch on rapid clicks** → No debounce is implemented. Mitigation: acceptable at this scale; can be addressed in a follow-up.
