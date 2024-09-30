import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.homePageElements import HomePageElements
from testData.currencyExchangeData import CurrencyExchangeData
from utilities.baseClass import BaseClass


class TestHomePage(BaseClass):

    def test_logo(self):
        home_page = HomePageElements(self.driver)
        logo = home_page.get_company_logo()
        logo.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(logo))
            print("Page refreshed after clicking the Logo.")
        except Exception as e:
            print(e)

    def test_personal_plan(self):
        home_page = HomePageElements(self.driver)
        personal = home_page.get_personal_plan()
        personal.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(personal))
            print("Page refreshed after clicking the Logo.")
        except Exception as e:
            print(e)

    def test_business_plan(self):
        home_page = HomePageElements(self.driver)
        home_page.get_business_plan().click()

        try:
            self.assert_current_url("business")
        except Exception as e:
            print(e)
        self.driver.back()

    def test_send_money_header(self):
        home_page = HomePageElements(self.driver)
        home_page.get_send_money_header().click()

        try:
            self.assert_current_url("send-money")
        except Exception as e:
            print(e)
        self.driver.back()

    def test_currency_converter(self):
        home_page = HomePageElements(self.driver)
        home_page.get_converter().click()

        try:
            self.assert_current_url("currencyconverter")
        except Exception as e:
            print(e)
        self.driver.back()

    def test_currency_api(self):
        home_page = HomePageElements(self.driver)
        home_page.get_currency_api().click()

        try:
            self.assert_current_url("currencydata")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_currency_chart(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_tools()).perform()
        actions.move_to_element(home_page.get_currency_chart()).click().perform()

        try:
            self.assert_current_url("currencycharts")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_IBAN_calculator(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_tools()).perform()
        actions.move_to_element(home_page.get_IBAN_calculator()).click().perform()
        try:
            self.assert_current_url("ibancalculator")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_rate_alert_tools(self):
        time.sleep(3)
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_tools()).perform()
        actions.move_to_element(home_page.get_rate_alert_tools()).click().perform()

        try:
            self.assert_current_url("ratealerts")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_apps(self):
        time.sleep(3)
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_tools()).perform()
        actions.move_to_element(home_page.get_apps()).click().perform()

        try:
            self.assert_current_url("apps")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_historical_currency_rates(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_tools()).perform()
        actions.move_to_element(home_page.get_historical_currency_rates()).click().perform()

        try:
            self.assert_current_url("currencytables")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_more_tools(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_tools()).perform()
        actions.move_to_element(home_page.get_more_tools()).click().perform()

        try:
            self.assert_current_url("tools")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_help_center(self):
        time.sleep(3)
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources()).perform()
        actions.move_to_element(home_page.get_help_center()).click().perform()
        self.driver.switch_to.window(self.driver.window_handles[1])

        try:
            self.assert_current_url("hc/en-gb")
        except Exception as e:
            print(e)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)

    # def test_refer_a_friend(self):
    #     time.sleep(3)
    #     home_page = HomePageElements(self.driver)
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(home_page.get_resources()).perform()
    #     actions.move_to_element(home_page.get_refer_a_friend()).click().perform()
    #
    #     try:
    #         self.assert_current_url("refer-a-friend")
    #     except Exception as e:
    #         print(e)
    #
    #     self.driver.back()

    def test_blog(self):
        time.sleep(3)
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources()).perform()
        actions.move_to_element(home_page.get_blog()).click().perform()

        try:
            self.assert_current_url("blog")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_money_transfer_tips(self):
        time.sleep(3)
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources()).perform()
        actions.move_to_element(home_page.get_money_transfer_tips()).click().perform()

        try:
            self.assert_current_url("moneytransfertips")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_currency_encyclopedia(self):
        time.sleep(3)
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources()).perform()
        actions.move_to_element(home_page.get_currency_encyclopedia()).click().perform()

        try:
            self.assert_current_url("currency")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_currency_newsletter(self):
        time.sleep(3)
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources()).perform()
        actions.move_to_element(home_page.get_currency_newsletter()).click().perform()

        try:
            self.assert_current_url("currencyemail")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_glossary(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources()).perform()
        glossary = home_page.get_currency_newsletter()
        actions.move_to_element(glossary).click().perform()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(glossary))
            print("Page refreshed after clicking the Logo.")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_more_resources(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_resources()).perform()
        actions.move_to_element(home_page.get_more_resources()).click().perform()
        try:
            self.assert_current_url("learn")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_money_transfer_signin(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_sign_in()).perform()
        actions.move_to_element(home_page.get_money_transfer_signin()).click().perform()
        try:
            self.assert_current_url("signin")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_rate_alert_signin(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_sign_in()).perform()
        actions.move_to_element(home_page.get_rate_alert_signin()).click().perform()
        try:
            self.assert_current_url("login")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_money_transfer_register(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_register()).perform()
        actions.move_to_element(home_page.get_money_transfer_register()).click().perform()
        try:
            self.assert_current_url("signup")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    def test_rate_alert_register(self):
        home_page = HomePageElements(self.driver)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_page.get_register()).perform()
        actions.move_to_element(home_page.get_rate_alerts_register()).click().perform()
        try:
            self.assert_current_url("signup")
        except Exception as e:
            print(e)
        self.driver.back()
        time.sleep(3)

    #---------------------------- Footer Test ---------------------------- (Incomplete)

    # def test_US_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_US_dollar().click()
    #
    #     try:
    #         self.assert_current_url("usd-us-dollar")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_EUR_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_EUR_dollar().click()
    #
    #     try:
    #         self.assert_current_url("eur-euro")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_GBP_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_GBP_dollar().click()
    #
    #     try:
    #         self.assert_current_url("gbp-british-pound")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_CAD_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_CAD_dollar().click()
    #
    #     try:
    #         self.assert_current_url("cad-canadian-dollar")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_AUD_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_AUD_dollar().click()
    #
    #     try:
    #         self.assert_current_url("aud-australian-dollar")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_JPY_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_JPY_dollar().click()
    #
    #     try:
    #         self.assert_current_url("jpy-japanese-yen")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_INR_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_INR_dollar().click()
    #
    #     try:
    #         self.assert_current_url("inr-indian-rupee")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_NZD_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_NZD_dollar().click()
    #
    #     try:
    #         self.assert_current_url("nzd-new-zealand-dollar")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_CHF_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_CHF_dollar().click()
    #
    #     try:
    #         self.assert_current_url("chf-swiss-franc")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_ZAR_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_ZAR_dollar().click()
    #
    #     try:
    #         self.assert_current_url("zar-south-african-rand")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_RUB_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_RUB_dollar().click()
    #
    #     try:
    #         self.assert_current_url("rub-russian-ruble")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_BGN_dollar(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_BGN_dollar().click()
    #
    #     try:
    #         self.assert_current_url("bgn-bulgarian-lev")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)

    # def test_facebook(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_facebook().click()
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #
    #     try:
    #         self.assert_current_url("facebook")
    #     except Exception as e:
    #         print(e)
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     time.sleep(3)
    #
    # def test_linkedin(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_facebook().click()
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #
    #     try:
    #         self.assert_current_url("linkedin")
    #     except Exception as e:
    #         print(e)
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     time.sleep(3)
    #
    # def test_instagram(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_instagram().click()
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #
    #     try:
    #         self.assert_current_url("instagram")
    #     except Exception as e:
    #         print(e)
    #     self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     time.sleep(3)

    # def test_send_money_online(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_money_online().click()
    #
    #     try:
    #         self.assert_current_url("send-money")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_india(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_india().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-india")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_pakistan(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_pakistan().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-pakistan")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_mexico(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_mexico().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-mexico")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)

    # def test_send_to_japan(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_japan().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-japan")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_uk(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_uk().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-uk")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_canada(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_canada().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-canada")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_australia(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_australia().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-australia")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_new_zealand(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_new_zealand().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-new-zealand")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_mobile_wallet(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_mobile_wallet().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-mobile-wallet")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_large_money_transfer(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_large_money_transfer().click()
    #
    #     try:
    #         self.assert_current_url("large-money-transfer")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_security(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_security().click()
    #
    #     try:
    #         self.assert_current_url("security")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_to_mexico(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_to_mexico().click()
    #
    #     try:
    #         self.assert_current_url("send-money-to-mexico")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_report_fraud(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_report_fraud().click()
    #     time.sleep(5)
    #     home_page.get_popup_yes().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("contact-details")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_trustpilot_reviews(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_trustpilot_reviews().click()
    #     time.sleep(5)
    #     home_page.get_popup_yes().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("trustpilot")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)

    # def test_business_payment(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_business_payments().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("business")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_international_business_payment(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_international_business_payments().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("send-money")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_global_business_payment(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_global_business_payments().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("payments")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_risk_management(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_risk_management().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("risk-management")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_resource_planning(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_resource_planning().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("erp")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_api_integration(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_api_integration().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("currencydata")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_referral_program(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_referral_program().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("referral-partner")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_mass_payment(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_mass_payment().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("mass-payments")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)

    # def test_money_transfer_and_currency_apps(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_money_transfer_and_currency_apps().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("apps")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_android_money_transfer_app(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_android_money_transfer_app().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("android")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_ios_money_transfer_app(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_ios_money_transfer_app().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("ios")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)

    # def test_footer_blog(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_blog().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("blog")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_currency_converter(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_currency_converter().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("currencyconverter")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_currency_charts(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_currency_charts().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("currencycharts")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_historical_rates(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_historical_rates().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("currencytables")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_encyclopedia(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_encyclopedia().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("currency")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_rate_alerts(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_rate_alerts().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("ratealerts")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_newsletter(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_newsletters().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("currencyemail")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_iban_cal(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_iban_cal().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("ibancalculator")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_footer_glossary(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_footer_glossary().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("terms")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)




