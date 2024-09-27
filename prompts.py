prompts = {
        "What is your first name? ": "first_name",
        "What is your last name? ": "last_name",
        "What is your middle name, if any? ": "middle_name",
        "What is your former name, if any? (e.g. a maiden name) ": "former_name",
        "What is your street address IN TEXAS, including any apartment numbers? If none, describe where you live. ": "street_address",
        "What city (in TX)? ": "city",
        "What county (in TX)? ": "county",
        "What is your zip code?": 'zip_code',
        "Mailing (street) address different than the one described (optional)? ": "street_address_2",
        'Secondary address city (optional)? ': "city_2",
        'Secondary address state (optional)? ': "state_2",
        'Secondary address zip code (optional)? ': "zip_code_2",
        'What is the city AND county of your former residence IN TEXAS? ': "former_res",
        'What month were you born? ': "birth_month",
        'What day were you born? ': "birth_day",
        'What year were you born? ': "birth_year",
        'What is your phone number (optional)? ': "phone",
        'Have you been issued a TX driver\'s license or social security number (SSN)?': 'no_id',
        'What is your TX driver\'s license number OR TX Personal ID number? ': "license",
        'What are the LAST 4 digits of your social security number (provide if no TX driver\'s license or Personal Identification cannot be given)? ': "ssn",
        'Are you a United States Citizen (Y or N)? ': "citizenship",
        'Will you be 18 years of age on or before election day (Y or N)? ': "voting_age",
        'Are you interested in becoming an election worker (Y or N)? ': "election_worker",
        "Do you identify as male or female (optional)? ": "gender"
        "New application?: new_application"
}

fields = ['These questions must be completed before proceeding', 'Last Name Include Suffix if any Jr Sr III 2', 'First Name', 'Middle NameIf any', 'Former Name if any', 'Residence Address Street Address and Apartment Number If none describe where you live Do not include PO Box Rural Rt or Business Address 3', 'City', 'County', 'Zip Code', 'Mailing Address Street Address and Apartment Number If mail cannot be delivered to your residence address 4', 'City_2', 'State', 'Zip Code_2', 'City and County of Former Residence in Texas', 'Date of Birth: \\(month\\)', 'Date of Birth: \\(day\\)', 'Date of Birth: \\(year\\)', 'Telephone Number Optional', 'Telephone Number Optional 2', 'Telephone Number Optional 3', "Texas Driver's License Number or Texas Personal Identification Number", 'give last 4 digits of your Social Security Number', 'I have not been issued ID', 'Date:', 'Deputy Number', 'Date_2', 'Name of ApplicantApplicants Agent if applicable', 'Receipt No', 'Name of Volunteer Deputy Registrar', 'Deputy No', 'Date_3', 'Print', 'Reset', 'Are you a United States Citizen?', 'Will you be 18 years of age on or before election day?', 'Are you interested in serving as an election worker?', 'Gender (Optional)']

person_attributes = {
       "first_name":None, 
        "last_name":None,
        "middle_name":None,
        "former_name":None,
        "street_address":None,
        "city":None,
        "county":None,
        "zip_code":None,
        "street_address_2":None,
        "city_2":None,
        "state":None,
        "zip_code_2":None,
        "former_res":None,
        "birth_month":None,
        "birth_day":None,
        "birth_year":None,
        "phone":None,
        'phone_2':None,
        'phone_3':None,
        "license":None,
        "ssn":None,
        "no_id":None,
        "date":None,
        "deputy":None,
        "secondary_date":None,
        "applicant_agent":None,
        "receipt":None,
        "volunteer":None,
        "deputy_no":None,
        "date_3":None,
        "print":None,
        "reset":None,
        'citizenship':None,
        "voting_age":None,
        "election_worker":None,
        "gender":None
        }