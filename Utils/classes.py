from abc import ABC, abstractmethod
import requests
from utils.exeptions import ParsingError


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
            "page": 20,
            "archived": False
        }

        self.header = {"User_Agent": "HHScalperApp 1.0"}
        self.vacancies = []

    def get_request(self):
        response = requests.get(self.api_url, headers=self.header, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Error while trying to get Vacancies, Status: {response.status_code}")
        return response.json()["items"]

    @staticmethod
    def get_vacancy(vacancy):
        try:
            info = {'title': vacancy["name"], 'area': vacancy["area"]["name"], 'employer': vacancy["employer"]["name"],
                    'url': vacancy["area"]["url"], 'requirement': vacancy["snippet"]["requirement"]}

            salary = vacancy["salary"]
            if salary:
                info["salary"] = salary["from"]
                info["salary_to"] = salary["to"]
                info["currency"] = salary["currency"]
            else:
                info["salary"] = "No details"
                info["salary_to"] = "Not specified"
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



class 
# usinp = "Java Developer"
# hh = HeadHunterAPI(usinp)
# print(hh.get_all_vacancies_info())



    # @staticmethod
    # def get_formatted_vacancies(keyword):
    #
    #     for vacancy in keyword[0]["items"]:
    #         title = vacancy["name"]
    #         area = vacancy["area"]["name"]
    #         employer = vacancy["employer"]["name"]
    #         url = vacancy['area']['url']
    #         salary_from = vacancy['salary']['from']
    #         salary_to = vacancy['salary']['to']
    #         requirement = vacancy['snippet']['requirement']
    #         vac = Vacancy(title, area, employer, url, salary_from, salary_to, requirement)
    #         list_vacancy_hh_sj.append(vac)
    #


        # formatted_vacancy = {
        #     "api": "HeadHunter",
        #     "area": vacancy["area"]["name"],
        #     "employer": vacancy["employer"]["name"],
        #     "requirement": vacancy["snippet"]["requirement"],
        #     "title": vacancy["name"],
        #     "url": vacancy["alternate_url"],
        #
        # }
        #
        # salary = vacancy["salary"]
        # if salary:
        #     formatted_vacancy["salary"] = salary["from"]
        #     formatted_vacancy["salary_to"] = salary["to"]
        #     formatted_vacancy["currency"] = salary["currency"]
        # else:
        #     formatted_vacancy["salary"] = "No details"
        #     formatted_vacancy["salary_to"] = "Not specified"
        #     formatted_vacancy["currency"] = "Not specified"
        #
        # formatted_vacancies.append(formatted_vacancy)
        # vacancy_hh = Vacancy()

