# chapter 7

`python`
pip install "fastapi[standard]"
pip install "uvicorn[standard]"
`python`

`bash`
uvicorn app.main:app --relaod
`bash`

**
Body() diffrence with Body()
**

```bash
docker run --rm  --name my-postgres \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=test \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  --network fastapi_network\
  -d postgres:18.4-alpine
```
