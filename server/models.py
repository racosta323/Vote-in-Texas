import requests
from io import BytesIO
from fillpdf import fillpdfs
from prompts import person_attributes, attribute_keys
import ipdb


class PdfDoc:
    def __init__(self):
        self.pdf = None
        self.pdf_content = None
        self.url = "https://www.sos.state.tx.us/elections/forms/vr-with-receipt.pdf"
       
    def request(self):

        try:
            response = requests.get(self.url)
            response.raise_for_status()      
            pdf_doc = response.content
            self.pdf_content = BytesIO(pdf_doc)
            self.pdf = pdf_doc.decode('Latin-1')
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}") 
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}") 
        except Exception as e:
            print(f"An error occurred: {e}")  

    def get_fields(self):
        try:
            self.form_fields = list(fillpdfs.get_form_fields(self.pdf_content).keys())
        except Exception as e:
            raise SystemExit(e)

    def data_dict(self, person, data=None): 
        self.get_fields()
        
        if data is None:
            data = {}
        
        if not isinstance(person, Person):
            raise ValueError("The 'person' argument must be an instance of the Person class.")
        
        for key, field in zip(attribute_keys, self.form_fields[0:]):
            # ipdb.set_trace()
            if key in person._attributes and person._attributes[key] is not None:
                data[field] = person._attributes[key]
                if key == 'phone':
                    data['Telephone Number Optional'] = person._attributes[key][0:3]
                    data['Telephone Number Optional 2'] = person._attributes[key][3:6]
                    data['Telephone Number Optional 3'] = person._attributes[key][6:10]
                    
                if key in ['citizenship', 'voting_age', 'election_worker']:
                    if person._attributes[key].lower() in ['y', 'yes']:
                        data[field] = 'Yes'
                    if person._attributes[key].lower() in ['n', 'no']:
                        data[field] = 'No'    
                
                if key == 'gender':
                    if person._attributes[key].lower() in ['m', 'male']:
                        data[field] = 'Yes'
                    if person._attributes[key].lower() in ['f', 'female']:
                        data[field] = 'No'
                
                if key == 'no_id':
                     if person._attributes[key].lower() in ['n', 'no']:
                        data[field] = 'Yes'

                if key == 'why':
                    if int(person._attributes[key]) == 1:
                        data[field] = 'New Application'
                    if int(person._attributes[key]) == 2:
                        data[field] = 'Change of Address, Name, or Other Information'
                    if int(person._attributes[key]) == 3:
                        data[field] = 'Request for a Replacement Card'

        return data
        
    def write_pdf(self, person, save_to_file=False):
        self.request()
        input_pdf_path = self.pdf
        output_pdf = BytesIO()
        data_dict = self.data_dict(person)

        output_pdf_path = f"{person._attributes['first_name']}_{person._attributes['last_name']}_TX_voter_reg.pdf"
        
        fillpdfs.write_fillable_pdf(input_pdf_path=input_pdf_path, output_pdf_path=output_pdf, data_dict=data_dict)
        
        if save_to_file:
            with open(output_pdf_path, 'wb') as f:
                f.write(output_pdf.getvalue())
        
        output_pdf.seek(0)
        return output_pdf
        
class Person:
    def __init__(self,**kwargs):        
        self._attributes = person_attributes

        for key, value in kwargs.items():
            if key in self._attributes:
                self._attributes[key] = value
            else:
                raise AttributeError(f'Invalid attribute: {key}')
            
    def __repr__(self):
        output = f"""
        First name: {self._attributes['first_name']}
        Last name: {self._attributes['last_name']}
        """
        return output