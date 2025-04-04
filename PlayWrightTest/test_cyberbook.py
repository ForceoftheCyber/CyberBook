import re
import time
from playwright.sync_api import Page, expect, sync_playwright
import pytest
import subprocess

# starts Teachbooks on localhost port 8000


@pytest.fixture(scope="session", autouse=True)
def run_server():
    server = subprocess.Popen(
        ["python", "-m", "http.server", "8000", "--directory", "book/_build/html"])
    print("Server started")

    yield

    server.terminate()
    server.wait()
    print("Server stopped")


# Uncomment this if you want visual feedback in browser, this significantly slows down the testing
# even if run in headless mode

@pytest.fixture
def page(slow_mo: int = 500):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=slow_mo)
        context = browser.new_context()
        _page = context.new_page()
        yield _page
        _page.close()
        context.close()
        browser.close()


def test_has_title(page: Page):
    page.goto("http://localhost:8000/chapters/pid_control/intro.html")
    expect(page).to_have_title(re.compile("P"))

    # This is just to pause it a bit at the end so you get some time to view
    page.evaluate("() => Promise.resolve()")

# Tests going to a chapter from the intro chapter


def test_aligning_expectation_from_pid_intro(page: Page):
    page.goto("http://localhost:8000/chapters/pid_control/intro.html")

    page.get_by_role(
        "link", name="1.2. Checking Prerequisite Knowledge").click()
    expect(page.get_by_role(
        "heading", name="Checking Prerequisite Knowledge")).to_be_visible()

    page.evaluate("() => Promise.resolve()")

# Tests answering the first option in the two questions, in this case you will get a wrong result


def test_answering_wrong(page: Page):
    page.goto(
        "http://localhost:8000/chapters/pid_control/checking_prerequisite_knowledge.html")

    page.get_by_role("button", name="Proportional component").click()
    page.get_by_role("button", name="Increased steady-state error").click()
    time.sleep(1)
    page.get_by_role("button", name="Check answer").click()
    time.sleep(2)

    # Finds and checks for wrong questions
    expect(page.locator(
        'pre:has-text("Wrong! No questions are correctly answered")')).to_be_visible()
    expect(page.locator('pre:has-text("Wrong answer!")').nth(0)).to_be_visible()
    expect(page.locator('pre:has-text("Wrong answer!")').nth(1)).to_be_visible()

    # This is going to be changed shortly as of time of writing so can't check it now
    # expect(page.locator(
    #   'strong:has-text("[Will expand on wrong answer]")')).to_be_visible()

# Test button try again with new questions (Theese test do not really check everything, just checks
# that check answer reapears)


def test_try_again_with_new_questions(page: Page):
    page.goto(
        "http://localhost:8000/chapters/pid_control/checking_prerequisite_knowledge.html")
    page.get_by_role("button", name="Proportional component").click()
    page.get_by_role("button", name="Increased steady-state error").click()
    page.get_by_role("button", name="Check answer").click()

    page.get_by_role("button", name="Try again with new questions").click()
    page.get_by_role("button", name="Check answer").click()
    time.sleep(2)

# Test answering correct


def test_answering_correct(page: Page):
    page.goto(
        "http://localhost:8000/chapters/pid_control/checking_prerequisite_knowledge.html")
    page.get_by_role("button", name="Increased system oscillations").click()
    page.get_by_role("button", name="Integral component").click()
    page.get_by_role("button", name="Check answer").click()

    expect(page.locator(
        'pre:has-text("All questions are correctly answered! You may now proceed.")')).to_be_visible()

    expect(page.locator('pre:has-text("Correct!")').nth(0)).to_be_visible()
    expect(page.locator('pre:has-text("Correct!")').nth(1)).to_be_visible()
