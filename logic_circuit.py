#  python & data structure
#  class and subclass

class logic_gate:
	def __init__(self, n):
		self.label = n
		self.output = None

	def get_label(self):
		return self.label

	def get_output(self):
		self.output = self.perform_gate_logic()
		return self.output

class binary_gate(logic_gate):
	def __init__(self, n):
		super().__init__(n)

		self.pin_a = None
		self.pin_b = None

	def get_pin_a(self):
		if self.pin_a == None:
			return int(input("Enter pin a input for gate " + self.get_label() + "-->"))
		else:
			return self.pin_a.get_from().get_output()

	def get_pin_b(self):
		if self.pin_b == None:
			return int(input("Enter pin b input for gate " + self.get_label() + "-->"))
		else:
			return self.pin_b.get_from().get_output()
		
	def set_next_pin(self, source):
		if self.pin_a == None:
			self.pin_a = source
		else:
			if self.pin_b == None:
				self.pin_b = source
			else:
				raise RuntimeError("Error: No empty pins")
		
class unary_gate(logic_gate):
	def __init__(self, n):
		super().__init__(n)
		self.pin = None

	def get_pin(self):
		if self.pin == None:
			return int(input("Enter pin input for gate " + self.get_label() + "-->"))
		else:
			return self.pin.get_from().get_output()

	def set_next_pin(self, source):
		if self.pin == None:
			self.pin = source
		else:
			raise RuntimeError("Error: No empty pins")
		
class and_gate(binary_gate):
	def __init__(self, n):
		super().__init__(n)
		
	def perform_gate_logic(self):
		a = self.get_pin_a()
		b = self.get_pin_b()
		if a == 1 and b == 1:
			return 1
		else:
			return 0

class or_gate(binary_gate):
	def __init__(self, n):
		super().__init__(n)
	def perform_gate_logic(self):
		
		a = self.get_pin_a()
		b = self.get_pin_b()
		if a == 1 or b == 1:
			return 1
		else:
			return 0

class not_gate(unary_gate):
	def __init__(self, n):
		super().__init__(n)
		
	def perform_gate_logic(self):
		a = self.get_pin()
		if a == 1:
			return 0
		elif a == 0:
			return 1


class connector:
	"""docstring for ClassName"""
	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate
		tgate.set_next_pin(self)

	def get_from(self):
		return self.fromgate

	def get_to(self):
		return self.togate

g1 = and_gate("G1")
g2 = and_gate("G2")
g3 = or_gate("G3")
g4= not_gate("G4")
c1 = connector(g1, g3)
c2 = connector(g2, g3)
c3 = connector(g3, g4)
x = g4.get_output()
print(x)		