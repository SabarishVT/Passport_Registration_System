import PySimpleGUI as sg

def main():
    sg.theme('TanBlue')

    layout = [
        [sg.Text('Passport Registration System', size=(30, 1), font=("Helvetica", 20),justification='right')],
        [sg.Text('Applying For ', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.OptionMenu(('New', 'Renewal'), key='optionmenu1',size=(10,1),pad=(3,20)),
        sg.Text('Type', size=(10, 1), font=("Helvetica", 12), justification = 'right'),
        sg.OptionMenu(('Normal', 'Tatkal'), key='optionmenu2',size=(10,1)),
        sg.Text('Pages', size=(10, 1), font=("Helvetica", 12), justification = 'right'),
        sg.OptionMenu(('36', '60'), key='optionmenu3',size=(10,1),pad=(3,20))],
        [sg.Text('First Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input1',font=("Helvetica", 12)),
        sg.Text('Middle Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input2',font=("Helvetica", 12)),
        sg.Text('Last Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input3',font=("Helvetica", 12))],
        [sg.Text('Gender', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.Radio('Male', "RADIO1", key='rad1', default=True),
        sg.Radio('Female', "RADIO1", key='rad2'),
        sg.Radio('Other', "RADIO1", key='rad3')],
        [sg.Text('Date of Birth ', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.OptionMenu(('1', '2','3'), key='optionmenu4',size=(10,1)),
        sg.OptionMenu(('Jan', 'Feb'), key='optionmenu5',size=(10,1)),
        sg.OptionMenu(('1980', '1981'), key='optionmenu6',size=(10,1))],
        [sg.Text('Marital Status', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.OptionMenu(('Single', 'Married','Divorced','Widow/Widower'), key='optionmenu7',size=(10,1))],
        [sg.Text('Country', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input4',font=("Helvetica", 12)),
        sg.Text('State', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input5',font=("Helvetica", 12)),
        sg.Text('District', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input6',font=("Helvetica", 12))],
        [sg.Text('Aadhar No', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input7',font=("Helvetica", 12))],
        [sg.Text('PAN No', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input8',font=("Helvetica", 12))],
        [sg.Text('Voter ID', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input9',font=("Helvetica", 12))],
        [sg.Text('Educational Qualitificaiton', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.OptionMenu(('7th pass or less', '8 to 10th','10th Above','Graduate Above'), key='optionmenu8',size=(10,1))],
        [sg.Text('Employment Type', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.OptionMenu(('Public Sector', 'Private Sector'), key='optionmenu9',size=(10,1))],
        [sg.Text('Visible Distinguishing Mark', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input10',font=("Helvetica", 12))],
        [sg.Text('Permanent Address', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.Multiline(enter_submits=True, key='query1', do_not_clear=False),
        sg.Text('Middle Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.Multiline(enter_submits=True, key='query2', do_not_clear=False)],
        [sg.Text('Pincode', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input11',font=("Helvetica", 12)),
        sg.Text('Pincode', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input12',font=("Helvetica", 12))],
        [sg.Text('Police Station', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input13',font=("Helvetica", 12)),
        sg.Text('Police Station', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input14',font=("Helvetica", 12))],
        [sg.Text('Fathers First Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input15',font=("Helvetica", 12)),
        sg.Text('Fathers Middle Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input16',font=("Helvetica", 12)),
        sg.Text('Fathers Last Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input17',font=("Helvetica", 12))],
        [sg.Text('Mothers First Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input18',font=("Helvetica", 12)),
        sg.Text('Mothers Middle Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input19',font=("Helvetica", 12)),
        sg.Text('Mothers Last Name', size=(10, 1), font=("Helvetica", 12), justification = 'left'),
        sg.InputText(key='input20',font=("Helvetica", 12))],
        [sg.Button("Submit"),
        sg.Button("Reset"),
        sg.Button("Cancel")]
    ]
    window = sg.Window('Passport Registration Form', layout, default_element_size=(40,1), grab_anywhere=False)

    while True:
        event, values = window.read()
        
        if event == 'SEND':
            print(values['optionmenu1'])
        
    window.close()

if __name__ == "__main__":
    main()