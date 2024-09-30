import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageElements:

    def __init__(self, driver):
        self.driver = driver

    # -------------------------------- Header Elements ---------------------------------
    __company_logo = (By.XPATH, "//a[@aria-label = 'Home']")
    __personal_plan = (By.XPATH, "//a[contains(text(),'Personal')]")
    __business_plan = (By.CSS_SELECTOR, "div[class*= 'fxQDoB'] a:nth-child(2)")
    __send_money_header = (By.CSS_SELECTOR, "nav[class*='cEJNcP'] a:nth-child(1)")
    __converter = (By.CSS_SELECTOR, "nav[class*='cEJNcP'] a:nth-child(2)")
    __currency_api = (By.CSS_SELECTOR, "nav[class*='cEJNcP'] a:nth-child(3)")

    # Tools Dropdown
    __tools = (By.CSS_SELECTOR, "div[class*='hTiYc']:nth-child(4)")
    __currency_charts = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[1]/a/div[contains(text(), 'Currency Charts')]")
    __IBAN_calculator = (By.XPATH, "/html/body/div[1]/div/div[4]/header/div[1]/nav[1]/div[1]/div/div/div/div/ul[2]/li[1]/a")
    __rate_alerts_tools = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[2]/a/div[contains(text(), 'Rate Alerts')]")
    __apps = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[2]/a/div[contains(text(), 'Apps')]")
    __historical_currency_rates = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[3]/a/div[contains(text(), 'Historical Currency Rates')]")
    __more_tools = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[3]/a/div[contains(text(), 'More Tools')]")

    # Resources Dropdown
    __resources = (By.CSS_SELECTOR, "div[class*='hTiYc']:nth-child(5)")
    __help_center = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[1]/a/div[contains(text(), 'Help Center')]")
    __refer_a_friend = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[2]/a/div[contains(text(), 'Refer A Friend')]")
    __blog = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[3]/a/div[contains(text(), 'Blog')]")
    __money_transfer_tips = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[4]")
    __currency_encyclopedia = (By.CSS_SELECTOR, "ul[class*='gcURDw'] li:nth-child(5)")
    __currency_newsletter = (By.CSS_SELECTOR, "ul[class*='gcURDw'] li:nth-child(6)")
    __glossary = (By.CSS_SELECTOR, "ul[class*='gcURDw'] li:nth-child(7)")
    __more_resources = (By.XPATH, "//ul[@class='sc-79aa4c0a-7 gcURDw']/li[8]")
    # __resources = (By.CSS_SELECTOR, "div[class*='hTiYc']:nth-child(5)")
    # __help_center = (By.XPATH, "//div[@id='0.5240065019113589']/div/div/ul/li[1]/a")
    # __refer_a_friend = (By.XPATH, "//div[@id='0.5240065019113589']/div/div/ul/li[2]/a")
    # __blog = (By.XPATH, "//div[@id='0.5240065019113589']/div/div/ul/li[3]")
    # __money_transfer_tips = (By.XPATH, "//div[@id='0.5240065019113589']/div/div/ul/li[4]")
    # __currency_encyclopedia = (By.CSS_SELECTOR, "//div[@id='0.5240065019113589']/div/div/ul/li[5]")
    # __currency_newsletter = (By.CSS_SELECTOR, "//div[@id='0.5240065019113589']/div/div/ul/li[6]")
    # __glossary = (By.CSS_SELECTOR, "//div[@id='0.5240065019113589']/div/div/ul/li[7]")
    # __more_resources = (By.XPATH, "//div[@id='0.5240065019113589']/div/div/ul/li[1]")

    # Register Dropdown
    __register = (By.CSS_SELECTOR, "div[class*='hTiYc']:nth-child(2)")
    __money_transfer_register = (By.XPATH, "/html/body/div[1]/div/div[4]/header/div[1]/nav[2]/div/div[2]/div/div/div/div/ul/li[1]")
    __rate_alerts_register = (By.XPATH, "/html/body/div[1]/div/div[4]/header/div[1]/nav[2]/div/div[2]/div/div/div/div/ul/li[2]")

    # Sign-in Dropdown
    __sign_in = (By.CSS_SELECTOR, "div[class*='hTiYc']:nth-child(1)")
    # __money_transfer_signin = (By.XPATH, "//div[@id='0.9332815453324252']/div/div/ul/li[1]")
    __money_transfer_signin = (By.XPATH, "/html/body/div[1]/div/div[4]/header/div[1]/nav[2]/div/div[1]/div/div/div/div/ul/li[1]")
    # __rate_alerts_signin = (By.XPATH, "//div[@id='0.9332815453324252']/div/div/ul/li[2]")
    __rate_alerts_signin = (By.XPATH, "/html/body/div[1]/div/div[4]/header/div[1]/nav[2]/div/div[1]/div/div/div/div/ul/li[2]")

