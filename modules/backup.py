from netmiko import ConnectHandler
from datetime import datetime
import logging

def connect_multiple_info(router, commands):
    try:
        connection = ConnectHandler(**router)

        print(f"\n---- {router['host']} ----")

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        output_file = (
            f"backups/{router['host']}_{timestamp}.txt"
        )

        with open(output_file, "w") as file:

            for command in commands:

                output = connection.send_command(command)

                print(f"\n#### {command} ####")
                print(output)

                file.write(
                    f"\n### {command} ###\n"
                )

                file.write(output)
                file.write("\n")

        connection.disconnect()

        print(f"\nBackup saved: {output_file}")

        logging.info(
            f"{router['host']} backup completed: {output_file}"
        )

    except Exception as e:

        print(
            f"{router['host']} backup failed: {e}"
        )

        logging.error(
            f"{router['host']} backup failed: {e}"
        )