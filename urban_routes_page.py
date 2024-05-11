import data
from selenium.webdriver.common.by import By
from data import phone_number
from data import card_number
from data import card_code
from data import message_for_driver
from utility import retrieve_phone_code
from selenium.webdriver import Keys


class UrbanRoutesPage:
    # Paso 1 Donde y hasta
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Paso 2 Seleccionar Comfort
    ask_for_taxi = (By.XPATH, "//button[@class = 'button round']")
    comfort_button = (By.XPATH, "//img[@alt='Comfort']")
    comfort_selected = (By.XPATH, "//div[@class = 'tcard active']") # Corrección
    # Paso 3 Agregar número de teléfono
    phone_button = (By.XPATH, "//div[text()='Número de teléfono']")
    num_field = (By.ID, 'phone')
    phone_next_button = (By.XPATH, "//button[text() = 'Siguiente']") # Corrección
    code_field = (By.ID, 'code')
    code_confirm_button = (By.XPATH, "//button[text() = 'Confirmar']") # Corrección
    confirm_phone_number = (By.XPATH, "div[@class = ''np-text]")
    # Paso 4 Agregar tarjeta de crédito
    payment_method = (By.XPATH, "//div[@class = 'pp-text']")
    add_card_button = (By.XPATH, "//div[@class = 'pp-plus-container']")
    card_number = (By.ID, 'number')
    card_code = (By.XPATH, "//input[@placeholder = '12']")
    add_information_card = (By.XPATH, "//button[text()='Agregar']") # Corrección
    close_button_payment = (By.XPATH, "(//button[@class = 'close-button section-close'])[3]") #Lo intenté con otros selectores pero no me dio y no tiene muchas opciones
    card_added = (By.XPATH, "//div[@class = 'pp-value-text']")
    # Paso 5 Mensaje para conductor
    message_driver = (By.ID, 'comment')
    # Paso 6 Agregar cobija y pañuelos
    blanket_tissues = (By.XPATH, "(//span[@class = 'slider round'])[1]") #No hay más opciones
    blanket_tissues_checkbox = (By.CSS_SELECTOR, "div.r-sw-container input.switch-input")
    # Paso 7 Agregar helados
    ice_cream = (By.XPATH, "(//div[@class ='counter-plus'])[1]") #No hay más opciones
    ice_cream_added = (By.XPATH, "//div[@class = 'counter-value']")
    # Paso 8 Solicitar el taxi
    request_taxi = (By.XPATH, "//span[@class ='smart-button-secondary']")
    order_pop_up = (By.XPATH, "//div[@class = 'order-header-title']")
    # Paso 9 Esperar información del conductor
    information_driver = (By.CLASS_NAME, 'order-number')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.driver.get(data.urban_routes_url)
        self.set_from(address_from)
        self.get_from()
        self.set_to(address_to)
        self.get_to()

    def click_ask_for_taxi(self):
        self.driver.find_element(*self.ask_for_taxi).click()

    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()

    def click_phone_button(self):
        self.driver.find_element(*self.phone_button).click()

    def set_num_field(self):
        self.driver.find_element(*self.num_field).send_keys(phone_number)

    def click_phone_next_button(self):
        self.driver.find_element(*self.phone_next_button).click()

    def set_verification_code(self):
        self.driver.find_element(*self.code_field).send_keys(retrieve_phone_code(self.driver))

    def click_code_confirm_button(self):
        self.driver.find_element(*self.code_confirm_button).click()

    def get_confirm_number(self):
        return self.driver.find_element(*self.num_field).get_property('value')

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self):
        self.driver.find_element(*self.card_number).send_keys(card_number)

    def set_card_code(self):
        self.driver.find_element(*self.card_code).send_keys(card_code)

    def press_tap_key(self):
        self.driver.find_element(*self.card_code).send_keys(Keys.TAB)

    def click_add_information_card(self):
        self.driver.find_element(*self.add_information_card).click()

    def click_close_button_payment(self):
        self.driver.find_element(*self.close_button_payment).click()

    def get_confirm_card(self):
        return self.driver.find_element(*self.card_added).get_property('value')

    def set_message_driver(self):
        self.driver.find_element(*self.message_driver).send_keys(message_for_driver)

    def click_blanket_tissues(self):
        self.driver.find_element(*self.blanket_tissues).click()

    def get_blanket_tissues_checkbox(self):
        checkbox = self.driver.find_element(*self.blanket_tissues_checkbox)
        return checkbox.is_selected()

    def click_add_icecream_button(self):
        add_icecream_buttons = self.driver.find_elements(*self.ice_cream)
        for button in add_icecream_buttons:
            button.click()
            button.click()

    def click_request_taxi(self):
        self.driver.find_element(*self.request_taxi).click()

    def wait_information_driver(self):
        self.driver.find_element(*self.information_driver)
