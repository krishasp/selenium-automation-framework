from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    
    message = login.get_message()
    assert "You logged into a secure area!" in message


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("wronguser", "wrongpass")

    message = login.get_message()
    assert "Your username is invalid!" in message