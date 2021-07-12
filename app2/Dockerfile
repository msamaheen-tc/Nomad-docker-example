FROM python:3.8
RUN pip3 install uvicorn fastapi asyncio
COPY . .
CMD ["uvicorn", "script2:app", "--host", "0.0.0.0", "--port", "1116"]