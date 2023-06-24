from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config   # helps in accessing our environment variables

# !!!! Select Mode !!!!
MODE = "DEVLOPMENT"

#Close all open positions and orders
ABORT_ALL_POSITIONS = True

#Find Cointegrated Pirs
FIND_COINTEGRATED = False

#place trades
MANAGE_EXITS = True

# PLACE TRADES
PLACE_TRADES = True

#RESOLUTION
RESOLUTION = "1HOUR"

#STATS WINDOW 
WINDOW = 21

#THRESHOLDS - OPENING
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1900

#THRESHOLD FOR CLOSING 
CLOSE_AT_ZSCORE_CROSS = True

#ETHERIUM ADDRESS
ETHEREUM_ADDRESS = "0x9e2638AB8796c9aeE7281B92235CAbaFC1C2C339"


#KEYS - PRODUCTIONS
#MUST BE ON MAINNET IN DYDX
STARK_PRIVATE_KEY_MAINNET = ""
DYDX_API_KEY_MAINNET = ""
DYDX_API_SECRET_MAINNET = ""
DYDX_API_PASSPHRASE_MAINNET = ""

#KEYS - DEVELOPMENT
#MUST BE ON TESTNET IN DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")


#Keys - export 
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET


# HOST - EXPORT
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

# HTTP PROVIDERS 
HTTP_PROVIDER_MAINNET = ""
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/ygS9S6SVy20zW2bIm7nW0OMMkGhwLWV6"

HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET
