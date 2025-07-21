# field half in circle and rest rectangle
radius=20
length=50
breadth=40
fencing_half_circle=3.14*radius 
fencing_rectangle_wall =length+breadth+length

wire_required=(fencing_half_circle+fencing_rectangle_wall)*5

Total_cost=wire_required*35

print("total cost for fencing wires for 5 times : ",Total_cost)
