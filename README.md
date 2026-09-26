# creditOptimizer

## To run the virtual enviroment follow the next steps:

1. Create the virtual enviroment

```python
python -m venv venv
```

2. Activate the virtual enviroment

``cd /venv/Scripts``

``activate`` or ``.\activate``

``cd ../../``

3. Install uvicorn

```python
pip install uvicorn
```

4. Install Fastapi

```python
pip install fastapi
```

## Run app with python:

```python
python main.py
```

## Run app with uvicorn:

``
uvicorn presentation.webapicreditoptimizer:app --host {your_ip} --port 7000 --reload
``
