This repository contains a collection of simple Python scripts created as part of a learning journey in Python
programming.

📚 Contents
This project contains automated UI tests for OpenCart using Selenium, pytest, and webdriver-manager.

🚀 How to Run Tests
This explains how to run the test_opencart.py test with different params using command-line options.

```bash
pytest src/test/ --browser=chrome --executor=local --base_url=http://192.168.0.30:8080 --alluredir=allure-results
```

```bash
allure serve allure-results
```

🚀 How to Run Tests in Docker
- Run docker-compose-selenoid.yml
- Run docker-compose.yml

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