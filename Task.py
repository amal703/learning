import requests

def fetch_employees_with_high_salary(endpoint_url, min_salary):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"} 
    try:
        response = requests.get(endpoint_url,headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "success":
                high_salary_employees = [employee["employee_name"] for employee in data["data"] if employee["employee_salary"] > min_salary]
                return high_salary_employees
            else:
                print("Error: API returned unsuccessful status.")
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return []

if __name__ == "__main__":
    endpoint_url = "https://dummy.restapiexample.com/api/v1/employees"
    high_salary_employees = fetch_employees_with_high_salary(endpoint_url, min_salary=200000)
    
    if high_salary_employees:
        print("Employees with salary greater than 200,000:")
        for employee_name in high_salary_employees:
            print(employee_name)
    else:
        print("No employees found with salary greater than 200,000.")
