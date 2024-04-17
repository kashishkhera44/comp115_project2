from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline



# Create two D6 and a Die 10 dice.
die_1 = Die()
die_2 = Die(10)


# Make some rolls, and store results in list
results = []
for roll_num in range(50_000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# Analyze the results.
frequencies =[]
max_result=die_1.num_sides +die_2.num_sides
for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# Visulaize the results.
x_values=list(range(1,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of Result'}
my_layout =Layout(title="Results of rolling a D6 and D10 50000 times", xaxis=x_axis_config)
offline.plot({'data':data,"layout":my_layout},filename="D6_d10.html")

print(frequencies)
