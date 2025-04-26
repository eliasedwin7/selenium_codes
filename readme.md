# Repo for selenium code

## 📘 Selenium WebDriver Commands Cheat Sheet
| **Operation**                        | **Command**                           | **Method/Property** | **Description**                                                                 |
|-------------------------------------|----------------------------------------|----------------------|---------------------------------------------------------------------------------|
| Navigate to URL                     | driver.get("https://example.com")      | Method               | Opens the URL in the browser session                                           |
| Get Current URL                     | driver.current_url                     | Property             | Returns the current URL from the browser's address bar                         |
| Back                                | driver.back()                          | Method               | Simulates the browser's back button                                            |
| Forward                             | driver.forward()                       | Method               | Simulates the browser's forward button                                         |
| Refresh Page                        | driver.refresh()                       | Method               | Reloads the current page                                                       |
| Get Page Title                      | driver.title                           | Property             | Returns the title of the current page                                          |
| Maximize Window                     | driver.maximize_window()               | Method               | Enlarges window to fill the screen (not full screen)                           |
| Minimize Window                     | driver.minimize_window()               | Method               | Minimizes the current window                                                   |
| Full Screen Window                  | driver.fullscreen_window()             | Method               | Fills screen like F11 key                                                      |
| Close Current Window                | driver.close()                         | Method               | Closes the current tab/window                                                  |
| Quit Browser                        | driver.quit()                          | Method               | Closes all tabs and ends the WebDriver session                                 |
| Get Page Source                     | driver.page_source                     | Property             | Returns HTML source of the page                                                |
| Find Element by ID                  | driver.find_element(By.ID, "id")       | Method               | Locates a single element by ID                                                 |
| Find Elements by Class Name         | driver.find_elements(By.CLASS_NAME, "class") | Method         | Locates all matching elements by class name                                    |
| Send Text to Input Field            | element.send_keys("text")              | Method               | Sends keystrokes to input field                                                |
| Click on Element                    | element.click()                        | Method               | Clicks the specified element                                                   |
| Clear Input Field                   | element.clear()                        | Method               | Clears any existing text in the field                                          |
| Get Element Text                    | element.text                           | Property             | Gets the visible text of an element                                            |
| Get Element Attribute               | element.get_attribute("attribute")     | Method               | Returns the value of a specified attribute                                     |
| Take Screenshot                     | driver.save_screenshot("screenshot.png") | Method             | Captures screenshot of current browser window                                  |

In Selenium, when you interact with a WebElement, you can access various **properties** and **methods** to extract or manipulate information.


### 🔍 **Common Properties & Methods of a WebElement**

| **Property/Method**                  | **Type**     | **Description**                                                                 |
|-------------------------------------|--------------|---------------------------------------------------------------------------------|
| `element.text`                      | Property     | Gets the visible text inside the element                                        |
| `element.tag_name`                  | Property     | Returns the tag name (like `div`, `input`, `a`)                                |
| `element.size`                      | Property     | Returns the size of the element as a dict: `{'height':..., 'width':...}`       |
| `element.location`                  | Property     | Returns the X, Y coordinates of the element                                     |
| `element.is_displayed()`            | Method       | Returns `True` if the element is visible                                        |
| `element.is_enabled()`              | Method       | Returns `True` if the element is enabled (usable)                              |
| `element.is_selected()`             | Method       | Returns `True` if the element (checkbox/radio) is selected                      |
| `element.get_attribute("name")`     | Method       | Gets the value of the specified attribute (like `href`, `value`, etc.)         |
| `element.get_dom_attribute("name")` | Method       | Gets the raw DOM attribute (even if not reflected in HTML attribute)           |
| `element.get_property("name")`      | Method       | Gets the JavaScript DOM property (not always the same as HTML attribute)       |
| `element.screenshot("el.png")`      | Method       | Takes a screenshot of the specific element                                     |
| `element.rect`                      | Property     | Returns `{'height', 'width', 'x', 'y'}` of the element                         |
| `element.value_of_css_property("property")` | Method | Gets the value of a CSS property like `color`, `font-size`, `background-color` |



### 🎯 What is `Select`?

- It's a **special Selenium class** that helps you easily **interact with `<select>` dropdown menus**.
- You use `Select` **only** when you are dealing with `<select>` HTML tags (the classic dropdowns).
- It gives you clean methods like **select by visible text**, **select by index**, **select by value**.

---

### 🧪 Simple Example

Imagine this HTML:

```html
<select id="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
</select>
```

You can control it using:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.example.com")  # page with select box

dropdown = Select(driver.find_element(By.ID, "cars"))

dropdown.select_by_visible_text("Saab")
# or
dropdown.select_by_value("mercedes")
# or
dropdown.select_by_index(0)  # 0 = Volvo
```

---

### 📋 Quick Cheat Sheet: `Select` Class Methods

| **Method**                       | **Description**                      |
|-----------------------------------|--------------------------------------|
| `select_by_visible_text("text")`  | Select option matching the visible text |
| `select_by_value("value")`        | Select option by the `value` attribute |
| `select_by_index(index)`          | Select option by its position (0-based) |
| `deselect_all()`                  | Deselect all options (only for multi-select) |
| `deselect_by_value("value")`      | Deselect option by value |
| `deselect_by_visible_text("text")`| Deselect option by visible text |
| `deselect_by_index(index)`        | Deselect option by index |
| `options`                         | Returns all options (WebElements) |
| `first_selected_option`           | Returns the first selected option |

---

### ⚡ In short:
- **`Select`** = Super handy helper when dealing with dropdowns
- **Without it**, you would need to manually click and select options using complex code.

---
