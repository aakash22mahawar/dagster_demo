from .logging_config import setup_logger
from .connection import get_snowflake_connection

# Initialize the logger
logger = setup_logger()

def load_to_snowflake(weather_data):
    conn = get_snowflake_connection()
    cur = conn.cursor()

    insert_query = """
    INSERT INTO sandbox.des_marketing.weather_data (
        city, country, timezone, observed_time, temperature,
        sunrise, sunset, moonrise, moonset, moonphase
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cur.execute(insert_query, (
        weather_data['city'],
        weather_data['country'],
        weather_data['timezone'],
        weather_data['observed_time'],
        weather_data['temperature'],
        weather_data['sunrise'],
        weather_data['sunset'],
        weather_data['moonrise'],
        weather_data['moonset'],
        weather_data['moonphase']
    ))

    cur.close()
    conn.close()


# # Example usage
# if __name__ == "__main__":
#    load_to_snowflake()
