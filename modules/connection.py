from netmiko import ConnectHandler
import logging

def connection_check(router):
    try:
        connection = ConnectHandler(**router)
        connection.disconnect()

        logging.info(
            f"{router['host']} connection successful"
        )

        return True

    except Exception as e:
        logging.error(
            f"{router['host']} connection failed: {e}"
        )

        print(
            f"{router['host']} failed to connect: {e}"
        )

        return False