from utilities.db_connection import db_cursor


def rates_calculation(date_from, date_to, origin, destination):
    cursor = db_cursor().cursor()
    print(date_from, date_to, origin, destination, "this is args")
    """
        the meat of the application where we take the ports
        the date from and the date to
        then we calculate the days and their average price

        first we need to get the origin region find the slug in the region if not that then port code

        then destination region find the slug in there or port code
    """

    # check port to port
    def port_to_port():
        # select the price table and get port codes between two time frames and average the price total
        # the reason for  >=  and < is because BETWEEN has a tendancy to be inclusive in certain situations
        postgreSQL_select_Query = "SELECT AVG(price) FROM prices WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        res = cursor.execute(postgreSQL_select_Query)

        return res

    def port_to_region():
        """
        cant see my results but i know this can use work joining the different tables from ports of the region side (destination)
        """
        postgreSQL_select_Query = "SELECT AVG(price) FROM prices JOIN ports on prices.orig_code=ports.code WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        res = cursor.execute(postgreSQL_select_Query)

        return res

    def region_to_port():
        postgreSQL_select_Query = "SELECT AVG(price) FROM prices JOIN ports on prices.orig_code=ports.code WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        res = cursor.execute(postgreSQL_select_Query)

        return res

    def region_to_region():
        """
        we have to backtrack from the region all the way back to the  port code, 
        from there we join the two searches and we do the same thing
        of averaging out the prices of the days 
        """

        # postgreSQL_select_Query = "SELECT AVG(price) FROM prices WHERE orig_code='{origin}' AND dest_code='{destination}' AND day BETWEEN day >= '{date_from}' AND day < '{date_to}';"
        # res = cursor.execute(postgreSQL_select_Query)

    # not sure if prices has to be less than three or if results have to be less than 3 here
    # def check_if_less_than_three():

    # this would have to be cleaner as well, there should be a way to grab the results and be less repetative with the if statements
    # as well as better naming and err checking.

    ptp = port_to_port()
    if (ptp):
        return ptp

    ptr = port_to_region()
    if (ptr):
        return ptr

    rtp = region_to_port()
    if (rtp):
        return rtp

    rtr = region_to_region()
    if (rtr):
        return rtr
    
    # this is not what i would have done, i would have set up a catch here in case and returned a code along with a specific err message
    # due to my lack of time i will be placing the string err
    return "500, error querying for rates"
