## Why

After completing a quiz, users currently have no way to immediately start a fresh quiz with the same category, type, and number of questions. They must navigate back to the index page and re-select all parameters. A "New Quiz" button on the results area would reduce friction and encourage replaying.

## What Changes

- Add a "New Quiz" button to `quiz.html` that reloads a fresh set of questions using the same URL parameters (category, type, amount) already present in the page URL
- The button should be shown alongside the existing "Check Answers" button

## Capabilities

### New Capabilities
- `new-quiz-button`: A button on the quiz page that fetches and renders a new set of trivia questions using the same query parameters as the current quiz session

### Modified Capabilities
<!-- No existing spec-level requirements are changing -->

## Impact

- `src/app/templates/quiz.html`: add "New Quiz" button and JS handler to re-invoke `loadQuiz()`
- No backend changes required
- No new dependencies
