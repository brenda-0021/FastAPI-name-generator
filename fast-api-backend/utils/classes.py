import requests

class APIException(Exception):
    def __init__(self, message, status_code):
        self.status_code = status_code
        super().__init__(message)

class RandomNameGenerator:
    def __init__(self, nationality, country, gender):
        self.nationality = nationality
        self.country = country
        self.gender = gender

    def make_appropriate_url(self):
        if self.gender == self.country == "none":
            url = "https://api.namefake.com/"
        elif self.country == "none":
            url = "https://api.namefake.com/" + self.gender + "/"
        elif self.gender == "none":
            url = "https://api.namefake.com/" + self.nationality + "-" + self.country + "/"
        else:
            url = "https://api.namefake.com/" + self.nationality + "-" + self.country + "/" + self.gender + "/"
        return url

    def make_api_call(self, count=1):  # Aceptar un parámetro count
        names = []  # Lista para almacenar los nombres generados

        for _ in range(count):  # Generar la cantidad de nombres solicitada
            retry = 0
            max_retry = 5
            response = None

            while retry < max_retry:
                try:
                    response = requests.get(self.make_appropriate_url())
                    response.raise_for_status()
                    break
                except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as err:
                    retry += 1
                    if retry == max_retry:
                        raise APIException('Connection Timeout', 503)
                except requests.exceptions.RequestException as err:
                    raise APIException(str(err), 500)

            # Agregar el nombre generado a la lista
            names.append(response.json()['name'])

        return names  # Devolver la lista de nombres generados
