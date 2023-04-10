import pytest

from pages.landing_page import LandingPage
from helper.outlook_util import OutlookUtil


@pytest.mark.usefixtures("browser")
@pytest.mark.usefixtures("config")
class TestLogin:
    @pytest.mark.positive
    def test_login(self, config):
        email = config["email"]
        password = config["password"]
        email_password = config["email_password"]

        login_page = self.select_country_and_language(config)
        identity_page = login_page.select_country_and_language(email, password).click_send_code_button()
        assert not identity_page.is_verify_and_login_button_enabled(), "The button should be disabled"

        outlook_util = OutlookUtil(email, email_password)
        verification_code = outlook_util.get_verification_code()
        identity_page.enter_verification_code(verification_code)
        assert identity_page.is_verify_and_login_button_enabled(), "The button should be enabled"

        glucose_history_page = identity_page.click_verify_and_login_button()
        assert glucose_history_page.is_upload_device_button_enabled(), "The button should be enabled"

        upload_device_page = glucose_history_page.navigate_to_upload_device_page()
        assert upload_device_page.is_press_to_begin_upload_button_enabled(), "The button should be enabled"

    @pytest.mark.negative
    def test_user_cannot_login_with_valid_email_and_invalid_password(self, config):
        email = config["email"]
        fake_password = "randompassword"

        login_page = self.select_country_and_language(config)
        login_page.enter_email(email)
        login_page.enter_password(fake_password)
        login_page.click_login_button()
        assert login_page.get_invalid_combination_error_message() == \
               "There was a problem with your email/password combination. Please try again.", "Wrong error message"

    @pytest.mark.negative
    def test_user_cannot_login_with_invalid_email(self, config):
        password = config["password"]
        fake_email = "fake@fake.com"

        login_page = self.select_country_and_language(config)
        login_page.enter_email(fake_email)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert login_page.get_invalid_combination_error_message() == \
               "There was a problem with your email/password combination. Please try again.", "Wrong error message"

    @pytest.mark.negative
    def test_invalid_email_format_error_message(self, config):
        invalid_format_email = "fake@@fake.com"

        login_page = self.select_country_and_language(config)
        login_page.enter_email(invalid_format_email)
        login_page.click_login_button()
        assert login_page.get_invalid_email_format_error_message() == "Email address is invalid", "Wrong error message"

    @pytest.mark.negative
    def test_empty_email_error_message(self, config):
        password = config["password"]

        login_page = self.select_country_and_language(config)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert login_page.get_invalid_email_format_error_message() == "Email address is required", "Wrong error message"

    @pytest.mark.negative
    def test_empty_password_error_message(self, config):
        email = config["email"]
        login_page = self.select_country_and_language(config)
        login_page.enter_email(email)
        login_page.click_login_button()
        assert login_page.get_invalid_password_format_error_message() == "Password is required", "Wrong error message"

    def select_country_and_language(self, config):
        country = config["country"]
        language = config["language"]
        landing_page = LandingPage(self.driver).go()
        landing_page.accept_cookies_if_present()
        landing_page.select_country(country)
        landing_page.select_language(language)
        login_page = landing_page.click_submit_button()
        return login_page
