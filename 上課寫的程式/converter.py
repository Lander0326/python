import PySimpleGUI as sg

layout = [
	[
		sg.Input(key = '-INPUT-'),
		sg.Spin(['km to mile','kg to pound','sec to min'], key = '-UNITS-'), 
		sg.Button('Convert', key = '-CONVERT-')
	],
	[sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window('Converter',layout)

while True:
	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-CONVERT-':
		input_value = values['-INPUT-']
		if input_value.isnumeric():
			if  values['-UNITS-'] == 'km to mile':
					output = round(float(input_value) * 0.6214,2)
					output_string = f'{input_value} km are {output} miles.'
			elif 'kg to pound':
					output = round(float(input_value) * 2.20462,2)
					output_string = f'{input_value} kg are {output} pounds.'
			elif 'sec to min':
					output = round(float(input_value) / 60,2)
					output_string = f'{input_value} seconds are {output} minutes.'

			window['-OUTPUT-'].update(output_string,text_color = "#ffffff")
		else:
			window['-OUTPUT-'].update('Please enter a number',text_color = "red")

window.close()