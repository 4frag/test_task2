docker cp ./test_task2.dump test_task2-postgres:/
docker exec test_task2-postgres pg_restore -U test_task2 -d test_task2 test_task2.dump
