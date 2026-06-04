import { test, expect } from "@playwright/test";

test("Start Quiz button redirects to quiz page", async ({ page }) => {
  // 1. Open homepage
  await page.goto("http://localhost:8000/");

  // 2. Click the button
  await page.click("#redirectBtn");

  // 3. Check URL changed
  await expect(page).toHaveURL("http://localhost:8000/quiz");
});