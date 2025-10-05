This repository contains a collection of simple Python scripts created as part of a learning journey in Python
programming.

📚 Contents
This project contains automated UI tests for OpenCart using Selenium, pytest, and webdriver-manager.

🚀 How to Run Tests
This explains how to run the test_opencart.py test with different params using command-line options.

```bash
pytest src/test/ --browser=chrome --base_url=http://localhost:8080 --alluredir=allure-results
```
```bash
allure serve allure-results
```

✅ Requirements
Python 3.7 or higher, pytest, selenium, webdriver-manager, allure

- To check your version:

```bash
python --version
```

- Install dependencies

```bash
pip install -r requirements.txt
```
```bash
docker build . -t tests
```
```bash
docker run -it tests src/test/ --browser=firefox --base_url=http://host.docker.internal:8080 --alluredir=allure-results
```