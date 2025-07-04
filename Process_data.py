import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"Saved updated data to {file_path}")

def update_college_data(colleges, new_data):
    for new_college in new_data:
        for college in colleges:
            if college['tnea_code'] == new_college['tnea_code']:
                college.update(new_college)
                print(f"Updated college: {college['institute_name']}")
                break
        else:
            colleges.append(new_college)
            print(f"Added college: {new_college['institute_name']}")
    return colleges

def main():
    file_path = 'colleges.json'
    colleges = load_json(file_path)
    if not colleges:
        return

    # Example: Update or add colleges (replace with actual data)
    new_data = [
        {
            "application_number": "N/A",
            "tnea_code": "9999",
            "institute_name": "NEW ENGINEERING COLLEGE",
            "address": "Sample Address, Chennai - 600001",
            "district": "Chennai",
            "state": "Tamil Nadu",
            "website": "www.newcollege.edu.in",
            "branches": [
                {"code": "CS", "name": "Computer Science and Engineering"},
                {"code": "EC", "name": "Electronics and Communication Engineering"}
            ],
            "is_7.5_quota_eligible": True,
            "cutoff_2025": {
                "CS": {"OC": 190.0, "BC": 185.0, "7.5_quota": 180.0},
                "EC": {"OC": 185.0, "BC": 180.0, "7.5_quota": 175.0}
            }
        }
    ]

    updated_colleges = update_college_data(colleges, new_data)
    save_json(updated_colleges, file_path)

if __name__ == "__main__":
    main()
