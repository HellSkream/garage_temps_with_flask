import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def get_last_numb_days(database, numb_days):
    conn = create_connection(database)

    sql_query = f"""SELECT log_time, cpu_temp, garage_temp, perth_temp FROM garage_temps
                WHERE log_time > date('now', '-{numb_days} days')
                """

    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    return df

def get_max_log_datetime(database):
    conn = create_connection(database)
    sql_query = "SELECT MAX(log_time) FROM garage_temps"
    query = conn.execute(sql_query)
    maxdate = query.fetchone()[0]
    conn.close()
    return maxdate

def update_records(database, file):
    conn = create_connection(database)
    col_names = {'Log Time':'log_time',
             'CPU Temp':'cpu_temp',
             'Garage Temp':'garage_temp' ,
             'Perth Temp':'perth_temp',
             'Weather Desc':'weath_desc',
             'Weath Time':'weath_time'}
    last_record = get_max_log_datetime(database)
    data = pd.read_csv(file)
    if last_record:
        data = data[data['Log Time'] > last_record]
    data = data.rename(columns=col_names)
    data.to_sql('garage_temps', conn, if_exists='append', index=False)
    conn.close()

def update_weath_codes(database, weath_dict):
    conn = create_connection(database)
    # cur = conn.cursor
    query = "INSERT INTO weath_desc (weath_desc, weath_code) VALUES (?,?)"
    for desc, code in weath_dict.items():
        conn.execute(query, [desc, code])
    conn.commit()
    conn.close()

if __name__=='__main__':
    database = 'garage_temps.sqlite'
    infile = r'Garage_Project_Data_Export_20240618.csv'
    numb_days = 6
    
    Weath_codes = {'None':'None',
               'light intensity shower rain': 'Rain',
               'light rain': 'Rain',
               'overcast clouds':'Cloudy',
               'clear sky':'Clear',
               'few clouds':'Clear',
               'scattered clouds':'Clear',
               'broken clouds':'Clear',
               'drizzle': 'Rain',
               'mist':'Cloudy',
               'fog':'Cloudy',
               'light intensity drizzle':'Cloudy',
               'shower rain':'Rain',
               'heavy intensity shower rain':'Rain',
               'moderate rain':'Rain',
               'heavy intensity drizzle':'Rain',
               'haze':'Clear',
               'smoke':'Clear',
               'thunderstorm with light rain':'Rain',
               'thunderstorm with rain':'Rain',
               'heavy intensity rain':'Rain',
               'thunderstorm with heavy rain':'Rain',
               'dust':'Clear',
               'thunderstorm':'Rain'
              }
    # x =get_last_numb_days(database, numb_days)
    # print(x)
    # update_records(database, infile)
    print(get_max_log_datetime(database))
    update_weath_codes(database, Weath_codes)
