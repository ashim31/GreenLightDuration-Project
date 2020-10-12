from fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_variable_input import FuzzyInputVariable
# from fuzzy_system.fuzzy_variable import FuzzyVariable
from fuzzy_system import FuzzySystem

a_vehicle = FuzzyInputVariable('ArrivingVehicle', 0, 50, 100)
a_vehicle.add_triangular('Less', 0, 0, 10)
a_vehicle.add_triangular('Medium', 7, 16, 25)
a_vehicle.add_triangular('High', 20, 50, 50)

q_vehicle = FuzzyInputVariable('QueuingVehicle', 0, 50, 100)
q_vehicle.add_triangular('Less', 0, 0, 10)
q_vehicle.add_triangular('Medium', 7, 16, 25)
q_vehicle.add_triangular('High', 20, 50, 50)

gl_duration = FuzzyOutputVariable('GreenLightDuration', 0, 60, 100)
gl_duration.add_triangular('Short', 0, 0, 10)
gl_duration.add_triangular('Medium', 8, 19, 30)
gl_duration.add_triangular('Long', 25, 60, 60)

system = FuzzySystem()
system.add_input_variable(a_vehicle)
system.add_input_variable(q_vehicle)
system.add_output_variable(gl_duration)

system.add_rule(
    {'ArrivingVehicle': 'High', 'QueuingVehicle': 'Less'},
    {'GreenLightDuration': 'Short'})

system.add_rule(
    {'ArrivingVehicle': 'High', 'QueuingVehicle': 'Medium'},
    {'GreenLightDuration': 'Medium'})

system.add_rule(
    {'ArrivingVehicle': 'High',
     'QueuingVehicle': 'High'},
    {'GreenLightDuration': 'Long'})

system.add_rule(
    {'ArrivingVehicle': 'Medium', 'QueuingVehicle': 'Less'},
    {'GreenLightDuration': 'Short'})

system.add_rule(
    {'ArrivingVehicle': 'Medium', 'QueuingVehicle': 'Medium'},
    {'GreenLightDuration': 'Medium'})

system.add_rule(
    {'ArrivingVehicle': 'Medium', 'QueuingVehicle': 'High'},
    {'GreenLightDuration': 'Long'})

system.add_rule(
    {'ArrivingVehicle': 'Less', 'QueuingVehicle': 'Less'},
    {'GreenLightDuration': 'Short'})

system.add_rule(
    {'ArrivingVehicle': 'Less', 'QueuingVehicle': 'Medium'},
    {'GreenLightDuration': 'Medium'})

system.add_rule(
    {'ArrivingVehicle': 'Less', 'QueuingVehicle': 'High'},
    {'GreenLightDuration': 'Short'})

output = system.evaluate_output({
    'ArrivingVehicle': 35,
    'QueuingVehicle': 50
	})

print(output)
system.plot_system()
