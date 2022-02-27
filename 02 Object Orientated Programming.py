class student():
    def __init__(self, name='no name', dob='00/00/0000', form='0AA', gender='no gender', postcode='AA0 0AA'):

        self.name, self.dob, self.form, self.gender, self.postcode = name, dob, form, gender, postcode

    def info(self):
        print()
        print('Name: ' + self.name)
        print('Date of birth: ' + self.dob)
        print('Form: ' + self.form)
        print('Gender: ' + self.gender)
        print('Postcode: ' + self.postcode)

    def change(self):
        valid = False
        while valid == False:
            valid = True
            editing = input('What would you like to edit?')
            if editing == 'name':
                self.name = choose()
            elif:



    def choose():
        return choice = int(input('What value do you want to change this too'))


bob = student()

bob.name, bob.dob, bob.form, bob.gender, bob.postcode = 'Bob', '28/09/2021', '7E2', 'Male', 'IG6 2JB'

bob.info()
