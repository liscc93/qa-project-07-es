import data
import time
import pytest
from urban_routes_page import UrbanRoutesPage
from selenium import webdriver

class TestUrbanRoutes:

    driver = None
    initial_header = None
    final_header = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()# desired_capabilities=capabilities
        cls.driver.implicitly_wait(20)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

# Prueba 2 - Seleccionar tarifa Comfort
    @pytest.mark.sleep(10)
    def test_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ask_for_taxi()
        routes_page.click_comfort_button()
        assert self.driver.find_element(*routes_page.comfort_selected).get_attribute('class') == "tcard active"

# Prueba 3 - Rellenar el número de teléfono y verifcar código
    @pytest.mark.sleep(10)
    def test_fill_phone_num(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_button()
        routes_page.set_num_field()
        routes_page.click_phone_next_button()
        routes_page.set_verification_code()
        routes_page.click_code_confirm_button()
        assert self.driver.find_element(*routes_page.num_field).get_property('value') == data.phone_number

# Prueba 4 - Agregar una tarjeta de crédito
    @pytest.mark.sleep(10)
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        routes_page.set_card_number()
        routes_page.set_card_code()
        routes_page.press_tap_key()
        routes_page.click_add_information_card()
        routes_page.click_close_button_payment()
        assert self.driver.find_element(*routes_page.card_added).get_property('id') == 'card-1'

# Prueba 5 - Escribir un mensaje para el conductor
    @pytest.mark.sleep(10)
    def test_write_msg_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_driver()
        assert self.driver.find_element(*routes_page.message_driver).get_attribute('value') == data.message_for_driver

# Prueba 6 - Pedir manta y pañuelos
    @pytest.mark.sleep(10)
    def test_ask_for_blanket_and_napkins(self):
        routes_page = UrbanRoutesPage(self.driver)
        initial_state = routes_page.get_blanket_tissues_checkbox()
        routes_page.click_blanket_tissues()
        final_state = routes_page.get_blanket_tissues_checkbox()
        assert initial_state != final_state, "El estado del botón no cambió."

# Prueba 7 - Pedir 2 helados
    @pytest.mark.sleep(10)
    def test_request_two_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_icecream_button()
        assert self.driver.find_element(*routes_page.ice_cream_added).text == '2'

# Prueba 8 - Aparece el modal para buscar un taxi
    @pytest.mark.sleep(10)
    def test_appears_popup(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_request_taxi()
        assert self.driver.find_element(*routes_page.request_taxi).is_displayed()

# Prueba 9 - Espera de la informarción del conductor en el modal
    def test_information_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(40)
        assert self.driver.find_element(*routes_page.information_driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()