from app.config import feature_mapping


def format_data(data):
    formated_data = [0]*len(feature_mapping.keys())
    for key, value in feature_mapping.items():
        sub_key = list(value.keys())[0]
        
        # numerical_features
        if value[sub_key] is None:
            formated_data[key] = data[sub_key]

        # categorical_features
        else:
            if data[sub_key] == value[sub_key]:
                formated_data[key] = 1
    return [formated_data]
