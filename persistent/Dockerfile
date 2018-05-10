FROM nestorld/pytest:release-PYTEST-v1.1.3

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8300

CMD ["python", "persistent_test.py"]
