#!/usr/bin/env python3
import os
import sys
import requests


def deserialize(path: str) -> list[dict]:
    """List all files in the given dir and deserialize them
        Parameters:
            path (str): path to assess
        Returns:
            deserialized_data (list[dict]): list of dictionaries deserialized from the files
    """
    os.chdir(path)
    list_dict = []
    index_key = ['title', 'name', 'date', 'feedback']
    for file in os.listdir():
        with open(file, 'r') as f:
            feedback_dict = {}
            for key in index_key:
                feedback_dict[key] = f.readline().strip()
            list_dict.append(feedback_dict)
    return list_dict


dict_lst = deserialize('/Users/francis/PycharmProjects/communication_btw_files_and_webserver/examples')
for feedback in dict_lst:
    x = requests.post('http://34.123.3.50/feedback/', data=feedback)
    print(x.reason)


if __name__ == '__main__':
    print(deserialize(sys.argv[1]))
