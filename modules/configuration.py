from napalm import get_network_driver
import logging


driver = get_network_driver("ios")


def napalm_configure(router, config):
    try:
        device = driver(
            router["host"],
            router["username"],
            router["password"]
        )

        device.open()

        device.load_merge_candidate(config=config)

        print(
            f"\n---- NAPALM Configure: {router['host']} ----"
        )

        diff = device.compare_config()

        print(diff)

        # Idempotency: commit only when changes exist
        if diff:

            device.commit_config()

            print("Configuration committed.")

            logging.info(
                f"{router['host']} NAPALM configuration committed"
            )

        else:

            print("No changes required.")

            logging.info(
                f"{router['host']} already has the required configuration"
            )

        device.close()

    except Exception as e:

        print(
            f"{router['host']} NAPALM configuration failed: {e}"
        )

        logging.error(
            f"{router['host']} NAPALM configuration failed: {e}"
        )