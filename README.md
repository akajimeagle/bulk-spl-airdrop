# bulk-spl-airdrop

----
#### Airdrop a list of SPL Tokens to a CSV of Wallet Addresses and their respective totals. 


## Prerequisites
* [Solana Tool Suite](https://docs.solana.com/cli/install-solana-cli-tools)
* [SPL Token CLI](https://spl.solana.com/token)
* [Python 3.9 or higher](https://www.python.org/downloads/release/python-3913/)
* ```airdrops.csv``` with correct information.
* ```solana config get``` settings correct *[Connected to correct cluster with correct wallet & config.]*
* The Solana wallet should have enough funds to cover the airdrop and account creation costs. 
  * (~ 0.00204428 SOL * Individual Accounts)

## Usage
* ```git clone https://github.com/ehutzle/bulk-spl-airdrop.git```
* ```cd bulk-spl-airdrop```
* configure and activate virtual environment: 
  * ```python3.9 -m venv venv```
  * ```source venv/bin/activate```
  * ```pip3 install -r requirements.txt```
* run script ```python3 airdrop.py```

## Special Notes
* It costs 0.00204428 SOL to airdrop a token to a wallet that does not have an account for the SPL token open.
