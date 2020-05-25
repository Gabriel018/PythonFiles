from covid import Covid

covid = Covid()

def covid_mundo():
    print(covid.get_total_active_cases())
    print(covid.get_total_deaths())
    print(covid.get_status_by_country_name("Brazil"))

covid_mundo()

