import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='phonebook.log',
    # filemode='w', # при каждом новом запуске перезапись логов
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
# logging.basicConfig(
#     level=logging.ERROR,
#     filename='phonebook.log',
#     format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
#     datefmt='%d.%m.%Y %H:%M:%S ',
# )

# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")


# def func():
#     logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")
