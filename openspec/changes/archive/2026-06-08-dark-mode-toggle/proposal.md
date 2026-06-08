## Why

Users interact with the trivia quiz in varied lighting conditions, and the current light-only theme can cause eye strain in low-light environments. Adding a dark mode toggle gives users control over the visual theme and improves overall comfort and accessibility.

## What Changes

- Add a toggle button in the top-right corner of both `index.html` and `quiz.html` to switch between light and dark themes
- Define dark mode CSS variables/overrides for background, text, card, and border colors
- Persist the user's theme preference in `localStorage` so it is restored on page load

## Capabilities

### New Capabilities
- `dark-mode-toggle`: A UI toggle in the top-right corner of all pages that switches between light and dark themes and persists the preference across page loads via localStorage

### Modified Capabilities
<!-- No existing spec-level requirements are changing -->

## Impact

- `src/app/templates/index.html`: add toggle button, dark mode CSS, and JS logic
- `src/app/templates/quiz.html`: add toggle button, dark mode CSS, and JS logic
- No backend changes required
- No new dependencies
