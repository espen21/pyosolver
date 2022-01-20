from pyosolver import PYOSolver

print("hello")
pio_dir = "C:\\PioSOLVER\\"
pio_exe = "PioSOLVER2-basic"
load_tree=  r"C:\PioSOLVER\Saved_solves\3b\BTNvsBB\596ss.cfr"

def get_desc(node):
    if "OOP_DEC" in node["NODE_TYPE"]: return "OOP"
    else: return "IP"
solver = PYOSolver(pio_dir,pio_exe)
solver.load_tree(load_tree)
a =solver.show_node("r:0")
ev_combo = solver.calc_ev(get_desc(a),"r:0")
children = solver.show_children("r:0")
for child in children:
    d = child["nodeID"]
    print(d)
    for c in solver.calc_ev("OOP",d):
       
        print(c)
    print(get_desc(solver.show_node(d)))
solver._run("calc_ev OOP r:0")