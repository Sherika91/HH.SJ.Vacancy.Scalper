from configparser import ParsingError
import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_request(self):
        pass


class HeadHunterAPI(AbstractAPI):
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, keyword):
        self.params = {
            "per_page": 100,
            "page": 0,
            "test": keyword,
            "archived": False
        }
        self.header = {
            "User_Agent": "HHScalperApp 1.0"
        }
        self.vacancies = []

    def get_request(self):
        response = requests.get(self.url, headers=self.header, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Error while trying to get Vacancies! Status: {response.status_code}")
        return response.json()["items"]

    def get_formatted_vacancies(self):
        formatted_vacancies = []

        for vacansy in self.vacancies:
            formatted_vacancy = {
                "employer": vacansy["employer"]["name"],
                "title": vacansy["name"],
                "url": vacansy["alternate_url"],
                "api": "HeadHunter",
            }
            salary = vacansy["salary"]
            if salary:
                formatted_vacancy["salary"] = salary["from"]
                formatted_vacancy["salary_to"] = salary["to"]
                formatted_vacancy["currency"] = salary["currency"]
            else:
                formatted_vacancy["salary"] = None
                formatted_vacancy["salary_to"] = None
                formatted_vacancy["currency"] = None
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies

    def get_vacancies(self, pages_count=2):
        self.vacancies = []
        for page_ in range(pages_count):
            page_vacancies = []
            self.params["page"] = page_
            print(f"({self.__class__.__name__}) Parceing page {page_} -", end=" ")
            try:
                page_vacancies = self.get_request()
            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f"Loaded vacancies: {len(page_vacancies)}")
            if len(page_vacancies) == 0:
                break

hh = HeadHunterAPI
print(hh.get_request)
# class SuperJobAPI(AbstractAPI, ABC):
#     def get_vacancies(self):
#         # реализация запроса к API SuperJob
#         pass
