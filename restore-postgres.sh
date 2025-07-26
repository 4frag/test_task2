docker cp ./test_task2.dump test_task2-postgres:/
docker exec test_task2-postgres pg_restore test_task2.dump
