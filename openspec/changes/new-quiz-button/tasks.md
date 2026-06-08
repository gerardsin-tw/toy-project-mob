## 1. quiz.html – Button Markup

- [x] 1.1 Add a "New Quiz" button element to `quiz.html` alongside the existing "Check Answers" button

## 2. quiz.html – Reset and Reload Logic

- [x] 2.1 Add a `newQuiz()` function to `quiz.html` that clears the score result text
- [x] 2.2 In `newQuiz()`, remove any correct/incorrect highlight classes (`is-true`, `is-false`) from all question cards
- [x] 2.3 In `newQuiz()`, remove any fireworks overlay element if present
- [x] 2.4 In `newQuiz()`, call `loadQuiz()` to fetch and render fresh questions
- [x] 2.5 Wire the "New Quiz" button click event to call `newQuiz()`

## 3. Verification

- [ ] 3.1 Manually verify the "New Quiz" button is visible on the quiz page
- [ ] 3.2 Manually verify clicking "New Quiz" loads a different set of questions with the same parameters
- [ ] 3.3 Manually verify that score text and card highlights are cleared before the new questions render
- [ ] 3.4 Manually verify that clicking "New Quiz" while fireworks are showing removes the overlay
