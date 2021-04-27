from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\hema\PycharmProjects\Alert1\Tasks\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
ex_loc = r"C:\Users\hema\PycharmProjects\FrameWork\DemoLanguagexcel\New.xlsx"
w = openpyxl.load_workbook(ex_loc)
sheet = w.active
driver.get("http://demo.automationtesting.in/Register.html")
lang_id = driver.find_element(By.ID, "msdd")
lang_id.click()
lang = driver.find_elements(By.XPATH, "//li[@class='ng-scope']")
i = 1
for each_data in lang:
    t = each_data.text
    c = sheet.cell(i, 1)
    c.value = t
    w.save(ex_loc)
    i = i + 1
    print(t)
