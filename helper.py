def compare_dates(date1, date2):
    date1_parts = date1.split("/")
    date2_parts = date2.split("/")
    return date1_parts >= date2_parts
