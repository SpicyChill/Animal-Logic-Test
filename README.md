# Animal-Logic-Test
Write a command-line tool in python that takes some sets of personal data (name, address, phone number) and serialise them/deserialise them in at least 2 formats, and also display the data it in at least 2 different ways.

test.yaml is the input file with test data includes name, number, address

In cml.py we have three commands:
dict_to_html()
The aim of this command convert python dictionary to json data and dispaly on html (serializing python object to json)

dict_to_xml()
The aim of this command convert python dictionary to xml data and dispaly on pretty text format after pasring (serializing python object to xml)

save_json_file()
The aim of this command convert python dictionary to json and save into a json file

How to run:
Type the following commands in your terminal each time choose one command
python cml.py dict_to_html
python cml.py dict_to_xml
python cml.py save_json_file
