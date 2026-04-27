import json
from src.sources.file_source import FileSource
from src.sources.api_source import ApiSource
from src.sources.generator_source import GeneratorSource
from src.models import Task


def test_file_source_reads_successfully(temp_json_file):
    """Проверяет успешное чтение из корректного JSON-файла."""
    file_path, expected_content = temp_json_file
    source = FileSource(file_path)
    tasks = source.get_tasks()

    assert len(tasks) == len(expected_content)
    for task_obj, expected_dict in zip(tasks, expected_content):
        assert isinstance(task_obj, Task)
        assert task_obj.id == expected_dict['id']
        assert task_obj.payload == expected_dict['payload']


def test_file_source_handles_non_existent_file():
    """Проверяет, что FileSource возвращает пустой список, если файл не найден."""
    source = FileSource("non_existent_file.json")
    tasks = source.get_tasks()
    assert tasks == []


def test_file_source_handles_malformed_json(tmp_path):
    """Проверяет, что FileSource возвращает пустой список при ошибке парсинга JSON."""
    file_path = tmp_path / "malformed.json"
    malformed_json_string = '[{"id": "1"},]'
    file_path.write_text(malformed_json_string)

    source = FileSource(str(file_path))
    tasks = source.get_tasks()
    assert tasks == []


def test_file_source_handles_missing_keys(tmp_path):
    """Проверяет, что FileSource возвращает пустой список, если в JSON не хватает ключей."""
    file_path = tmp_path / "missing_keys.json"
    content_with_wrong_keys = [{"identifier": "123", "data": {}}]
    file_path.write_text(json.dumps(content_with_wrong_keys))

    source = FileSource(str(file_path))
    tasks = source.get_tasks()
    assert tasks == []


def test_api_source_returns_tasks():
    """Проверяет, что ApiSource возвращает список объектов Task."""
    source = ApiSource()
    tasks = source.get_tasks()
    assert isinstance(tasks, list)
    assert len(tasks) > 0
    assert all(isinstance(t, Task) for t in tasks)


def test_generator_source_creates_correct_count():
    """Проверяет, что GeneratorSource создает указанное количество задач."""
    count = 6
    source = GeneratorSource(count=count)
    tasks = source.get_tasks()
    assert len(tasks) == count
    assert all(isinstance(t, Task) for t in tasks)


def test_generator_source_with_zero_count():
    """Проверяет, что GeneratorSource возвращает пустой список при count=0."""
    source = GeneratorSource(count=0)
    tasks = source.get_tasks()
    assert tasks == []
