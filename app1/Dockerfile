FROM python:3.8
RUN pip3 install uvicorn fastapi asyncio requests
COPY . .
CMD ["uvicorn", "script1:app", "--host", "0.0.0.0", "--port", "1117"]