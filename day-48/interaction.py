from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/best/Developer/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#-------------------------------------------- EXAMPLE CODE ----------------------------#
# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

#-------------------------------------------- SIGN UP CODE CHALLENGE ----------------------------#
driver.get("http://secure-retreat-92358.herokuapp.com/")

fn_input = driver.find_element_by_name("fName")
fn_input.send_keys("Best")
ln_input = driver.find_element_by_name("lName")
ln_input.send_keys("Dech")
mail_input = driver.find_element_by_name("email")
mail_input.send_keys("test@test.com")

submit_btn = driver.find_element_by_css_selector("form button")
submit_btn.click()

driver.quit()
