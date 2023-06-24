from Utils.json_saver import JSONSaver


class Vacancy(JSONSaver):

    def __init__(self, title, area, employer, url, salary_from, salary_to, currency, requirement):
        super().__init__()
        self.title = title
        self.area = area
        self.employer = employer
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirement = requirement

    def __str__(self):
        return f"{self.title}, {self.area}," \
               f"{self.employer}," \
               f"{self.salary_from}{self.currency} --> {self.salary_to}{self.currency}" \
               f"{self.url}," \
               f"{self.requirement}"
