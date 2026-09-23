from datetime import datetime, timedelta

from icalendar import Todo


def test_todo_due_without_start_has_zero_duration():
    todo = Todo.new(end=datetime.utcnow())

    assert todo.duration == timedelta(0)