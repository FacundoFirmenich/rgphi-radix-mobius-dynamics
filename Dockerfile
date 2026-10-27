FROM python:3.12-slim
WORKDIR /work
COPY . /work
RUN python -m pip install --no-cache-dir -e .
CMD ["rgphi", "verify"]
