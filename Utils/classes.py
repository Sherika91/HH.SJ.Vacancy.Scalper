import os
from abc import ABC, abstractmethod
import requests
from exceptions import ParsingError
from dotenv import load_dotenv


class AbstractAPi(ABC):
    """This is an abstract class for API"""

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    @abstractmethod
    def get_vacancy(vacancy):
        pass


class HeadHunterAPI(AbstractAPi):

    def __init__(self, keyword):
        self.keyword = keyword
        self.api_url = f'https://api.hh.ru/vacancies?text={self.keyword}'
        self.params = {
            "per_page": 20,
            "page": 0,
            "archived": False
        }

        self.header = {"User_Agent": "HHScalperApp 1.0"}
        self.vacancies = []

    def get_request(self):
        count_page = 5
        vacancies = []

        while self.params["page"] < count_page:
            response = requests.get(self.api_url, headers=self.header, params=self.params)
            print(f'{self.__class__.__name__} Loading Page: {self.params["page"]}')
            if response.status_code != 200:
                raise ParsingError(f"Error while trying to get Vacancies, Status: {response.status_code}")
            else:
                data = response.json()["items"]
                vacancies.extend(data)
                self.params["page"] += 1

        return vacancies

    @staticmethod
    def get_vacancy(vacancy):
        try:
            info = {'id': vacancy['id'], 'title': vacancy["name"], 'area': vacancy["area"]["name"], 'employer': vacancy["employer"]["name"],
                    'url': vacancy["alternate_url"], 'requirement': vacancy["snippet"]["requirement"]}

            salary = vacancy["salary"]
            if salary:
                info["salary_from"] = salary["from"]
                info["salary_to"] = salary["to"]
                info["currency"] = salary["currency"]
            else:
                info["salary_from"] = 0
                info["salary_to"] = 0
                info["currency"] = "Not specified"

            return info

        except FileNotFoundError:
            print("File not found!")

        except KeyError:
            print("Key not found!")

    def get_all_vacancies_info(self):
        all_vacancies_info = []
        for vacancy in self.get_request():
            vacancy_info = self.get_vacancy(vacancy)
            all_vacancies_info.append(vacancy_info)

        return all_vacancies_info


class SuperJobAPI(AbstractAPi):
    """Класс для работы с API SuperJob."""
    load_dotenv()
    url = f'https://api.superjob.ru/2.0/vacancies/'
    sj_api_secret_key = os.getenv('SJ_API_SECRET_KEY')

    def __init__(self, keyword):
        self.keyword = keyword
        self.api_url = 'https://api.superjob.ru/2.0/vacancies/'
        self.params = {
            "count": 20,
            "page": 0,
            "keyword": self.keyword,
            "archive": False
        }

        self.header = {
            "X-Api-App-Id": self.sj_api_secret_key
        }
        self.vacancies = []

    def get_request(self):
        vacancies_tmp = []
        count = 5

        while self.params["page"] < count:

            response = requests.get(self.api_url, headers=self.header, params=self.params)
            if response.status_code == 200:
                print(f'{self.__class__.__name__} Loading Page: {self.params["page"]}')
                data = response.json()
                vacancies_tmp.extend(data['objects'])
                self.params['page'] += 1
            else:
                raise ParsingError(f"Error while trying to get Vacancies, Status: {response.status_code}")
        filtered_vacancies = self.get_vacancy(vacancies_tmp)
        self.vacancies.extend(filtered_vacancies)

    @staticmethod
    def get_vacancy(vacancy_data: list) -> list:
        try:
            """
               Функция извлекает и конвертирует данные о вакансиях.

               """
            vacancies = []

            for vacancy in vacancy_data:
                if not vacancy["is_closed"]:
                    payment_from = vacancy['payment_from'] if vacancy['payment_from'] is not None else 0
                    payment_to = vacancy['payment_to'] if vacancy['payment_to'] is not None else 0
                    processed_vacancy = {
                        'platform': "SuperJob",
                        "id": vacancy["id"],
                        'title': vacancy['profession'],
                        'employer': vacancy['firm_name'],
                        'url': vacancy['link'],
                        'area': vacancy['town']['title'],
                        'salary_from': payment_from,
                        'salary_to': payment_to,
                        'currency': vacancy["currency"]
                    }
                    vacancies.append(processed_vacancy)

            return vacancies

        except FileNotFoundError:
            print("File not found!")

        except KeyError:
            print("Key not found!")

    def get_all_vacancies_info(self):
        self.get_request()
        return self.vacancies
