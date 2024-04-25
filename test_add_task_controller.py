import unittest
from datetime import datetime

from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect

from task_controller import TaskController  # Update with the correct import statement


class MockView:
    def __init__(self):
        self.selected_item = 1
        self.general_task_id = 1

    def run(self):
        pass

    def update_daily_tasks(self):
        print("Updating daily tasks")

    def update_all_tasks(self):
        print("Updating all tasks")

    def view_categories(self):
        print("Viewing categories")

    def update_reminders(self):
        print("Updating reminders")

    def update_about(self):
        print("Updating about")


class MockModel:
    def __init__(self):
        self.categories = []
        self.categories_count = 0

    def add_task(self, task):
        print(f"Adding task: {task}")

    def update_categories(self):
        print("Updating categories")


class ListNameObject:
    def __init__(self, name):
        self.text = "General"  # Assuming 'text' is used in your add_task method
        self.name = name  # Adding 'name' attribute for clarity



class TestTaskController(unittest.TestCase):
    def setUp(self):
        self.mock_view = MockView()
        self.mock_model = MockModel()
        self.task_controller = TaskController(view=self.mock_view, model=self.mock_model)

    def test_add_task_with_list_name_object(self):
        task_name = MDTextFieldRect(id = 'task_name',text="Task1")
        description_text = MDTextFieldRect(id="description_text",text="Description")
        date_text = MDLabel(id="date_text",text="2023-12-31")
        priority= MDTextFieldRect(id="priority",text="Low")
        list_name = MDTextFieldRect(id="list_name",text="General")

        self.moock_view.root.add_widget(task_name)
        self.mock_view.root.add_widget(description_text)
        self.mock_view.root.add_widget(date_text)
        self.mock_view.root.add_widget(priority)
        self.mock_view.root.add_widget(list_name)
        self.task_controller.add_task(self.mock_view.ids.task_name,self.mock_view.ids.description_text,self.mock_view.ids.date_text,self.mock_view.ids.priority,self.mock_view.ids.list_name)

        # Add your assertions based on the expected behavior
        # For example, you might want to check if the model's add_task method was called with the correct arguments
        # Uncomment and customize the following line based on your actual implementation
        # self.assertEqual(self.mock_model.add_task_called_with, expected_arguments)


if __name__ == "__main__":
    unittest.main()
