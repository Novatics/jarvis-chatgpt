#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Claudio Cavalcante 
"""

import sys


from services.chatgpt_api import ChatgptApiBusiness

def main():
    """
    Process the chatgpt request
    """
    params = sys.argv[1:]

    gpt_business = ChatgptApiBusiness()

    answer = gpt_business.send_prompt(params)

    print(answer.get_answer())


if __name__ == '__main__':
    main()
