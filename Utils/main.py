import sys
from Utils.classes import HeadHunterAPI, SuperJobAPI
from Utils.json_saver import JSONSaver


def user_interaction():
    """Function for user interaction"""
    while True:
        search_query = input("\nEnter a query to search for vacancies: ").strip()
        if search_query.isnumeric() or len(search_query) == 0:
            print("Please enter a valid search query")

        else:
            break

    head_hunter_api = HeadHunterAPI(search_query)
    super_jb_api = SuperJobAPI(search_query)
    json_saver = JSONSaver()

    platforms = {"hh": head_hunter_api, "sj": super_jb_api}
    selected_platforms = []

    for name, platform in platforms.items():
        print(f"Do you want to get vacancies from this platform ? --> {name.title()}? (Yes/No)")
        answer = input()
        if answer.lower() == "yes":
            selected_platforms.append(platform)

    vacancies = []

    for platform in selected_platforms:
        platform_vacancies = platform.get_all_vacancies_info()
        vacancies.extend(platform_vacancies)
    json_saver.save_as_json(vacancies)

    data = json_saver.load_data()

    print("\nChose command to continue.\n"
          "1. - Output ll vacancies\n"
          "2. - Get vacancy by salary\n"
          "3. - Get vacancy by Top salary\n"         
          "4. - Get vacancy by city\n"
          "5. - Save data as CSV\n"
          "0. - Exit the program\n")

    while True:

        answer = input()
        if answer == "1":
            for vacancy in data:
                print(vacancy)
                print("_" * 60)

        elif answer == "2":
            usr_input_2 = input("Enter top salary: ")
            for vacancy in json_saver.get_vacancies_by_salary(usr_input_2):
                if vacancy == "No vacancies found":
                    print(vacancy)
                else:
                    print(vacancy)
                    print("_" * 60)

        elif answer == "3":
            usr_input_3 = input("Enter count of top vacancies: ")
            for vacancy in json_saver.get_top_vacancies(usr_input_3):
                print(vacancy)
                print("_" * 60)

        elif answer == "4":
            usr_input_4 = input("Enter city: ").title()
            for vacancy in json_saver.get_vacancy_by_city(usr_input_4):
                print(vacancy)
                print("_" * 60)

        elif answer == "5":
            json_saver.save_data_as_csv()

        elif answer == "0":
            print("Goodbye!")
            sys.exit()
        else:
            print("No such command :(")


if __name__ == "__main__":
    user_interaction()
