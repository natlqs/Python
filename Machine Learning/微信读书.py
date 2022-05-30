from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json, base64


def capture_full_screen(driver) :

    def send(ctrl, params):
        resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
        url = driver.command_executor._url + resource
        body = json.dumps({"cmd":ctrl, "params": params})
        response = driver.command_executor._request("POST", url, body)
        return response.get("value")

    def evaluate(script):
        response = send("Runtime.evaluate", {"returnByValue": True, "expression": script})
        return response["result"]["value"]

    metrics = evaluate(\
    "({" + \
      "width: Math.max(window.innerWidth, document.body.scrollWidth, document.documentElement.scrollWidth)|0," + \
      "height: Math.max(innerHeight, document.body.scrollHeight, document.documentElement.scrollHeight)|0," + \
      "deviceScaleFactor: window.devicePixelRatio || 1," + \
      "mobile: typeof window.orientation !== 'undefined'" + \
    "})")
    send("Emulation.setDeviceMetricsOverride", metrics)
    screenshot = send("Page.captureScreenshot", {"format": "png", "fromSurface": True})
    send("Emulation.clearDeviceMetricsOverride", {})

    return base64.b64decode(screenshot["data"])


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    # driver.get('https://weread.qq.com/web/reader/f4e32d4071e1ec54f4e18f9kc81322c012c81e728d9d180')      # Python大数据分析与机器学习商业案例实战
    driver.get('https://weread.qq.com/web/reader/79e326107190b92779e78f0kc81322c012c81e728d9d180')         # Python金融大数据挖掘与分析全流程详解
    driver.find_element_by_xpath('//*[@id="routerView"]/div[2]/button[3]').click()
    time.sleep(0.5)
    screenshot = capture_full_screen(driver)
    with open(r"C:\01_Data\CODE\Python\Machine Learning\Python金融大数据挖掘与分析全流程详解\0.png", 'wb') as f:
    # with open(r"C:\01_Data\CODE\Python\Machine Learning\Python大数据分析与机器学习商业案例实战\0.png", 'wb') as f:
        f.write(screenshot)
    driver.find_element(By.XPATH, '//*[@id="routerView"]/div[1]/div[7]/div/button').click()
    # for i in range(1, 3):
    i = 1
    while True:
        try:
            time.sleep(2.5)
            screenshot = capture_full_screen(driver)
            with open(r"C:\01_Data\CODE\Python\Machine Learning\Python金融大数据挖掘与分析全流程详解\{}.png".format(i), 'wb') as f:
                f.write(screenshot)
            i = i + 1
            driver.find_element(By.XPATH, '//*[@id="routerView"]/div[1]/div[5]/div/button').click()
        except:
            break
    driver.quit()