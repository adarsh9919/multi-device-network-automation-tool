from netmiko import ConnectHandler
import logging


def verify_configuration(router):
    try:
        connection = ConnectHandler(**router)

        output = connection.send_command(
            "show running-config | section interface GigabitEthernet0/1"
        )

        print(
            f"\n--- Verification {router['host']} ---"
        )

        print(output)

        logging.info(
            f"{router['host']} configuration verification completed"
        )

        connection.disconnect()

    except Exception as e:

        logging.error(
            f"{router['host']} verification failed: {e}"
        )

        print(
            f"{router['host']} verification failed: {e}"
        )