from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_job_types = set()
    for job in jobs_list:
        unique_job_types.add(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)

    return jobs_filtered


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_filtered_by_industry = []

    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered_by_industry.append(job)

    print(jobs_filtered_by_industry)
    return jobs_filtered_by_industry


def get_max_salary(path):
    jobs_list = read(path)
    salaries = []

    for job in jobs_list:
        # ESSA CONDIÇÃO FOI VERIFICADA DE DUAS FORMAS:
        # UMA IDENTIFICANDO O QUEM VEM jobs_list["max_salary"],
        # PARA ELIMINAR OS SALÁRIOS " "
        # A OUTRA OLHANDO O ARQUIVO DE MOCK, jobs_with_salaries.csv
        # QUE PASSA NA COLUNA max_salary UM 'invalid',
        # POIS ANTES DE TRATAR ESSA SEGUNDA CONDIÇÃO,
        # DAVA O ERRO: ValueError (...) 'invalid'
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            salaries.append(int(job["max_salary"]))

    # print("Salário máximo encontrado: ", (max(salaries)))
    return max(salaries)


def get_min_salary(path):
    jobs_list = read(path)
    salaries = []

    for job in jobs_list:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            salaries.append(int(job["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job
    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job
    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise
    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    # PARA CADA IF ESTÁ SENDO LEVANTADO O ERRO ValueError
    # CONFORME MOSTRA A DOCUMENTAÇÃO EM 8.4. Levantando exceções
    # (https://docs.python.org)
    if ("min_salary" not in job) or ("max_salary" not in job):
        # raise = levantar
        raise ValueError

    if (type(job["min_salary"]) != int) or (type(job["max_salary"]) != int):
        raise ValueError

    if job["min_salary"] > job["max_salary"]:
        raise ValueError

    if type(salary) != int:
        raise ValueError

    result = salary >= job["min_salary"] and salary <= job["max_salary"]
    return result


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
