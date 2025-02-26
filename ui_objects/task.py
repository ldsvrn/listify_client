from . import subtask as sbts

from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Task(QFrame):
    """
    Task

    Project => Repository => Task => Subtask
    """

    def __init__(self, name_task: str = 'Tache', subtask_list=None):
        """
        create the task's ui elements, passing a subtask is optional
        :param name_task: name of task
        :param subtask_list: list of subtask
        """
        super().__init__()
        if subtask_list is None:  # creation of an empty list if none is given
            subtask_list = []
        self.__name_task = name_task
        self.__subtask_list = subtask_list

        self.setFrameStyle(QFrame.StyledPanel)

        # creating a widget and set layout
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.__task_label = QLabel(self.__name_task)

        self.__layout.addWidget(self.__task_label)

        self.__create_subtask_button = QPushButton("Créer une sous-tâche")
        self.__create_subtask_button.clicked.connect(
            lambda: self.create_subtask("subtask_test")
        )
        self.__layout.addWidget(self.__create_subtask_button)

        if self.__subtask_list:
            for subtask_widget in self.__subtask_list:
                self.__layout.addWidget(subtask_widget)

    def __str__(self):  # str to print the title in the project
        """
        return the task's name when printing
        :return:
        """
        return f"{self.__name_task}"

    def create_subtask(self, name_subtask: str = "Sous tache"):
        """
        create a subtask with a name
        :param name_subtask: str
        :return:
        """
        created_subtask = sbts.Subtask(name_subtask)
        self.__subtask_list.append(created_subtask)  # create the object in the list
        self.__layout.addWidget(created_subtask)

    def delete_subtask(self, num):
        """
        delete the "num"th subtask
        :param num:
        :return:
        """
        del self.__subtask_list[num]

    def to_dict(self):
        """
        exports the task to a dictionary for json serialization,
        called by the task's parent,
        it calls its children to_dict() methods
        :return: dict of the task
        """
        subtask_dicts = []
        for subtask in self.__subtask_list:
            subtask_dicts.append(subtask.to_dict())

        return {
            "name": self.__name_task,
            "subtasks": subtask_dicts,
        }

    @property
    def name_task(self):
        """
        returns the name of the task
        :return: str: name of the task
        """
        return self.__name_task

    @name_task.setter
    def name_task(self, name_task):
        """
        sets the name of the task
        :param name_task: str
        :return:
        """
        self.__name_task = name_task

    @property
    def subtask_list(self):
        """
        returns the list of subtasks
        :return: list
        """
        return self.__subtask_list

    @subtask_list.setter
    def subtask_list(self, subtask_list):
        """
        sets the list of subtasks
        :param subtask_list: list
        :return:
        """
        self.__subtask_list = subtask_list
