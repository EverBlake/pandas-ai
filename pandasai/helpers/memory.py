""" Memory class to store the conversations """
from typing import Union


class Memory:
    """Memory class to store the conversations"""

    _messages: list
    _memory_size: int
    _agent_info: str

    def __init__(self, memory_size: int = 1, agent_info: Union[str, None] = None):
        self._messages = []
        self._memory_size = memory_size
        self._agent_info = agent_info

    def add(self, message: str, is_user: bool):
        self._messages.append({"message": message, "is_user": is_user})

    def count(self) -> int:
        return len(self._messages)

    def all(self) -> list:
        return self._messages

    def last(self) -> dict:
        return self._messages[-1]

    def _truncate(self, message: Union[str, int], max_length: int = 100) -> str:
        """
        Truncates the message if it is longer than max_length
        """
        return (
            f"{message[:max_length]} ..." if len(str(message)) > max_length else message
        )

    def get_messages(self, limit: int = None) -> list:
        """
        Returns the conversation messages based on limit parameter
        or default memory size
        """
        limit = self._memory_size if limit is None else limit

        return [
            f"{'### QUERY' if message['is_user'] else '### ANSWER'}\n {message['message'] if message['is_user'] else self._truncate(message['message'])}"
            for message in self._messages[-limit:]
        ]

    def get_conversation(self, limit: int = None) -> str:
        """
        Returns the conversation messages based on limit parameter
        or default memory size
        """
        return "\n".join(self.get_messages(limit))

    def get_previous_conversation(self) -> str:
        """
        Returns the previous conversation but the last message
        """
        messages = self.get_messages(self._memory_size)
        return "" if len(messages) <= 1 else "\n".join(messages[:-1])

    def get_last_message(self) -> str:
        """
        Returns the last message in the conversation
        """
        messages = self.get_messages(self._memory_size)
        return "" if len(messages) == 0 else messages[-1]

    def get_system_prompt(self) -> str:
        return self._agent_info

    def to_json(self):
        messages = []
        for message in self.all():
            if message["is_user"]:
                messages.append({"role": "user", "message": message["message"]})
            else:
                messages.append({"role": "assistant", "message": message["message"]})
        return messages

    def clear(self):
        self._messages = []

    @property
    def size(self):
        return self._memory_size

    @property
    def agent_info(self):
        return self._agent_info
