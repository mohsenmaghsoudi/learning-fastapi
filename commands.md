# chapter 7

`python`
pip install "fastapi[standard]"
pip install "uvicorn[standard]"
pip install "pip install "psycopg[binary,pool]" ##pool dont install yet
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
  -v pgdata:/var/lib/postgresql \
  --network fastapi_network\
  -d postgres:18.4-alpine
```

```bash
docker run --rm -d \
  --name my-pgadmin \
  --network fastapi-network \
  -p 9999:80 \
  -e 'PGADMIN_DEFAULT_EMAIL=admin@admin.com' \
  -e 'PGADMIN_DEFAULT_PASSWORD=admin' \
  -v pgadmin_data:/var/lib/pgadmin \
  dpage/pgadmin4
```
