#### Requirements

- Python 3.12.1
- pip (Python package installer)
- virtualenv or venv module

#### Setup Instructions

1. Create and activate a virtual environment:

f you prefer to run the application without Docker, you can set up a local Python environment:

bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python run.py


bash
pytest -s tests

pytest -s tests/test_prices_controller.py::test_get_prices
