import subprocess
import time
import pandas as pd


TOKEN = input('Input SPL Token Public Key (Address): ')


def main():

    if TOKEN == '':
        raise ValueError('Please Enter Token SPL Address')

    df = pd.read_csv('airdrops.csv')
    results = []

    try:
        for row in df.itertuples():
            rec = row.owner
            cmd = ["spl-token", "transfer", TOKEN, row.total, rec,  "--allow-unfunded-recipient", "--fund-recipient"]
            send = subprocess.Popen(cmd)
            send.communicate()
            time.sleep(2)

            results.append([False, rec] if send.returncode != 0 else [True, rec])

    finally:
        pd.DataFrame(results).to_csv('results.csv')


if __name__ == '__main__':
    main()


