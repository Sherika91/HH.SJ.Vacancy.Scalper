import json
import csv
from abc import ABC, abstractmethod
from Utils.vacansy import Vacancy


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def save_as_json(self, data):
        pass


class JSONSaver(AbstractAPI):
    """Класс, который сохраняет все вакансии в json файл."""

    def save_as_json(self, data):

        with open("../vacancies.json", "w", encoding="utf-8") as file:
            json.dump(data, file, sort_keys=False, indent=2, ensure_ascii=False)

    @staticmethod
    def load_data():
        with open("../vacancies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        vacancies = []
        for vacancy in data:
            id_ = vacancy["id"]
            title = vacancy["title"]
            area = vacancy["area"]
            employer = vacancy["employer"]
            url = vacancy["url"]
            salary_from = vacancy["salary_from"]
            salary_to = vacancy["salary_to"]
            currency = vacancy["currency"]
            vacancies.append(Vacancy(id_, title, area, employer, url, salary_from, salary_to, currency))
        return vacancies

    def add_vacancy(self, vacancy):
        with open("../vacancies.json", encoding="utf-8") as file:
            data = json.load(file)
        data.append(vacancy)
        self.save_as_json(data)

    @staticmethod
    def save_data_as_csv():
        """Saves data as csv file"""
        with open("../vacancies.json", encoding="utf-8") as file:
            data = json.load(file)
        with open("../vacancies.csv", "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(("id", "Title", "Area", "Employer", "Url", "Salary_from", "Salary_to", "Currency"))
            for vacancy in data:
                writer.writerow((vacancy["id"], vacancy["title"], vacancy["area"], vacancy["employer"], vacancy["url"],
                                 vacancy["salary_from"], vacancy["salary_to"], vacancy["currency"]))

    @staticmethod
    def get_vacancies_by_salary(salary_range):
        """Returns vacancies by salary"""
        with open("../vacancies.json", encoding="utf-8") as file:
            data = json.load(file)
        result = []
        for vacancy in data:
            if vacancy["salary_from"] is None:
                continue
            elif vacancy["salary_from"] >= int(salary_range):
                result.append(Vacancy(vacancy["id"], vacancy["title"],
                                      vacancy["area"], vacancy["employer"],
                                      vacancy["url"], vacancy["salary_from"],
                                      vacancy["salary_to"], vacancy["currency"]))
            else:
                if len(result) == 0:
                    result.append("No vacancies found")

        return result

    @staticmethod
    def get_top_vacancies(count):
        """Returns top vacancies by salary"""
        with open("../vacancies.json", encoding="utf-8") as file:
            data = json.load(file)
        result = []
        for vacancy in data:
            if vacancy["salary_from"] is None:
                continue
            else:
                res = sorted(vacancy, key=lambda x: x["salary_from"], reverse=True)
                result.append(res)

        return result[:count]

    @staticmethod
    def get_vacancy_by_city(city):
        """Returns vacancies by city"""
        with open("../vacancies.json", encoding="utf-8") as file:
            data = json.load(file)
        result = []
        for vacancy in data:
            if vacancy["area"] == city:
                result.append(Vacancy(vacancy["id"], vacancy["title"],
                                      vacancy["area"], vacancy["employer"],
                                      vacancy["url"], vacancy["salary_from"],
                                      vacancy["salary_to"], vacancy["currency"]))
            else:
                if len(result) == 0:
                    result.append("No vacancies found in this city")
        return result
