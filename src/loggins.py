import logging

def setup_logging():
    """
    Настройка логирования для системы обработки задач.
    """
    logging.basicConfig(
        level=logging.INFO, 
        filename="shell.log", 
        filemode="w",
        # Добавил encoding, чтобы русские символы в логах не превратились в порнографию
        encoding='utf-8', 
        # Добавил [%(name)s], чтобы понимать, из какого файла пришел лог
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s"
    )

logger = logging.getLogger(__name__)
