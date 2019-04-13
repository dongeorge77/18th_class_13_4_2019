from A import A
class B(A):
    def __init__(self):
        A.__init__(self)
        print("in B")
b = B()
