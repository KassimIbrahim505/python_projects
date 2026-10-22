import re

medical_records = [
    {'patient_id': 'P001',
     'age': 38,
        'gender': 'Female',
     'diagnosis': 'Hypertension',
     'medications': ['Lisinopril'],
     'last_visit_id':'V2301'
    },
    {'patient_id': 'P002',
    'age': 52,
    'gender': 'Male',
    'diagnosis': 'Type 2 Diabetes',
    'medications': ['Metformin', 'Glipizide'],
    'last_visit_id': 'V2302'
    },
    {'patient_id': 'P003',
    'age': 29,
    'gender': 'Female',
    'diagnosis': 'Asthma',
    'medications': ['Albuterol'],
    'last_visit_id': 'V2303'
    },
    {'patient_id': 'P004',
    'age': 44,
    'gender': 'Male',
    'diagnosis': 'Migraine',
    'medications': ['Sumatriptan'],
    'last_visit_id': 'V2304'
    },
    {'patient_id': 'P005',
    'age': 61,
    'gender': 'Female',
    'diagnosis': 'High Cholesterol',
    'medications': ['Atorvastatin', 'Ezetimibe'],
    'last_visit_id': 'V2305'
    }
]

# Comment notes:
# all() returns True only when every item in the iterable is truthy.
# Here, it checks whether every item in the medications list is a string.
# If any item is not a string, all() returns False.
#
# Falsy-value checks:
# - `if not value` is True for any falsy value: False, None, 0, '', [], or {}.
# - `if value == False` checks equality; for example, 0 == False is True.
# - `if value is False` checks identity; it is True only for Boolean False.
#
# re.fullmatch() returns a match object when successful and None when unsuccessful.
# Therefore, `not value` identifies failed validation constraints.
#
# `p\d+` means the ID starts with `p` followed by one or more digits.
# `re.IGNORECASE` allows uppercase or lowercase letters.


def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id
                         ):
    constraints = {
        patient_id: isinstance(patient_id, str) and re.fullmatch('p\d+full', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ['male', 'female'],
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list) and all([isinstance(item, str) for item in medications]), 
        'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
                }

    return [key for key, value in constraints.items() if not value]

def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list of tuple')
        return False

    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at index {index}')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                 f'Invalid format: {dictionary} at posittion {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            print(f'Invalid format: "{key}: {dictionary[key]}" at position {index}')
            is_invalid = True

    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)
#print(find_invalid_records(**medical_records[0]))
     