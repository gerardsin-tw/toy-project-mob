## ADDED Requirements

### Requirement: Dark mode toggle button
The UI SHALL display a toggle button fixed to the top-right corner of every page that allows the user to switch between light and dark visual themes.

#### Scenario: Toggle button is visible on index page
- **WHEN** the user opens the index page
- **THEN** a theme toggle button SHALL be visible in the top-right corner of the viewport

#### Scenario: Toggle button is visible on quiz page
- **WHEN** the user opens the quiz page
- **THEN** a theme toggle button SHALL be visible in the top-right corner of the viewport

#### Scenario: Activating dark mode
- **WHEN** the user clicks the toggle button while light mode is active
- **THEN** the page SHALL switch to the dark color scheme and the button label SHALL update to indicate light mode can be restored

#### Scenario: Activating light mode
- **WHEN** the user clicks the toggle button while dark mode is active
- **THEN** the page SHALL switch to the light color scheme and the button label SHALL update to indicate dark mode can be activated

### Requirement: Dark mode color scheme
The dark theme SHALL provide sufficient contrast for all interactive and textual elements.

#### Scenario: Dark background and text
- **WHEN** dark mode is active
- **THEN** the page background SHALL be dark (e.g. `#1a1a2e`) and body text SHALL be light (e.g. `#e0e0e0`)

#### Scenario: Dark card styling
- **WHEN** dark mode is active
- **THEN** question/card elements SHALL use a dark background (e.g. `#16213e`) with a dark border (e.g. `#444`)

### Requirement: Theme persistence via localStorage
The app SHALL persist the user's theme preference in `localStorage` under the key `theme` and restore it on every page load.

#### Scenario: Preference saved on toggle
- **WHEN** the user activates dark mode
- **THEN** `localStorage` SHALL contain `{ theme: 'dark' }`

#### Scenario: Preference restored on reload
- **WHEN** the user reloads the page after previously selecting dark mode
- **THEN** the page SHALL load in dark mode without the user needing to toggle again

#### Scenario: Preference restored on navigation between pages
- **WHEN** the user navigates from the index page to the quiz page (or vice versa)
- **THEN** the theme previously chosen SHALL be applied on the destination page
