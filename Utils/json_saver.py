import json
from abc import ABC, abstractmethod
from utils import Classes


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def save_as_json(self):
        pass


class JSONSaver(AbstractAPI):
    """Класс, который сохраняет все вакансии в json файл."""

    def save_as_json(self):
        api_hh = Classes.HeadHunterAPI()
        # api_sj = SuperJobApi()
        api = [api_hh.get_request()]

        with open("../vacancies.json", "w", encoding="utf-8") as file:
            json.dump(api, file, sort_keys=False, indent=2, ensure_ascii=False)
    #
    # def save_data(self):
    #     data = []
    #     for vacancy in self.vacancies:
    #         data.append({
    #             "title": vacancy.title,
    #             "url": vacancy.link,
    #             "salary_from": vacancy.salary,
    #             "salary_to": vacancy.salary_to,
    #             "description": vacancy.description
    #         })
    #
    # def add_vacancy(self, vacancy):
    #     from vacansy import Vacancy
    #     if isinstance(vacancy, Vacancy):
    #         self.vacancies.append(vacancy)
    #     self.save_data()
    #
    # def get_vacancies_by_salary(self, salary_range):
    #     result = []
    #     for vacancy in self.vacancies:
    #         if vacancy.salary == salary_range:
    #             result.append(vacancy)
    #     return result
    #
    # def delete_vacancy(self, vacancy):
    #     if vacancy in self.vacancies:
    #         self.vacancies.remove(vacancy)
    #     self.save_data()
