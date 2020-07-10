from argparse import ArgumentParser
from sys import exit
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = None

BASIS = 0
STANDARD = 1
PREMIUM = 2


def change_plan(plan):
    driver.get("https://www.netflix.com/ChangePlan")
    try:
        driver.find_elements_by_class_name(
            "stacked-large-selection-list-item")[plan].click()
        driver.find_element_by_class_name("save-plan-button").click()
        driver.find_element_by_class_name("modal-action-button").click()
    except (IndexError, NoSuchElementException):
        quit_and_exit()


def login(user_login_id, password):
    driver.get("https://www.netflix.com/de/login")
    try:
        driver.find_element_by_id("id_userLoginId").send_keys(user_login_id)
        driver.find_element_by_id(
            "id_password").send_keys(password, Keys.ENTER)
    except NoSuchElementException:
        quit_and_exit()

    if driver.find_elements_by_class_name("ui-message-error"):
        quit_and_exit()


def parse_arguments():
    parser = ArgumentParser(
        usage="%(prog)s -u USERNAME -p PASSWORD")
    parser.add_argument(
        "-s",
        "--sleep",
        default=0,
        type=int,
        help="Pause time between plan change",
        metavar="SECONDS")
    required_arguments = parser.add_argument_group("required arguments")
    required_arguments.add_argument(
        "-u",
        "--username",
        required=True,
        help="Your netflix email adress or phone number")
    required_arguments.add_argument(
        "-p",
        "--password",
        required=True,
        help="Your netflix password")
    args = parser.parse_args()
    return args


def quit_and_exit():
    driver.quit()
    exit()


def start_webdriver():
    global driver
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)


def main(args):
    start_webdriver()
    login(args.username, args.password)
    change_plan(PREMIUM)
    sleep(args.sleep)
    change_plan(BASIS)
    quit_and_exit()


if __name__ == "__main__":
    main(parse_arguments())
