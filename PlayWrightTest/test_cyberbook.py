import re
import time
from playwright.sync_api import Page, expect, sync_playwright
import pytest

#Test to find page title, this pretty much checks if you are able to access the page

#Uncomment this if you want visual feedback in browser, this significantly slows down the testing
#even if run in headless mode

@pytest.fixture
def page(slow_mo: int=1000):
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

    page.evaluate("() => Promise.resolve()") #This is just to pause it a bit at the end so you get some time to view

#Tests going to a chapter from the intro chapter
def test_aligning_expectation_from_pid_intro (page: Page):
    page.goto("http://localhost:8000/chapters/pid_control/intro.html")

    page.get_by_role("link", name="2.2. Checking Prerequisite Knowledge").click()
    expect(page.get_by_role("heading", name="2.2. Checking Prerequisite Knowledge")).to_be_visible()

    page.evaluate("() => Promise.resolve()")

#Tests answering the first option in the two questions, in this case you will get a wrong result
def test_answering_wrong (page: Page):
    page.goto("http://localhost:8000/chapters/pid_control/checking_prerequisite_knowledge.html")

    #page.get_by_role("button", value="0" class="")
    #button_selector = page.locator('button.widget-toggle-button[value="Proportional%20component"]')
    #button_selector.click()
    page.get_by_role("button", name="Proportional component").click()
    time.sleep(1)
