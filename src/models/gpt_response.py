#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on seg jun 26 13:48:23 2023
@author ccavalcante
"""

from typing import List

from pydantic import BaseModel, Field

ASSISTANT_ROLE='assistant'

class MessageModel(BaseModel):
    """
    Main message data
    """

    role: str = Field()
    content: str = Field()

class ChoiceModel(BaseModel):
    """
    Choices mapping
    """

    message: MessageModel = Field('Message data per choice')

    def get_content(self) -> str:
        """
        Returns the message content

        Returns
        -------
            str
        """

        return self.message.content



    def is_answer(self) -> bool:
        """
        Check if the message is a gpt answer

        Returns
        -------
            bool
        """

        return self.message.role == ASSISTANT_ROLE


class GptResponseModel(BaseModel):
    """ Model used to translate the GPT json response """

    choices: List[ChoiceModel] = Field(description='List of contents')

    def get_answer(self) -> str:
        """
        Returns the Chatgpt answer formatted

        Returns
        -------
            str
        """

        answers = [message for message in self.choices if message.is_answer()]

        return "\n\n".join(answer.get_content() for answer in answers)
