### Discription
This smal project try to solve problem discribed in the following link https://kata-log.rocks/configure-wardrobe-kata. Chosen solution seeks to apply layer architecture.

### Tree
```
.
├── Pipfile
├── Pipfile.lock
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
    ├── app_main.py
    ├── calc_score_logic.py
    ├── combinations_logic.py
    ├── data_from_user.py
    ├── __init__.py
    ├── tests
    │   ├── __init__.py
    │   └── logic_tests.py
    ├── wall.py
    └── wardrobe.py
```
### Questions
- we need to reorganize folders e.g:
    create folder domain and put application logic to this folder? 
- app_maim.py is a service layer? I thing is desired.
- data_from_user.py can be a contoller in the sens of "clean architecture"?
- is necesary to split tests for separate files? I thing is desired.
