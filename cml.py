import os
import click
import json
import simplejson
import yaml
from yaml.loader import SafeLoader
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml



# The aim of this function parse and converts a yaml object to python dictionary(deserializing YAML to Python)
with open(r'test.yaml') as f:
    data = yaml.load(f, SafeLoader)

@click.group()
def cli():
  pass    

# The aim of this function convert python dictionary to json data and dispaly on html(serializing python object to json)
@cli.command(name='tohtml')
def dict_to_html():
    dataonhtml = ""
    for k in data:
	    dataonhtml += "<td>" + k + "</td>"
	    for d in data[k]:
		    dataonhtml += "<td>" + d + "</td>"
	    dataonhtml += "<tr>"

    dataonhtml = "<table border=1>" + dataonhtml + "<table>"
    with open("file.html", "w") as file:
	    file.write(dataonhtml)
    os.system('open %s' % "file.html")
    


# The aim of this function convert python dictionary to xml data and dispaly on pretty text format after pasring(serializing python object to xml)
@cli.command(name='toxml')
def dict_to_xml():
    xml = dicttoxml(data)
    dom = parseString(xml)
    click.echo(dom.toprettyxml())

# The aim of this function convert python dictionary to json and save into a file
@cli.command(name='savejson')
def save_json_file():
    with open('result.json','w') as fp:
        json.dump(data,fp)



if __name__ == '__main__':
    cli()