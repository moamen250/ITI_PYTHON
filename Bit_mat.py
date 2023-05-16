def Set_bit(val,BitNo):
		val=int(val)
		BitNo=int(BitNo)
		result=val|(1<<BitNo)
		return result
# Function to Get Bit
def Get_bit(val,BitNo):
		val=int(val)
		BitNo=int(BitNo)
		result=(val>>BitNo)&1
		return result
# Function to TOggle Bit
def Toggle_bit(val,BitNo):
		val=int(val)
		BitNo=int(BitNo)
		result=val^(1<<BitNo)
		return result
# Function to Clear Bit
def Clear_bit(val,BitNo):
		val=int(val)
		BitNo=int(BitNo)
		result=val&(1<<BitNo)
		return result

x=Set_bit=(3,1)
print(x)
y=Set_bit=(5,1)
print(y)
z=Set_bit=(7,3)
print(z)
E=Set_bit=(7,2)
print(E)
w=Get_bit
print(w)