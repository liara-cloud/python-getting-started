# Python + Liara Object Storage

## How to work

```
git clone https://github.com/liara-cloud/python-getting-started.git
```
```
cd python-getting-started
```
```
git checkout object-storage
```
```
mv .env.example .env # and set ENVs
```
```
pip install virtualenv
```
```
python -m venv .venv
```
```
source .venv/bin/activate # (on Windows: .venv\Scripts\activate)
```
```
pip install -r requirements.txt
```
```
python app.py
```

check `localhost:8000` to use object storage

## More info?

- [Liara Docs](https://docs.liara.ir/object-storage/how-tos/connect-via-platform/python/)
- [Boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html)