docker cp ./test_task2.dump test_task2-postgres:/
docker exec test_task2-postgres pg_restore -d test_task2 test_task2.dump
