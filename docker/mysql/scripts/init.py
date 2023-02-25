import subprocess
import asyncio


async def main():
    while True:
        try:
            message = subprocess.check_output(
                'docker exec -i tungtung_mysql sh -c \'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"\' < scripts/init.sql',
                shell=True,
                stderr=subprocess.PIPE
            ).decode()
        except subprocess.CalledProcessError as e:
            print("processing")
            await asyncio.sleep(1)
            continue

        break
    print("completed.")


asyncio.run(main())
