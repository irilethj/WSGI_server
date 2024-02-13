import json
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def simple_app(environ, start_response):
    query_string = environ.get('QUERY_STRING', '')
    get_parameters = parse_qs(query_string)

    species = {'Cyberman': 'John Lumic',
               'Dalek': 'Davros',
               'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
               'Human': 'Leonardo da Vinci',
               'Ood': 'Klineman Halpen',
               'Silence': 'Tasha Lem',
               'Slitheen': 'Coca-Cola salesman',
               'Sontaran': 'General Staal',
               'Time Lord': 'Rassilon',
               'Weeping Angel': 'The Division Representative',
               'Zygon': 'Broton'}

    if 'species' in get_parameters and get_parameters['species'][0] in species:
        status = '200 OK'
        response_body = json.dumps(
            {"credentials": species[get_parameters['species'][0]]})
    else:
        status = '404 Not Found'
        response_body = json.dumps({"credentials": "Unknown"})

    headers = [('Content-type', 'application/json; charset=utf-8')]

    start_response(status, headers)

    return [response_body.encode('utf-8')]


if __name__ == "__main__":
    with make_server('', 8888, simple_app) as httpd:
        print("Serving HTTP on port 8888...")
        httpd.serve_forever()
