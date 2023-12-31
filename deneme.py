class Node:
    def __init__(self,ps):
        self.props=ps
    def isa(self,a,exclude=None):
        if isinstance(a,Node):
            if a.isa(self):
                return True
        for p in self.props:
            if a==exclude:
                continue
            if type(p)==str:
                if p==a:
                    return True
            elif isinstance(p,A) or isinstance(p,O):
                if a==p.name and p.isa(self):
                    return True
        return False

class A(Node):
    def __init__(self,name,props):
        self.name=name
        super().__init__(props)
    def isa(self,parent):
        for p in self.props:
            
            if not parent.isa(p,exclude=self):
                return False
        return True
class O(Node):
    def __init__(self,name,props):
        self.name=name
        super().__init__(props)
    def isa(self,parent):
        for p in self.props:
            if parent.isa(p,exclude=self):
                return True
        return False
elma=Node(["yesil","bitki","meyve","sert",A("yenir",["sert","yesil"])])
elma2=Node(["mavi","bitki","meyve","sert",A("yenir",["sert",O(None,["yesil","kirmizi"])])])
print(elma.isa("yenir"))
print(elma2.isa("yenir"))
