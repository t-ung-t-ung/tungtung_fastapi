import subprocess
import asyncio
import os

async def main():
    while True:
        try:
            message = subprocess.check_output(
                'sh -c "docker exec -i tungtung_mysql sh -c \'exec mysql -uroot -p$MYSQL_ROOT_PASSWORD\' < scripts/init.sql"',
                shell=True,
                stderr=subprocess.STDOUT
            ).decode()
            print(message)
        except subprocess.CalledProcessError as e:
            print("processing", e.stderr, e.output, e.cmd, e.stdout)
            await asyncio.sleep(1)
            continue

        break
    print("completed.")


asyncio.run(main())