#  ------------------------------ Body Tests ----------------------------------

    # def test_convert_btn(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_convert_btn().click()
    #
    #     try:
    #         self.assert_current_url("currencyconverter")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_send_btn(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_send_btn().click()
    #
    #     try:
    #         self.assert_current_url("send-money")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_charts_btn(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_charts_btn().click()
    #
    #     try:
    #         self.assert_current_url("currencycharts")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_alerts_btn(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_alerts_btn().click()
    #
    #     try:
    #         self.assert_current_url("ratealerts")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)

    # def test_convert_currencies(self):
    #     home_page = HomePageElements(self.driver)
    #
    #     explicitWait = WebDriverWait(self.driver, 6)
    #     home_page.get_amount_field().click()
    #     home_page.get_amount_field().clear()
    #     time.sleep(3)
    #     # home_page.get_amount_field().send_keys(get_form_data["Amount"])
    #     home_page.get_amount_field().send_keys("22")
    #     input_field = float(home_page.get_amount_field().get_attribute("value"))
    #     # input_field = format(input_field, ".2f")
    #     # home_page.get_from_field().send_keys(get_form_data["From"])
    #     home_page.get_from_field().send_keys("Ind")
    #     time.sleep(3)
    #     explicitWait.until(
    #         EC.presence_of_element_located((By.ID, "midmarketFromCurrency-listbox"))
    #     )
    #     home_page.get_from_country().click()
    #     # home_page.get_to_field().send_keys(get_form_data["To"])
    #     home_page.get_to_field().send_keys("Pak")
    #     time.sleep(5)
    #     explicitWait.until(
    #         EC.presence_of_element_located((By.ID, "midmarketToCurrency-listbox"))
    #     )
    #     home_page.get_to_country().click()
    #     home_page.get_convert_the_currency().click()
    #     time.sleep(5)
    #     rate = home_page.get_rate_of_from_country().text
    #     rate = rate.split(" ")
    #     per_rate = float(rate[-2])
    #     # per_rate = format(per_rate, ".2f")
    #     print(per_rate)
    #     converted_amount = home_page.get_converted_amount().text
    #     converted_amount = converted_amount.split(" ")
    #     total = round(float(converted_amount[0]), 2)
    #     # total = format(total, ".2f")
    #     print(converted_amount[0])
    #     # cal = (per_rate * input_field)
    #     # cal = format(cal, '.2f')
    #     print((per_rate * input_field))
    #     print(str(per_rate * input_field) in str(total))
    #     # print(home_page.get_converted_amount().text)
    #     time.sleep(5)
    #     self.driver.back()
    #     time.sleep(5)
    #
    #
    #
    # @pytest.fixture(params=CurrencyExchangeData.currency_data)
    # def get_form_data(self, request):
    #     return request.param

    # def test_get_started(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_get_started().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("signup")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_body_send_money(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_body_send_money().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("send-money")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_body_view_charts(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_body_view_charts().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("currencycharts")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)
    #
    # def test_body_create_alerts(self):
    #     home_page = HomePageElements(self.driver)
    #     home_page.get_create_alerts().click()
    #     time.sleep(5)
    #     try:
    #         self.assert_current_url("ratealerts")
    #     except Exception as e:
    #         print(e)
    #     self.driver.back()
    #     time.sleep(3)










