from pyosolver import PYOSolver

print("hello")
pio_dir = "C:\\PioSOLVER\\"
pio_exe = "PioSOLVER2-basic"
load_tree=  r"C:\PioSOLVER\Saved_solves\3b\BTNvsBB\596ss.cfr"

solver = PYOSolver(pio_dir,pio_exe)
solver.load_tree(load_tree)
solver.show_node("r")