#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on seg jun 26 18:07:39 2023
@author ccavalcante
"""
import json
import os
import requests

from models.gpt_response import GptResponseModel

WELCOME_QUESTION = "Hello sir, what do you want?"
OPENAI_KEY_LABEL='OPENAI_API_KEY'
ASSITANT_ROLE='assistant'

class ChatgptApiBusiness:
    """ Manage ChatGPT connections and other transformations """

    def __init__(self):

        self.__welcome_question = WELCOME_QUESTION
        self.__api_key = os.environ.get(OPENAI_KEY_LABEL)


        self.__openai_url = 'https://api.openai.com/v1/chat/completions'
        self.__headers = {
            'Authorization': f'Bearer {self.__api_key}',
            'Content-Type': 'application/json',
        }
        self.__body = {
            "model": "gpt-3.5-turbo",
            "temperature": 0.7
        }


    def __send_api_request(self, prompt: str):

        self.__body["messages"] = [{"role": "user", "content": prompt}]

        response = requests.post(
                self.__openai_url,
                headers=self.__headers,
                data=json.dumps(self.__body))

        if response.status_code != 200:
            print("Ocorreu um erro na solicitação:", response.text)
            return None

        return GptResponseModel.parse_obj(response.json())


    def ask_input(self, cli_input: list = None):
        """
        Awaits for an user question if no cli_input was sent

        Paramters
        ---------
            cli_input {list}

        Returns
        -------
            str
        """

        if isinstance(cli_input, list) and len(cli_input) > 1:

            return " ".join(cli_input)

        return input(self.__welcome_question)


    def send_prompt(self, cli_input: list = None) -> GptResponseModel:
        """
        Send the prompt and returns the Response model

        Parameters
        ----------
            cli_input {list}

        Returns
        -------
            GptResponseModel
        """

        prompt = self.ask_input(cli_input)

        return self.__send_api_request(prompt)
