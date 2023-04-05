from utilities.db_connection import db_cursor


def rates_calculation(date_from, date_to, origin, destination):
    cursor = db_cursor().cursor()
    print(date_from, date_to, origin, destination, "this is args")
    # """
    #     the meat of the application where we take the ports
    #     the date from and the date to
    #     then we calculate the days and their average price

    #     first we need to get the origin region find the slug in the region if not that then port code

    #     then destination region find the slug in there or port code
    # """

    # check port to port
    def port_to_port():
        # select the price table and get port codes between two time frames and average the price total        
        postgreSQL_select_Query = "SELECT AVG(price) FROM prices WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        res = cursor.execute(postgreSQL_select_Query)

        return res
    def port_to_region():
        postgreSQL_select_Query = "SELECT AVG(price) FROM prices WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        res = cursor.execute(postgreSQL_select_Query)

        return res
    def region_to_port():
        postgreSQL_select_Query = "SELECT AVG(price) FROM prices WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        res = cursor.execute(postgreSQL_select_Query)

        return res
    def region_to_region():
        postgreSQL_select_Query = "SELECT AVG(price) FROM prices WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        res = cursor.execute(postgreSQL_select_Query)

        return res

    ptp = port_to_port()
    if (ptp):
        return ptp
    elif 

    return []
