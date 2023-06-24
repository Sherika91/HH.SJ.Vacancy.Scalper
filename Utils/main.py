from utils import Classes

# Создание экземпляра класса для работы с API сайтов с вакансиями
# superjob_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = Classes.HeadHunterAPI

# superjob_vacancies = superjob_api.get_vacancies("Python")

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем


def user_interaction():
    search_query = input("Enter a query to search for vacancies: ")
    list_vacancy_hh_sj = []

    head_hunter_api = Classes.HeadHunterAPI(search_query)
    # super_jb_api = SuperJobAPI()
    # json_saver = JSONSaver()

    # platforms = {"hh": hh_api, "sj": super_jb_api}
    platforms = {"hh": head_hunter_api}
    selected_platforms = []

    for name, platform in platforms.items():
        print(f"Do you want to get vacancies from this platform ? --> {name.title()}? (Yes/No)")
        answer = input()
        if answer.lower() == "yes":
            selected_platforms.append(platform)

    vacancies = []
    for platform in selected_platforms:
        platform_vacancies = platform.get_vacancy(platform.get_request())
        vacancies.append(platform_vacancies)
        return vacancies

    print(vacancies)





    # for vacan in list_vacancy_hh_sj:
    #     if search_query == vacan.title:
    #         print(vacan)
    #     else:
    #         print(f"Нет вакансий, соответствующих заданным критериям.")

    # def get_formatted_vacancies(self):
    #     formatted_vacancies = []
    #
    #     for vacancy in self.get_request():
    #         formatted_vacancy = {
    #             "api": "HeadHunter",
    #             "area": vacancy["area"]["name"],
    #             "employer": vacancy["employer"]["name"],
    #             "requirement": vacancy["snippet"]["requirement"],
    #             "title": vacancy["name"],
    #             "url": vacancy["alternate_url"],
    #
    #         }
    #         salary = vacancy["salary"]
    #
    #         if salary:
    #             formatted_vacancy["salary"] = salary["from"]
    #             formatted_vacancy["salary_to"] = salary["to"]
    #             formatted_vacancy["currency"] = salary["currency"]
    #         else:
    #             formatted_vacancy["salary"] = None
    #             formatted_vacancy["salary_to"] = None
    #             formatted_vacancy["currency"] = None
    #
    #         formatted_vacancies.append(formatted_vacancy)
    #
    #     return formatted_vacancies

    # for vacancy in list_vacancy_hh_sj:
    #     print(list_vacancy_hh_sj)

    # print('{title}, {employer}\n'
    #       '{area}\n'
    #       '{salary_from} --> {salary_to}\n'
    #       '{requirement}\n'
    #       '{url}\n'.format(title=vacancy["name"], employer=vacancy["employer"]["name"],
    #                        area=vacancy["area"]["name"],
    #                        salary_from=["salary"][int("from")], salary_to=["salary"][int("to")],
    #                        url=vacancy["area"]["url"],
    #                        requirement=vacancy["snippet"]["requirement"],
    #                        )
    #       )

    # vacancy_ = Vacancy(title=vacancy["name"], area=vacancy["area"]["name"],
    #                    employer=vacancy["employer"]["name"],
    #                    url=vacancy['area']['url'],
    #                    salary_from=vacancy["salary"][int("from")], salary_to=vacancy["salary"][int("to")],
    #                    requirement=vacancy['snippet']['requirement'])
    #
    # print(vacancy_)


if __name__ == "__main__":
    user_interaction()
