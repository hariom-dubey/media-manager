def result_row_to_dict(data):
    return data._asdict()

def result_list_to_dict(data):
    return [row._asdict() for row in data]