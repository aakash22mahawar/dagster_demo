import snowflake.connector
import configparser
from .logging_config import setup_logger
import os

BASE_DIR = os.path.dirname(__file__)
config_file_path = os.path.join(BASE_DIR, "config.ini")

# Initialize the logger
logger = setup_logger()



# Function to establish and return the Snowflake connection using private key authentication
def get_snowflake_connection():
    # Load the configuration from the config.ini file
    config = configparser.ConfigParser()
    config.read(config_file_path)

    try:
        # Read Snowflake credentials from the config file
        SNOWFLAKE_USER = config['Snowflake']['user']
        SNOWFLAKE_PASSWORD = config['Snowflake']['password']
        SNOWFLAKE_ACCOUNT = config['Snowflake']['account']
        SNOWFLAKE_WAREHOUSE = config['Snowflake']['warehouse']
        SNOWFLAKE_DATABASE = config['Snowflake']['database']
        SNOWFLAKE_SCHEMA = config['Snowflake']['schema']
        SNOWFLAKE_AUTOCOMMIT = config.getboolean('Snowflake', 'autocommit')
        ROLE = config['Snowflake']['role']


        # Establish and return the Snowflake connection
        connection = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA,
            autocommit=SNOWFLAKE_AUTOCOMMIT,
            role=ROLE
        )

        logger.info("Snowflake connection established successfully!")
        return connection

    except Exception as e:
        logger.error(f"Snowflake connection failed: {e}")
        raise


# # Test the connection
# if __name__ == "__main__":
#     conn = get_snowflake_connection()
#     if conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT CURRENT_VERSION()")
#         print("Snowflake Version:", cursor.fetchone()[0])