#     ---------------------------- Header Elements Getter -----------------------------

    def get_company_logo(self):
        return self.driver.find_element(*HomePageElements.__company_logo)

    def get_personal_plan(self):
        return self.driver.find_element(*HomePageElements.__personal_plan)

    def get_business_plan(self):
        return self.driver.find_element(*HomePageElements.__business_plan)

    def get_send_money_header(self):
        return self.driver.find_element(*HomePageElements.__send_money_header)

    def get_converter(self):
        return self.driver.find_element(*HomePageElements.__converter)

    def get_currency_api(self):
        return self.driver.find_element(*HomePageElements.__currency_api)

    def get_tools(self):
        return self.driver.find_element(*HomePageElements.__tools)

    def get_currency_chart(self):
        return self.driver.find_element(*HomePageElements.__currency_charts)

    def get_IBAN_calculator(self):
        return self.driver.find_element(*HomePageElements.__IBAN_calculator)

    def get_rate_alert_tools(self):
        return self.driver.find_element(*HomePageElements.__rate_alerts_tools)

    def get_apps(self):
        return self.driver.find_element(*HomePageElements.__apps)

    def get_historical_currency_rates(self):
        return self.driver.find_element(*HomePageElements.__historical_currency_rates)

    def get_more_tools(self):
        return self.driver.find_element(*HomePageElements.__more_tools)

    def get_resources(self):
        return self.driver.find_element(*HomePageElements.__resources)

    def get_help_center(self):
        return self.driver.find_element(*HomePageElements.__help_center)

    def get_refer_a_friend(self):
        return self.driver.find_element(*HomePageElements.__refer_a_friend)

    def get_blog(self):
        return self.driver.find_element(*HomePageElements.__blog)

    def get_money_transfer_tips(self):
        return self.driver.find_element(*HomePageElements.__money_transfer_tips)

    def get_currency_encyclopedia(self):
        return self.driver.find_element(*HomePageElements.__currency_encyclopedia)

    def get_currency_newsletter(self):
        return self.driver.find_element(*HomePageElements.__currency_newsletter)

    def get_glossary(self):
        return self.driver.find_element(*HomePageElements.__glossary)

    def get_more_resources(self):
        return self.driver.find_element(*HomePageElements.__more_resources)

    def get_register(self):
        return self.driver.find_element(*HomePageElements.__register)

    def get_money_transfer_register(self):
        return self.driver.find_element(*HomePageElements.__money_transfer_register)

    def get_rate_alerts_register(self):
        return self.driver.find_element(*HomePageElements.__rate_alerts_register)

    def get_sign_in(self):
        return self.driver.find_element(*HomePageElements.__sign_in)

    def get_money_transfer_signin(self):
        return self.driver.find_element(*HomePageElements.__money_transfer_signin)

    def get_rate_alert_signin(self):
        return self.driver.find_element(*HomePageElements.__rate_alerts_signin)

#   ---------------------------- Body Elements ----------------------------

    __convert_btn = (By.XPATH, "//span[contains(text(),'Convert')]")
    __send_btn = (By.XPATH, "//span[contains(text(),'Send')]")
    __charts_btn = (By.XPATH, "//span[contains(text(),'Charts')]")
    __alerts_btn = (By.XPATH, "//span[contains(text(),'Alerts')]")
    __amount_field = (By.ID, "amount")
    __from_field = (By.XPATH, "//div[@id='midmarketFromCurrency']/div/div/input")
    __to_field = (By.XPATH, "//div[@id='midmarketToCurrency']/div[2]/div/input")
    __from_country_to_choose = (By.XPATH, "//ul[@id='midmarketFromCurrency-listbox']/li[1]/div[2]")
    __to_country_to_choose = (By.XPATH, "//ul[@id='midmarketToCurrency-listbox']/li[1]/div[2]")
    __convert_the_currency = (By.CSS_SELECTOR, "div[class*='chRjcw'] button")
    __rate_of_from_country = (By.CSS_SELECTOR, "div.GwlFu p:nth-child(1)")
    __converted_amount = (By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[2]")
    __get_started = (By.XPATH, "//div[@class='sc-48fbfaf6-0 ibTeXs']/div[@class='text-center']/a")
    __body_send_money = (By.XPATH, "//a[contains(text(),'Send money')]")
    __body_view_charts = (By.XPATH, "//a[contains(text(),'View charts')]")
    __body_create_alert = (By.XPATH, "//a[contains(text(),'Create alert')]")



# ----------------------------- Body Getters ------------------------------

    def get_convert_btn(self):
        return self.driver.find_element(*HomePageElements.__convert_btn)

    def get_send_btn(self):
        return self.driver.find_element(*HomePageElements.__send_btn)

    def get_charts_btn(self):
        return self.driver.find_element(*HomePageElements.__charts_btn)

    def get_alerts_btn(self):
        return self.driver.find_element(*HomePageElements.__alerts_btn)

    def get_amount_field(self):
        return self.driver.find_element(*HomePageElements.__amount_field)

    def get_from_field(self):
        return self.driver.find_element(*HomePageElements.__from_field)

    def get_from_country(self):
        return self.driver.find_element(*HomePageElements.__from_country_to_choose)

    def get_to_field(self):
        return self.driver.find_element(*HomePageElements.__to_field)

    def get_to_country(self):
        return self.driver.find_element(*HomePageElements.__to_country_to_choose)

    def get_convert_the_currency(self):
        return self.driver.find_element(*HomePageElements.__convert_the_currency)

    def get_rate_of_from_country(self):
        return self.driver.find_element(*HomePageElements.__rate_of_from_country)

    def get_converted_amount(self):
        return self.driver.find_element(*HomePageElements.__converted_amount)

    def get_get_started(self):
        return self.driver.find_element(*HomePageElements.__get_started)

    def get_body_send_money(self):
        return self.driver.find_element(*HomePageElements.__body_send_money)

    def get_body_view_charts(self):
        return self.driver.find_element(*HomePageElements.__body_view_charts)

    def get_create_alerts(self):
        return self.driver.find_element(*HomePageElements.__body_create_alert)




#  ----------------------------- Footer Elements -----------------------------------

    # -------------------------- Currency Profiles --------------------------------

    __US_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[1]/a/span")
    __EUR_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[2]/a/span")
    __GBP_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[3]/a/span")
    __CAD_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[4]/a/span")
    __AUD_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[5]/a/span")
    __JPY_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[6]/a/span")
    __INR_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[7]/a/span")
    __NZD_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[8]/a/span")
    __CHF_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[9]/a/span")
    __ZAR_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[10]/a/span")
    __RUB_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[11]/a/span")
    __BGN_dollar = (By.XPATH, "/html/body/div[1]/div/div[4]/div[13]/section/div/div[12]/a/span")

    # ------------------------- Social Media --------------------------------

    __facebook = (By.CSS_SELECTOR, ".bwAEBa:nth-child(1)")
    __linkedin = (By.CSS_SELECTOR, ".bwAEBa:nth-child(3)")
    __instagram = (By.CSS_SELECTOR, ".bwAEBa:nth-child(4)")

    __send_money_online = (By.XPATH, "//a[contains(text(),'Send Money Online')]")
    __send_to_india = (By.XPATH, "//a[contains(text(),'Send Money to India')]")
    __send_to_pakistan = (By.XPATH, "//a[contains(text(),'Send Money to Pakistan')]")
    __send_to_mexico = (By.XPATH, "//a[contains(text(),'Send Money to Mexico')]")
    __send_to_japan = (By.XPATH, "//a[contains(text(),'Send Money to Japan')]")
    __send_to_uk = (By.XPATH, "//a[contains(text(),'Send Money to the UK')]")
    __send_to_canada = (By.XPATH, "//a[contains(text(),'Send Money to Canada')]")
    __send_to_australia = (By.XPATH, "//a[contains(text(),'Send Money to Australia')]")
    __send_to_new_zealand = (By.XPATH, "//a[contains(text(),'Send Money to New Zealand')]")
    __send_to_mobile_wallet = (By.XPATH, "//a[contains(text(),'Send Money to Mobile Wallet')]")
    __large_money_transfer = (By.XPATH, "//a[contains(text(),'Large Money Transfer')]")
    __security = (By.XPATH, "//a[contains(text(),'Security')]")
    __report_fraud = (By.XPATH, "//button[contains(text(),'Report fraud')]")
    __trustpilot_reviews = (By.XPATH, "//button[contains(text(),'Trustpilot Reviews')]")
    __popup_yes = (By.XPATH, "/html/body/div[5]/div/div/div/div/a")

    __business_payments = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(1) > a:nth-child(1)")
    __international_business_payments = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(2) > a:nth-child(1)")
    __global_business_payments = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(3) > a:nth-child(1)")
    __risk_management = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(4) > a:nth-child(1)")
    __resource_planning = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(5) > a:nth-child(1)")
    __api_integration = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(6) > a:nth-child(1)")
    __referral_program = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(7) > a:nth-child(1)")
    __mass_payment = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(2) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(8) > a:nth-child(1)")

    __money_transfer_and_currency_apps = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(3) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(1) > a:nth-child(1)")
    __android_money_transfer_app = (By.CSS_SELECTOR,  "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(3) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(2) > a:nth-child(1)")
    __ios_money_transfer_app = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(3) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(3) > a:nth-child(1)")

    __footer_blog = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(1) > a:nth-child(1)")
    __footer_currency_converter = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(2) > a:nth-child(1)")
    __footer_currency_charts = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(3) > a:nth-child(1)")
    __footer_historical_rates = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(4) > a:nth-child(1)")
    __footer_encyclopedia = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(5) > a:nth-child(1)")
    __footer_rate_alerts = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(6) > a:nth-child(1)")
    __footer_newsletters = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(7) > a:nth-child(1)")
    __footer_IBAN_cal = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(8) > a:nth-child(1)")
    __footer_glossary = (By.CSS_SELECTOR, "div[class ='sc-8a2e600-2 cLxVNS']:nth-child(4) ul[class='sc-8a2e600-4 khxdIo'] li:nth-child(9) > a:nth-child(1)")


    #  ------------------------------ Footer Getters --------------------------------

    def get_US_dollar(self):
        return self.driver.find_element(*HomePageElements.__US_dollar)

    def get_EUR_dollar(self):
        return self.driver.find_element(*HomePageElements.__EUR_dollar)

    def get_GBP_dollar(self):
        return self.driver.find_element(*HomePageElements.__GBP_dollar)

    def get_CAD_dollar(self):
        return self.driver.find_element(*HomePageElements.__CAD_dollar)

    def get_AUD_dollar(self):
        return self.driver.find_element(*HomePageElements.__AUD_dollar)

    def get_JPY_dollar(self):
        return self.driver.find_element(*HomePageElements.__JPY_dollar)

    def get_INR_dollar(self):
        return self.driver.find_element(*HomePageElements.__INR_dollar)

    def get_NZD_dollar(self):
        return self.driver.find_element(*HomePageElements.__NZD_dollar)

    def get_CHF_dollar(self):
        return self.driver.find_element(*HomePageElements.__CHF_dollar)

    def get_ZAR_dollar(self):
        return self.driver.find_element(*HomePageElements.__ZAR_dollar)

    def get_RUB_dollar(self):
        return self.driver.find_element(*HomePageElements.__RUB_dollar)

    def get_BGN_dollar(self):
        return self.driver.find_element(*HomePageElements.__BGN_dollar)

    def get_facebook(self):
        return self.driver.find_element(*HomePageElements.__facebook)

    def get_linkedin(self):
        return self.driver.find_element(*HomePageElements.__linkedin)

    def get_instagram(self):
        return self.driver.find_element(*HomePageElements.__instagram)

    def get_send_money_online(self):
        return self.driver.find_element(*HomePageElements.__send_money_online)

    def get_send_to_india(self):
        return self.driver.find_element(*HomePageElements.__send_to_india)

    def get_send_to_pakistan(self):
        return self.driver.find_element(*HomePageElements.__send_to_pakistan)

    def get_send_to_mexico(self):
        return self.driver.find_element(*HomePageElements.__send_to_mexico)

    def get_send_to_japan(self):
        return self.driver.find_element(*HomePageElements.__send_to_japan)

    def get_send_to_uk(self):
        return self.driver.find_element(*HomePageElements.__send_to_uk)

    def get_send_to_canada(self):
        return self.driver.find_element(*HomePageElements.__send_to_canada)

    def get_send_to_australia(self):
        return self.driver.find_element(*HomePageElements.__send_to_australia)

    def get_send_to_new_zealand(self):
        return self.driver.find_element(*HomePageElements.__send_to_new_zealand)

    def get_send_to_mobile_wallet(self):
        return self.driver.find_element(*HomePageElements.__send_to_mobile_wallet)

    def get_large_money_transfer(self):
        return self.driver.find_element(*HomePageElements.__large_money_transfer)

    def get_security(self):
        return self.driver.find_element(*HomePageElements.__security)

    def get_report_fraud(self):
        return self.driver.find_element(*HomePageElements.__report_fraud)

    def get_trustpilot_reviews(self):
        return self.driver.find_element(*HomePageElements.__trustpilot_reviews)

    def get_popup_yes(self):
        return self.driver.find_element(*HomePageElements.__popup_yes)

    def get_business_payments(self):
        return self.driver.find_element(*HomePageElements.__business_payments)

    def get_international_business_payments(self):
        return self.driver.find_element(*HomePageElements.__international_business_payments)

    def get_global_business_payments(self):
        return self.driver.find_element(*HomePageElements.__global_business_payments)

    def get_risk_management(self):
        return self.driver.find_element(*HomePageElements.__risk_management)

    def get_resource_planning(self):
        return self.driver.find_element(*HomePageElements.__resource_planning)

    def get_api_integration(self):
        return self.driver.find_element(*HomePageElements.__api_integration)

    def get_referral_program(self):
        return self.driver.find_element(*HomePageElements.__referral_program)

    def get_mass_payment(self):
        return self.driver.find_element(*HomePageElements.__mass_payment)

    def get_money_transfer_and_currency_apps(self):
        return self.driver.find_element(*HomePageElements.__money_transfer_and_currency_apps)

    def get_android_money_transfer_app(self):
        return self.driver.find_element(*HomePageElements.__android_money_transfer_app)

    def get_ios_money_transfer_app(self):
        return self.driver.find_element(*HomePageElements.__ios_money_transfer_app)

    def get_footer_blog(self):
        return self.driver.find_element(*HomePageElements.__footer_blog)

    def get_footer_currency_converter(self):
        return self.driver.find_element(*HomePageElements.__footer_currency_converter)

    def get_footer_currency_charts(self):
        return self.driver.find_element(*HomePageElements.__footer_currency_charts)

    def get_footer_historical_rates(self):
        return self.driver.find_element(*HomePageElements.__footer_historical_rates)

    def get_footer_encyclopedia(self):
        return self.driver.find_element(*HomePageElements.__footer_encyclopedia)
    
    def get_footer_rate_alerts(self):
        return self.driver.find_element(*HomePageElements.__footer_rate_alerts)

    def get_footer_newsletters(self):
        return self.driver.find_element(*HomePageElements.__footer_newsletters)

    def get_footer_iban_cal(self):
        return self.driver.find_element(*HomePageElements.__footer_IBAN_cal)

    def get_footer_glossary(self):
        return self.driver.find_element(*HomePageElements.__footer_glossary)

