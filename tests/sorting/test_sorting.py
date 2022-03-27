import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-24"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-12"},
        {"max_salary": 500, "min_salary": 100, "date_posted": "1987-02-19"},
        {"max_salary": 50000, "min_salary": 1000, "date_posted": "1997-10-30"},
    ]

    expected_ordering_min_salary = [
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-12"},
        {"max_salary": 500, "min_salary": 100, "date_posted": "1987-02-19"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-24"},
        {"max_salary": 50000, "min_salary": 1000, "date_posted": "1997-10-30"},
    ]

    expected_ordering_max_salary = [
        {"max_salary": 50000, "min_salary": 1000, "date_posted": "1997-10-30"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-24"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-12"},
        {"max_salary": 500, "min_salary": 100, "date_posted": "1987-02-19"},
    ]

    expected_ordering_date_posted = [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-01-24"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-06-12"},
        {"max_salary": 50000, "min_salary": 1000, "date_posted": "1997-10-30"},
        {"max_salary": 500, "min_salary": 100, "date_posted": "1987-02-19"},
    ]

    assert sort_by(jobs, "min_salary") == expected_ordering_min_salary
    assert sort_by(jobs, "max_salary") == expected_ordering_max_salary
    assert sort_by(jobs, "date_posted") == expected_ordering_date_posted

    invalid_criteria = ["job_type", None]

    for criteria in invalid_criteria:
        with pytest.raises(ValueError):
            sort_by(jobs, criteria)
