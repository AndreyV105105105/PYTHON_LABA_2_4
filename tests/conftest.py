import pytest
import json
import os


@pytest.fixture
def temp_json_file(tmp_path):
    """
    Фикстура для создания временного JSON-файла с данными для тестов.
    Возвращает путь к файлу и его содержимое.
    """
    content = [
        {"id": "1", "payload": {"sousdafsdrce": "bfdsb-file"}},
        {"id": "2", "payload": {"dsf": "sdbdfb"}}
    ]
    # tmp_path - это фикстура pytest для создания временных директорий
    file_path = tmp_path / "tasks.json"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f)

    # yield возвращает управление тесту, а код после yield выполняется после завершения теста
    yield str(file_path), content

    # Очистка: удаляем файл после теста (хотя tmp_path делает это автоматически)
    os.remove(file_path)

