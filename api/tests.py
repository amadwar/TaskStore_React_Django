from django.test import TestCase
from django.test import TestCase
from .models import Task
from .serializers import Taskserializers

# Create your tests here.
class TaskSerializerTestCase(TestCase):
    def setUp(self):
        self.task_data = {
            'type': 'Feature',
            'title': 'New feature',
            'description': 'Add a new feature to the system',
            'due_date': '2023-03-03',
            'assigned_user':  1, # change the link to id
            'assigned_group': 2, # change the link to id
            'created_by': 1, # change the link to id
            'modified_by': 1, # change the link to id
            'status': 'new' 
        }

    def test_task_serializer(self):
        serializer = Taskserializers(data=self.task_data)
        self.assertTrue(serializer.is_valid())
        task = serializer.save()
        self.assertEqual(task.type, 'Feature')
        self.assertEqual(task.title, 'New feature')
        self.assertEqual(task.description, 'Add a new feature to the system')
        self.assertEqual(task.due_date, '2022-01-01')
        self.assertEqual(task.assigned_user, 1) # check the ID of the user
        self.assertEqual(task.assigned_group, 2) # check the ID of the group
        self.assertEqual(task.created_by, 1) # check the ID of the user
        self.assertEqual(task.modified_by, 1) # check the ID of the user
        self.assertEqual(task.status, 'new')




