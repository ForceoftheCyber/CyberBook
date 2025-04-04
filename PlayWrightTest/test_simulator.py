import re
import time
from playwright.sync_api import Page, expect, sync_playwright
import pytest


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

# Tests the simulator with wrong parameters (this has to be updated when Hans provides)


def test_wrong_simulator_parameters(page: Page):
    page.set_default_navigation_timeout(70000)
    page.set_default_timeout(70000)
    page.goto(
        "http://localhost:8000/chapters/simulator/maglev_dynamical_system_simulation.html")

    # Set Kp slider value to 20 which equals style transform translate(-1000%)
    # slider1 = page.locator('div.noUi-handle noUi-handle-lower')
    #time.sleep(70)
    slider1 = page.locator('div.noUi-handle.noUi-handle-lower').nth(0)
    slider2 = page.locator('div.noUi-handle.noUi-handle-lower').nth(1)

    #slider1 = page.locator('span.section-number').nth(0)

    expect(slider1).to_be_visible(timeout=70000)
    expect(slider2).to_be_visible(timeout=70000)
    #expect(slider1).to_be_visible()

    #slider1.evaluate()

    slider1.evaluate("""(element) => {
    element.setAttribute('aria-valuetext', '20');
    }""")
    slider2.evaluate("""(element) => {
    element.setAttribute('aria-valuetext', '10');
    }""")

    actual_value = slider1.evaluate("element => element.getAttribute('aria-valuetext')")
    expected_value = '20'  # The value you expect
    assert actual_value == expected_value, f"Expected aria-valuetext to be {expected_value}, but got {actual_value}"

    actual_value = slider2.evaluate("element => element.getAttribute('aria-valuetext')")
    expected_value = '10'  # The value you expect
    assert actual_value == expected_value, f"Expected aria-valuetext to be {expected_value}, but got {actual_value}"
    print(actual_value)

    #Press assert button should fail
    page.get_by_role("button", name="Evaluate").click()


    time.sleep(20)

def test_valid_simulator_parameters(page: Page):
    page.goto(
        "http://localhost:8000/chapters/simulator/maglev_dynamical_system_simulation.html")
    
    slider1 = page.locator('div.noUi-handle.noUi-handle-lower').nth(0)
    slider2 = page.locator('div.noUi-handle.noUi-handle-lower').nth(1)

    