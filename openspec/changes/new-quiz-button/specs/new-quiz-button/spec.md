## ADDED Requirements

### Requirement: New Quiz button
The quiz page SHALL display a "New Quiz" button that loads a fresh set of trivia questions using the same category, type, and amount parameters as the current quiz session.

#### Scenario: Button is visible on quiz page
- **WHEN** the user is on the quiz page
- **THEN** a "New Quiz" button SHALL be visible alongside the "Check Answers" button

#### Scenario: Clicking New Quiz loads fresh questions
- **WHEN** the user clicks the "New Quiz" button
- **THEN** the quiz SHALL fetch and render a new set of questions using the same category, type, and amount from the current URL

#### Scenario: Clicking New Quiz resets grading state
- **WHEN** the user clicks the "New Quiz" button after having graded a quiz
- **THEN** the score result text SHALL be cleared and any correct/incorrect highlights on question cards SHALL be removed

#### Scenario: Clicking New Quiz removes fireworks overlay
- **WHEN** the user clicks the "New Quiz" button while a fireworks overlay is visible
- **THEN** the fireworks overlay SHALL be removed before the new questions are rendered
