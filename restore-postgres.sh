docker cp ./dump.sql test_task2-postgres:/
docker exec test_task2-postgres psql -U test_task2 test_task2 -f dump.sql
