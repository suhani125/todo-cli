from todo import add_task, mark_done, delete_task, load_tasks, save_tasks


def test_add_task_assigns_incrementing_ids():
    tasks = []
    assert add_task(tasks, "A")["id"] == 1
    assert add_task(tasks, "B")["id"] == 2


def test_mark_done():
    tasks = []
    add_task(tasks, "A")
    assert mark_done(tasks, 1) is True
    assert tasks[0]["done"] is True
    assert mark_done(tasks, 99) is False


def test_delete_task():
    tasks = []
    add_task(tasks, "A")
    assert delete_task(tasks, 1) is True
    assert tasks == []
    assert delete_task(tasks, 1) is False


def test_save_and_load(tmp_path):
    f = tmp_path / "t.json"
    tasks = []
    add_task(tasks, "A")
    save_tasks(tasks, f)
    assert load_tasks(f) == tasks
