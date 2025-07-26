docker cp ./dump.sql test_task2-postgres:/
docker exec test_task2-postgres psql -U test_task2 -d test_task2 < dump.sql
