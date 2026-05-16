import tkinter as tk
from tkinter import ttk, messagebox
import math
from collections import Counter

class MathLifeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MathLife - Ultimate Mathematics Suite")
        self.root.geometry("900x700")
        self.root.configure(bg='#f5f5f5')
        
        # Modern styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#f5f5f5')
        style.configure('TLabel', background='#f5f5f5', font=('Segoe UI', 10))
        style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'), foreground='#2c3e50')
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#34495e')
        style.configure('TButton', font=('Segoe UI', 10), padding=6)
        style.configure('Action.TButton', font=('Segoe UI', 10, 'bold'), padding=8, background='#3498db', foreground='white')
        style.map('Action.TButton', background=[('active', '#2980b9')])
        style.configure('TEntry', padding=4, font=('Segoe UI', 10))
        style.configure('TNotebook', background='#f5f5f5')
        style.configure('TNotebook.Tab', padding=[12, 6], font=('Segoe UI', 9, 'bold'))
        
        # Main container
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="⚡ MathLife - Ultimate Mathematics Suite", style='Title.TLabel')
        title_label.pack(pady=(0, 15))
        
        # Create notebook for categories
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Category tabs
        self.categories = {
            "Algebra": ["Quadratic Eq", "Linear Eq", "Matrix Ops"],
            "Calculus": ["Derivative", "Integration"],
            "Statistics": ["Statistics", "Probability"],
            "Geometry": ["Coordinate", "Polygon", "Circle", "Sphere", "Cylinder", "Cone"],
            "Number Theory": ["GCD/LCM", "Prime Check", "Fibonacci", "Base Convert"],
            "Functions": ["Trigonometry", "Logarithm", "Exponential"],
            "Series": ["Arithmetic", "Geometric"],
            "Other": ["Vector", "Complex", "Percentage"]
        }
        
        self.frames = {}
        self.create_all_tabs()
        
    def create_all_tabs(self):
        for category, calculators in self.categories.items():
            tab_frame = ttk.Frame(self.notebook, padding=15)
            self.notebook.add(tab_frame, text=category)
            self.frames[category] = tab_frame
            
            if category == "Algebra":
                self.create_algebra_tab(tab_frame)
            elif category == "Calculus":
                self.create_calculus_tab(tab_frame)
            elif category == "Statistics":
                self.create_statistics_tab(tab_frame)
            elif category == "Geometry":
                self.create_geometry_tab(tab_frame)
            elif category == "Number Theory":
                self.create_number_theory_tab(tab_frame)
            elif category == "Functions":
                self.create_functions_tab(tab_frame)
            elif category == "Series":
                self.create_series_tab(tab_frame)
            elif category == "Other":
                self.create_other_tab(tab_frame)
    
    def create_input_field(self, parent, label_text, row, default=""):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, sticky='w', pady=4, padx=5)
        entry = ttk.Entry(parent, width=25)
        entry.grid(row=row, column=1, sticky='ew', pady=4, padx=5)
        if default:
            entry.insert(0, default)
        return entry
    
    def create_result_display(self, parent, row, height=6):
        result_text = tk.Text(parent, width=70, height=height, state='disabled', 
                             font=('Consolas', 10), bg='#ecf0f1', fg='#2c3e50')
        result_text.grid(row=row, column=0, columnspan=3, sticky='ew', pady=10, padx=5)
        return result_text
    
    def display_result(self, text_widget, result):
        text_widget.config(state='normal')
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", result)
        text_widget.config(state='disabled')
    
    def create_algebra_tab(self, parent):
        # Quadratic Equation Solver
        quad_frame = ttk.LabelFrame(parent, text="Quadratic Equation Solver (ax² + bx + c = 0)", padding=10)
        quad_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        self.quad_a = self.create_input_field(quad_frame, "a:", 0)
        self.quad_b = self.create_input_field(quad_frame, "b:", 1)
        self.quad_c = self.create_input_field(quad_frame, "c:", 2)
        self.quad_result = self.create_result_display(quad_frame, 4)
        
        ttk.Button(quad_frame, text="Solve", command=self.solve_quadratic, style='Action.TButton').grid(row=3, column=0, columnspan=2, pady=10)
        
        # Linear Equation Solver
        linear_frame = ttk.LabelFrame(parent, text="Linear Equation Solver (ax + b = 0)", padding=10)
        linear_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.linear_a = self.create_input_field(linear_frame, "a:", 0)
        self.linear_b = self.create_input_field(linear_frame, "b:", 1)
        self.linear_result = self.create_result_display(linear_frame, 3, height=3)
        
        ttk.Button(linear_frame, text="Solve", command=self.solve_linear, style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
        
        # Matrix Operations
        matrix_frame = ttk.LabelFrame(parent, text="Matrix Operations (2×2)", padding=10)
        matrix_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(matrix_frame, text="Matrix A:").grid(row=0, column=0, sticky='w', pady=4, padx=5)
        self.mat_a11 = ttk.Entry(matrix_frame, width=8)
        self.mat_a11.grid(row=0, column=1, padx=2)
        self.mat_a12 = ttk.Entry(matrix_frame, width=8)
        self.mat_a12.grid(row=0, column=2, padx=2)
        self.mat_a21 = ttk.Entry(matrix_frame, width=8)
        self.mat_a21.grid(row=1, column=1, padx=2)
        self.mat_a22 = ttk.Entry(matrix_frame, width=8)
        self.mat_a22.grid(row=1, column=2, padx=2)
        
        ttk.Label(matrix_frame, text="Matrix B:").grid(row=0, column=3, sticky='w', pady=4, padx=5)
        self.mat_b11 = ttk.Entry(matrix_frame, width=8)
        self.mat_b11.grid(row=0, column=4, padx=2)
        self.mat_b12 = ttk.Entry(matrix_frame, width=8)
        self.mat_b12.grid(row=0, column=5, padx=2)
        self.mat_b21 = ttk.Entry(matrix_frame, width=8)
        self.mat_b21.grid(row=1, column=4, padx=2)
        self.mat_b22 = ttk.Entry(matrix_frame, width=8)
        self.mat_b22.grid(row=1, column=5, padx=2)
        
        self.matrix_result = self.create_result_display(matrix_frame, 3, height=4)
        
        btn_frame = ttk.Frame(matrix_frame)
        btn_frame.grid(row=2, column=0, columnspan=6, pady=10)
        
        ops = [("A+B", "add"), ("A-B", "subtract"), ("A×B", "multiply"), 
               ("det(A)", "det_a"), ("det(B)", "det_b"), ("A^T", "transpose_a")]
        for i, (txt, op) in enumerate(ops):
            ttk.Button(btn_frame, text=txt, command=lambda o=op: self.matrix_op(o)).grid(row=0, column=i, padx=3)
    
    def create_calculus_tab(self, parent):
        # Derivative Calculator
        deriv_frame = ttk.LabelFrame(parent, text="Derivative Calculator", padding=10)
        deriv_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(deriv_frame, text="Function Type:").grid(row=0, column=0, sticky='w', pady=4, padx=5)
        self.deriv_func_type = tk.StringVar(value="polynomial")
        funcs = [("Polynomial ax^n", "polynomial"), ("sin(x)", "sin"), ("cos(x)", "cos"), 
                 ("tan(x)", "tan"), ("e^x", "exponential"), ("ln(x)", "logarithmic")]
        for i, (txt, val) in enumerate(funcs):
            ttk.Radiobutton(deriv_frame, text=txt, variable=self.deriv_func_type, value=val).grid(row=i, column=1, sticky='w')
        
        self.deriv_a = self.create_input_field(deriv_frame, "a (coeff):", 0, "1")
        self.deriv_n = self.create_input_field(deriv_frame, "n (power):", 1, "2")
        self.deriv_x = self.create_input_field(deriv_frame, "x value:", 2)
        self.deriv_result = self.create_result_display(deriv_frame, 6, height=4)
        
        ttk.Button(deriv_frame, text="Calculate Derivative", command=self.calc_derivative, 
                  style='Action.TButton').grid(row=5, column=0, columnspan=2, pady=10)
        
        # Integration Calculator
        integ_frame = ttk.LabelFrame(parent, text="Integration Calculator (Trapezoidal Rule)", padding=10)
        integ_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(integ_frame, text="Function Type:").grid(row=0, column=0, sticky='w', pady=4, padx=5)
        self.integ_func_type = tk.StringVar(value="polynomial")
        integ_funcs = [("Polynomial ax^n", "polynomial"), ("sin(x)", "trigonometric"), ("e^x", "exponential")]
        for i, (txt, val) in enumerate(integ_funcs):
            ttk.Radiobutton(integ_frame, text=txt, variable=self.integ_func_type, value=val).grid(row=i, column=1, sticky='w')
        
        self.integ_a = self.create_input_field(integ_frame, "a (coeff):", 0, "1")
        self.integ_n = self.create_input_field(integ_frame, "n (power):", 1, "2")
        self.integ_lower = self.create_input_field(integ_frame, "Lower limit:", 2)
        self.integ_upper = self.create_input_field(integ_frame, "Upper limit:", 3)
        self.integ_intervals = self.create_input_field(integ_frame, "Intervals:", 4, "100")
        self.integ_result = self.create_result_display(integ_frame, 6, height=4)
        
        ttk.Button(integ_frame, text="Calculate Integral", command=self.calc_integral, 
                  style='Action.TButton').grid(row=5, column=0, columnspan=2, pady=10)
    
    def create_statistics_tab(self, parent):
        # Statistics Calculator
        stat_frame = ttk.LabelFrame(parent, text="Statistics Calculator", padding=10)
        stat_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(stat_frame, text="Data (comma-separated):").grid(row=0, column=0, sticky='w', pady=4, padx=5)
        self.stat_data = tk.Text(stat_frame, width=35, height=3)
        self.stat_data.grid(row=1, column=0, columnspan=2, sticky='ew', pady=4, padx=5)
        self.stat_result = self.create_result_display(stat_frame, 3, height=10)
        
        ttk.Button(stat_frame, text="Calculate Statistics", command=self.calc_statistics, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
        
        # Probability Calculator
        prob_frame = ttk.LabelFrame(parent, text="Probability Calculator", padding=10)
        prob_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.prob_type = tk.StringVar(value="permutation")
        prob_types = [("Permutation P(n,r)", "permutation"), ("Combination C(n,r)", "combination"), 
                      ("Factorial n!", "factorial"), ("Binomial Probability", "binomial")]
        for i, (txt, val) in enumerate(prob_types):
            ttk.Radiobutton(prob_frame, text=txt, variable=self.prob_type, value=val).grid(row=i, column=0, sticky='w')
        
        self.prob_n = self.create_input_field(prob_frame, "n:", 0)
        self.prob_r = self.create_input_field(prob_frame, "r:", 1)
        self.prob_p = self.create_input_field(prob_frame, "p (probability):", 2, "0.5")
        self.prob_k = self.create_input_field(prob_frame, "k (successes):", 3)
        self.prob_result = self.create_result_display(prob_frame, 6, height=4)
        
        ttk.Button(prob_frame, text="Calculate", command=self.calc_probability, 
                  style='Action.TButton').grid(row=5, column=0, columnspan=2, pady=10)
    
    def create_geometry_tab(self, parent):
        # Coordinate Geometry
        coord_frame = ttk.LabelFrame(parent, text="Coordinate Geometry", padding=10)
        coord_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(coord_frame, text="Point 1 (x₁, y₁):").grid(row=0, column=0, sticky='w', pady=4, padx=5)
        self.coord_x1 = ttk.Entry(coord_frame, width=10)
        self.coord_x1.grid(row=0, column=1, padx=2)
        self.coord_y1 = ttk.Entry(coord_frame, width=10)
        self.coord_y1.grid(row=0, column=2, padx=2)
        
        ttk.Label(coord_frame, text="Point 2 (x₂, y₂):").grid(row=1, column=0, sticky='w', pady=4, padx=5)
        self.coord_x2 = ttk.Entry(coord_frame, width=10)
        self.coord_x2.grid(row=1, column=1, padx=2)
        self.coord_y2 = ttk.Entry(coord_frame, width=10)
        self.coord_y2.grid(row=1, column=2, padx=2)
        self.coord_result = self.create_result_display(coord_frame, 3, height=3)
        
        ttk.Button(coord_frame, text="Calculate", command=self.calc_coordinate, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=3, pady=10)
        
        # Polygon Area
        polygon_frame = ttk.LabelFrame(parent, text="Regular Polygon Area", padding=10)
        polygon_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.poly_n = self.create_input_field(polygon_frame, "Number of sides:", 0)
        self.poly_side = self.create_input_field(polygon_frame, "Side length:", 1)
        self.poly_result = self.create_result_display(polygon_frame, 3, height=3)
        
        ttk.Button(polygon_frame, text="Calculate", command=self.calc_polygon, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
        
        # Circle Calculator
        circle_frame = ttk.LabelFrame(parent, text="Circle Calculator", padding=10)
        circle_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        self.circle_r = self.create_input_field(circle_frame, "Radius:", 0)
        self.circle_result = self.create_result_display(circle_frame, 2, height=4)
        
        ttk.Button(circle_frame, text="Calculate", command=self.calc_circle, 
                  style='Action.TButton').grid(row=1, column=0, columnspan=2, pady=10)
        
        # Sphere Calculator
        sphere_frame = ttk.LabelFrame(parent, text="Sphere Calculator", padding=10)
        sphere_frame.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
        
        self.sphere_r = self.create_input_field(sphere_frame, "Radius:", 0)
        self.sphere_result = self.create_result_display(sphere_frame, 2, height=3)
        
        ttk.Button(sphere_frame, text="Calculate", command=self.calc_sphere, 
                  style='Action.TButton').grid(row=1, column=0, columnspan=2, pady=10)
        
        # Cylinder Calculator
        cyl_frame = ttk.LabelFrame(parent, text="Cylinder Calculator", padding=10)
        cyl_frame.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
        
        self.cyl_r = self.create_input_field(cyl_frame, "Radius:", 0)
        self.cyl_h = self.create_input_field(cyl_frame, "Height:", 1)
        self.cyl_result = self.create_result_display(cyl_frame, 3, height=3)
        
        ttk.Button(cyl_frame, text="Calculate", command=self.calc_cylinder, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
        
        # Cone Calculator
        cone_frame = ttk.LabelFrame(parent, text="Cone Calculator", padding=10)
        cone_frame.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
        
        self.cone_r = self.create_input_field(cone_frame, "Radius:", 0)
        self.cone_h = self.create_input_field(cone_frame, "Height:", 1)
        self.cone_result = self.create_result_display(cone_frame, 3, height=4)
        
        ttk.Button(cone_frame, text="Calculate", command=self.calc_cone, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
    
    def create_number_theory_tab(self, parent):
        # GCD/LCM Calculator
        gcd_frame = ttk.LabelFrame(parent, text="GCD & LCM Calculator", padding=10)
        gcd_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        self.gcd_num1 = self.create_input_field(gcd_frame, "Number 1:", 0)
        self.gcd_num2 = self.create_input_field(gcd_frame, "Number 2:", 1)
        self.gcd_result = self.create_result_display(gcd_frame, 3, height=3)
        
        ttk.Button(gcd_frame, text="Calculate", command=self.calc_gcd_lcm, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
        
        # Prime Number Checker
        prime_frame = ttk.LabelFrame(parent, text="Prime Number Checker", padding=10)
        prime_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.prime_op = tk.StringVar(value="check")
        ttk.Radiobutton(prime_frame, text="Check if prime", variable=self.prime_op, value="check").grid(row=0, column=0, sticky='w')
        ttk.Radiobutton(prime_frame, text="Find primes up to N", variable=self.prime_op, value="find").grid(row=1, column=0, sticky='w')
        self.prime_n = self.create_input_field(prime_frame, "Number:", 0)
        self.prime_result = self.create_result_display(prime_frame, 3, height=5)
        
        ttk.Button(prime_frame, text="Calculate", command=self.calc_prime, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
        
        # Fibonacci Calculator
        fib_frame = ttk.LabelFrame(parent, text="Fibonacci Sequence Generator", padding=10)
        fib_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        self.fib_n = self.create_input_field(fib_frame, "Number of terms:", 0)
        self.fib_result = self.create_result_display(fib_frame, 2, height=6)
        
        ttk.Button(fib_frame, text="Generate", command=self.calc_fibonacci, 
                  style='Action.TButton').grid(row=1, column=0, columnspan=2, pady=10)
        
        # Number Base Converter
        base_frame = ttk.LabelFrame(parent, text="Number Base Converter", padding=10)
        base_frame.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
        
        self.base_num = self.create_input_field(base_frame, "Decimal number:", 0)
        self.base_result = self.create_result_display(base_frame, 2, height=10)
        
        ttk.Button(base_frame, text="Convert to All Bases", command=self.convert_base, 
                  style='Action.TButton').grid(row=1, column=0, columnspan=2, pady=10)
    
    def create_functions_tab(self, parent):
        # Trigonometry Calculator
        trig_frame = ttk.LabelFrame(parent, text="Trigonometry Calculator", padding=10)
        trig_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        self.trig_angle = self.create_input_field(trig_frame, "Angle (degrees):", 0)
        self.trig_result = self.create_result_display(trig_frame, 2, height=5)
        
        ttk.Button(trig_frame, text="Calculate", command=self.calc_trigonometry, 
                  style='Action.TButton').grid(row=1, column=0, columnspan=2, pady=10)
        
        # Logarithm Calculator
        log_frame = ttk.LabelFrame(parent, text="Logarithm Calculator", padding=10)
        log_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.log_num = self.create_input_field(log_frame, "Number:", 0)
        self.log_base = self.create_input_field(log_frame, "Base:", 1, "10")
        self.log_result = self.create_result_display(log_frame, 3, height=3)
        
        ttk.Button(log_frame, text="Calculate", command=self.calc_logarithm, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
        
        # Exponential Calculator
        exp_frame = ttk.LabelFrame(parent, text="Exponential Calculator", padding=10)
        exp_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        self.exp_type = tk.StringVar(value="exponential")
        exp_types = [("Exponential a^x", "exponential"), ("Natural Log ln", "natural_log"), ("Log base 10", "log10")]
        for i, (txt, val) in enumerate(exp_types):
            ttk.Radiobutton(exp_frame, text=txt, variable=self.exp_type, value=val).grid(row=i, column=0, sticky='w')
        
        self.exp_base = self.create_input_field(exp_frame, "Base a:", 0)
        self.exp_x = self.create_input_field(exp_frame, "Exponent/Value x:", 1)
        self.exp_result = self.create_result_display(exp_frame, 3, height=3)
        
        ttk.Button(exp_frame, text="Calculate", command=self.calc_exponential, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=2, pady=10)
    
    def create_series_tab(self, parent):
        # Arithmetic Series
        arith_frame = ttk.LabelFrame(parent, text="Arithmetic Series", padding=10)
        arith_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        self.arith_a = self.create_input_field(arith_frame, "First term (a):", 0)
        self.arith_d = self.create_input_field(arith_frame, "Common difference (d):", 1)
        self.arith_n = self.create_input_field(arith_frame, "Number of terms (n):", 2)
        self.arith_result = self.create_result_display(arith_frame, 4, height=4)
        
        ttk.Button(arith_frame, text="Calculate", command=self.calc_arithmetic_series, 
                  style='Action.TButton').grid(row=3, column=0, columnspan=2, pady=10)
        
        # Geometric Series
        geo_frame = ttk.LabelFrame(parent, text="Geometric Series", padding=10)
        geo_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.geo_a = self.create_input_field(geo_frame, "First term (a):", 0)
        self.geo_r = self.create_input_field(geo_frame, "Common ratio (r):", 1)
        self.geo_n = self.create_input_field(geo_frame, "Number of terms (n):", 2)
        self.geo_result = self.create_result_display(geo_frame, 4, height=4)
        
        ttk.Button(geo_frame, text="Calculate", command=self.calc_geometric_series, 
                  style='Action.TButton').grid(row=3, column=0, columnspan=2, pady=10)
    
    def create_other_tab(self, parent):
        # Vector Calculator
        vec_frame = ttk.LabelFrame(parent, text="Vector Operations (2D)", padding=10)
        vec_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(vec_frame, text="Vector A (x, y):").grid(row=0, column=0, sticky='w', pady=4, padx=5)
        self.vec_ax = ttk.Entry(vec_frame, width=10)
        self.vec_ax.grid(row=0, column=1, padx=2)
        self.vec_ay = ttk.Entry(vec_frame, width=10)
        self.vec_ay.grid(row=0, column=2, padx=2)
        
        ttk.Label(vec_frame, text="Vector B (x, y):").grid(row=1, column=0, sticky='w', pady=4, padx=5)
        self.vec_bx = ttk.Entry(vec_frame, width=10)
        self.vec_bx.grid(row=1, column=1, padx=2)
        self.vec_by = ttk.Entry(vec_frame, width=10)
        self.vec_by.grid(row=1, column=2, padx=2)
        self.vec_result = self.create_result_display(vec_frame, 3, height=5)
        
        ttk.Button(vec_frame, text="Calculate", command=self.calc_vector, 
                  style='Action.TButton').grid(row=2, column=0, columnspan=3, pady=10)
        
        # Complex Number Calculator
        complex_frame = ttk.LabelFrame(parent, text="Complex Number Operations", padding=10)
        complex_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(complex_frame, text="Complex 1 (a + bi):").grid(row=0, column=0, sticky='w', pady=4, padx=5)
        self.complex_a1 = ttk.Entry(complex_frame, width=10)
        self.complex_a1.grid(row=0, column=1, padx=2)
        ttk.Label(complex_frame, text="+").grid(row=0, column=2)
        self.complex_b1 = ttk.Entry(complex_frame, width=10)
        self.complex_b1.grid(row=0, column=3, padx=2)
        ttk.Label(complex_frame, text="i").grid(row=0, column=4)
        
        ttk.Label(complex_frame, text="Complex 2 (c + di):").grid(row=1, column=0, sticky='w', pady=4, padx=5)
        self.complex_a2 = ttk.Entry(complex_frame, width=10)
        self.complex_a2.grid(row=1, column=1, padx=2)
        ttk.Label(complex_frame, text="+").grid(row=1, column=2)
        self.complex_b2 = ttk.Entry(complex_frame, width=10)
        self.complex_b2.grid(row=1, column=3, padx=2)
        ttk.Label(complex_frame, text="i").grid(row=1, column=4)
        
        self.complex_result = self.create_result_display(complex_frame, 3, height=4)
        
        btn_frame = ttk.Frame(complex_frame)
        btn_frame.grid(row=2, column=0, columnspan=5, pady=10)
        ttk.Button(btn_frame, text="Add", command=lambda: self.calc_complex('add')).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Multiply", command=lambda: self.calc_complex('multiply')).grid(row=0, column=1, padx=5)
        
        # Percentage Calculator
        percent_frame = ttk.LabelFrame(parent, text="Percentage Calculator", padding=10)
        percent_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
        
        self.pct_value = self.create_input_field(percent_frame, "Value:", 0)
        self.pct_total = self.create_input_field(percent_frame, "Total:", 1)
        self.pct_percent = self.create_input_field(percent_frame, "Percentage %:", 2)
        self.pct_result = self.create_result_display(percent_frame, 4, height=4)
        
        btn_frame2 = ttk.Frame(percent_frame)
        btn_frame2.grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(btn_frame2, text="Calculate %", command=self.calc_pct_percent).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame2, text="Calculate Value", command=self.calc_pct_value).grid(row=0, column=1, padx=5)
    
    # ==================== CALCULATOR FUNCTIONS ====================
    
    def solve_quadratic(self):
        try:
            a = float(self.quad_a.get())
            b = float(self.quad_b.get())
            c = float(self.quad_c.get())
            
            if a == 0:
                messagebox.showerror("Error", "Coefficient 'a' cannot be zero")
                return
            
            discriminant = b**2 - 4*a*c
            
            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)
                result = f"Two real roots:\nx₁ = {x1:.4f}\nx₂ = {x2:.4f}\n\nDiscriminant (Δ) = {discriminant:.4f} > 0"
            elif discriminant == 0:
                x = -b / (2*a)
                result = f"One real root:\nx = {x:.4f}\n\nDiscriminant (Δ) = {discriminant:.4f} = 0"
            else:
                real_part = -b / (2*a)
                imag_part = math.sqrt(abs(discriminant)) / (2*a)
                result = f"Complex roots:\nx₁ = {real_part:.4f} + {imag_part:.4f}i\nx₂ = {real_part:.4f} - {imag_part:.4f}i\n\nDiscriminant (Δ) = {discriminant:.4f} < 0"
            
            self.display_result(self.quad_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def solve_linear(self):
        try:
            a = float(self.linear_a.get())
            b = float(self.linear_b.get())
            
            if a == 0:
                result = "Infinite solutions" if b == 0 else "No solution"
            else:
                x = -b / a
                result = f"x = {x:.4f}"
            
            self.display_result(self.linear_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def matrix_op(self, operation):
        try:
            A = [[float(self.mat_a11.get()), float(self.mat_a12.get())],
                 [float(self.mat_a21.get()), float(self.mat_a22.get())]]
            B = [[float(self.mat_b11.get()), float(self.mat_b12.get())],
                 [float(self.mat_b21.get()), float(self.mat_b22.get())]]
            
            if operation == "add":
                result = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
                text = f"A + B =\n[[{result[0][0]:.2f}, {result[0][1]:.2f}]\n [{result[1][0]:.2f}, {result[1][1]:.2f}]]"
            elif operation == "subtract":
                result = [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]
                text = f"A - B =\n[[{result[0][0]:.2f}, {result[0][1]:.2f}]\n [{result[1][0]:.2f}, {result[1][1]:.2f}]]"
            elif operation == "multiply":
                result = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
                text = f"A × B =\n[[{result[0][0]:.2f}, {result[0][1]:.2f}]\n [{result[1][0]:.2f}, {result[1][1]:.2f}]]"
            elif operation == "det_a":
                det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
                text = f"Determinant of A = {det:.2f}"
            elif operation == "det_b":
                det = B[0][0] * B[1][1] - B[0][1] * B[1][0]
                text = f"Determinant of B = {det:.2f}"
            elif operation == "transpose_a":
                text = f"A^T =\n[[{A[0][0]:.2f}, {A[1][0]:.2f}]\n [{A[0][1]:.2f}, {A[1][1]:.2f}]]"
            
            self.display_result(self.matrix_result, text)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_derivative(self):
        try:
            x = float(self.deriv_x.get())
            func_type = self.deriv_func_type.get()
            h = 0.0001
            
            if func_type == "polynomial":
                a = float(self.deriv_a.get())
                n = float(self.deriv_n.get())
                f_x = a * (x ** n)
                analytical = a * n * (x ** (n - 1))
                result = f"f(x) = {f_x:.4f}\nf'(x) = {analytical:.4f} (Analytical: {a*n}x^{n-1})"
            elif func_type in ["sin", "cos", "tan"]:
                if func_type == "sin":
                    f_x = math.sin(x)
                    derivative = math.cos(x)
                    func_name, deriv_name = "sin(x)", "cos(x)"
                elif func_type == "cos":
                    f_x = math.cos(x)
                    derivative = -math.sin(x)
                    func_name, deriv_name = "cos(x)", "-sin(x)"
                else:
                    f_x = math.tan(x)
                    derivative = 1 / (math.cos(x) ** 2)
                    func_name, deriv_name = "tan(x)", "sec²(x)"
                result = f"f(x) = {func_name} = {f_x:.4f}\nf'(x) = {deriv_name} = {derivative:.4f}"
            elif func_type == "exponential":
                f_x = math.exp(x)
                result = f"f(x) = e^{x} = {f_x:.4f}\nf'(x) = e^{x} = {f_x:.4f}"
            elif func_type == "logarithmic":
                if x <= 0:
                    messagebox.showerror("Error", "x must be positive for ln(x)")
                    return
                f_x = math.log(x)
                derivative = 1 / x
                result = f"f(x) = ln({x}) = {f_x:.4f}\nf'(x) = 1/{x} = {derivative:.4f}"
            
            self.display_result(self.deriv_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def calc_integral(self):
        try:
            a = float(self.integ_lower.get())
            b = float(self.integ_upper.get())
            n = int(self.integ_intervals.get())
            
            if n <= 0:
                messagebox.showerror("Error", "Number of intervals must be positive")
                return
            
            func_type = self.integ_func_type.get()
            h = (b - a) / n
            
            def f(x):
                if func_type == "polynomial":
                    coeff = float(self.integ_a.get())
                    power = float(self.integ_n.get())
                    return coeff * (x ** power)
                elif func_type == "trigonometric":
                    return math.sin(x)
                elif func_type == "exponential":
                    return math.exp(x)
            
            integral = f(a) + f(b)
            for i in range(1, n):
                x_i = a + i * h
                integral += 2 * f(x_i)
            integral *= h / 2
            
            analytical_text = ""
            if func_type == "polynomial":
                coeff = float(self.integ_a.get())
                power = float(self.integ_n.get())
                if power != -1:
                    upper_val = coeff * (b ** (power + 1)) / (power + 1)
                    lower_val = coeff * (a ** (power + 1)) / (power + 1)
                    analytical = upper_val - lower_val
                    analytical_text = f"\nAnalytical: {analytical:.6f}"
            
            result = f"∫f(x)dx from {a} to {b} = {integral:.6f}{analytical_text}"
            self.display_result(self.integ_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_statistics(self):
        try:
            data_str = self.stat_data.get("1.0", tk.END)
            data = [float(x.strip()) for x in data_str.split(',') if x.strip()]
            
            if not data:
                messagebox.showerror("Error", "Please enter at least one data value")
                return
            
            n = len(data)
            mean = sum(data) / n
            sorted_data = sorted(data)
            median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 if n % 2 == 0 else sorted_data[n//2]
            
            frequency = Counter(data)
            max_freq = max(frequency.values())
            modes = [k for k, v in frequency.items() if v == max_freq]
            mode_str = ', '.join([str(m) for m in modes])
            
            variance = sum((x - mean) ** 2 for x in data) / n
            std_dev = math.sqrt(variance)
            data_range = max(data) - min(data)
            
            result = f"Data Analysis Results:\n{'='*40}\n"
            result += f"Number of values (n): {n}\n"
            result += f"Sum: {sum(data):.4f}\n"
            result += f"Mean (Average): {mean:.4f}\n"
            result += f"Median: {median:.4f}\n"
            result += f"Mode: {mode_str}\n"
            result += f"Variance (σ²): {variance:.4f}\n"
            result += f"Standard Deviation (σ): {std_dev:.4f}\n"
            result += f"Range: {data_range:.4f}\n"
            result += f"Minimum: {min(data):.4f}\n"
            result += f"Maximum: {max(data):.4f}"
            
            self.display_result(self.stat_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers separated by commas")
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def calc_probability(self):
        try:
            calc = self.prob_type.get()
            
            if calc == "factorial":
                n = int(self.prob_n.get())
                if n < 0:
                    messagebox.showerror("Error", "Factorial not defined for negative numbers")
                    return
                result = f"{n}! = {self.factorial(n)}"
                
            elif calc in ["permutation", "combination"]:
                n = int(self.prob_n.get())
                r = int(self.prob_r.get())
                
                if n < 0 or r < 0 or r > n:
                    messagebox.showerror("Error", "Invalid values")
                    return
                
                if calc == "permutation":
                    res = self.factorial(n) // self.factorial(n - r)
                    result = f"P({n},{r}) = {res}"
                else:
                    res = self.factorial(n) // (self.factorial(r) * self.factorial(n - r))
                    result = f"C({n},{r}) = {res}"
                    
            elif calc == "binomial":
                n = int(self.prob_n.get())
                k = int(self.prob_k.get())
                p = float(self.prob_p.get())
                
                if n < 0 or k < 0 or k > n or p < 0 or p > 1:
                    messagebox.showerror("Error", "Invalid values")
                    return
                
                comb = self.factorial(n) // (self.factorial(k) * self.factorial(n - k))
                probability = comb * (p ** k) * ((1 - p) ** (n - k))
                result = f"P(X={k}) = {probability:.6f} ({probability*100:.2f}%)"
            
            self.display_result(self.prob_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers")
    
    def calc_coordinate(self):
        try:
            x1 = float(self.coord_x1.get())
            y1 = float(self.coord_y1.get())
            x2 = float(self.coord_x2.get())
            y2 = float(self.coord_y2.get())
            
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            midpoint_x = (x1 + x2) / 2
            midpoint_y = (y1 + y2) / 2
            
            result = f"Distance: {distance:.2f}\nMidpoint: ({midpoint_x:.2f}, {midpoint_y:.2f})"
            self.display_result(self.coord_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_polygon(self):
        try:
            n = int(self.poly_n.get())
            s = float(self.poly_side.get())
            
            if n < 3:
                messagebox.showerror("Error", "Polygon must have at least 3 sides")
                return
            
            area = (n * s**2) / (4 * math.tan(math.pi / n))
            result = f"Area: {area:.2f} square units"
            self.display_result(self.poly_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_circle(self):
        try:
            r = float(self.circle_r.get())
            if r <= 0:
                messagebox.showerror("Error", "Radius must be positive")
                return
            
            area = math.pi * r**2
            circumference = 2 * math.pi * r
            diameter = 2 * r
            
            result = f"Area: {area:.2f}\nCircumference: {circumference:.2f}\nDiameter: {diameter:.2f}"
            self.display_result(self.circle_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_sphere(self):
        try:
            r = float(self.sphere_r.get())
            if r <= 0:
                messagebox.showerror("Error", "Radius must be positive")
                return
            
            volume = (4/3) * math.pi * r**3
            surface_area = 4 * math.pi * r**2
            
            result = f"Volume: {volume:.2f}\nSurface Area: {surface_area:.2f}"
            self.display_result(self.sphere_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_cylinder(self):
        try:
            r = float(self.cyl_r.get())
            h = float(self.cyl_h.get())
            
            if r <= 0 or h <= 0:
                messagebox.showerror("Error", "Radius and height must be positive")
                return
            
            volume = math.pi * r**2 * h
            surface_area = 2 * math.pi * r * (r + h)
            
            result = f"Volume: {volume:.2f}\nSurface Area: {surface_area:.2f}"
            self.display_result(self.cyl_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_cone(self):
        try:
            r = float(self.cone_r.get())
            h = float(self.cone_h.get())
            
            if r <= 0 or h <= 0:
                messagebox.showerror("Error", "Radius and height must be positive")
                return
            
            volume = (1/3) * math.pi * r**2 * h
            slant_height = math.sqrt(r**2 + h**2)
            surface_area = math.pi * r * (r + slant_height)
            
            result = f"Volume: {volume:.2f}\nSurface Area: {surface_area:.2f}\nSlant Height: {slant_height:.2f}"
            self.display_result(self.cone_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_gcd_lcm(self):
        try:
            num1 = int(self.gcd_num1.get())
            num2 = int(self.gcd_num2.get())
            
            if num1 <= 0 or num2 <= 0:
                messagebox.showerror("Error", "Numbers must be positive")
                return
            
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a
            
            gcd_val = gcd(num1, num2)
            lcm_val = abs(num1 * num2) // gcd_val
            
            result = f"GCD: {gcd_val}\nLCM: {lcm_val}"
            self.display_result(self.gcd_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers")
    
    def is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def calc_prime(self):
        try:
            n = int(self.prime_n.get())
            if n < 0:
                messagebox.showerror("Error", "Please enter a non-negative integer")
                return
            
            operation = self.prime_op.get()
            if operation == "check":
                if self.is_prime(n):
                    result = f"{n} is a PRIME number ✓"
                else:
                    result = f"{n} is NOT a prime number ✗"
            elif operation == "find":
                if n > 10000:
                    messagebox.showerror("Error", "Please enter a number ≤ 10000")
                    return
                primes = [i for i in range(2, n + 1) if self.is_prime(i)]
                result = f"Prime numbers up to {n}:\n{', '.join(map(str, primes))}\n\nTotal: {len(primes)} primes"
            
            self.display_result(self.prime_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
    
    def calc_fibonacci(self):
        try:
            n = int(self.fib_n.get())
            if n <= 0 or n > 100:
                messagebox.showerror("Error", "Enter number between 1 and 100")
                return
            
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[-1] + fib[-2])
            sequence = ', '.join(map(str, fib[:n]))
            
            result = f"First {n} Fibonacci numbers:\n{sequence}"
            self.display_result(self.fib_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
    
    def convert_base(self):
        try:
            decimal = int(self.base_num.get())
            if decimal < 0:
                messagebox.showerror("Error", "Please enter a non-negative integer")
                return
            
            binary = bin(decimal)[2:]
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:].upper()
            
            def convert_base_num(number, base):
                if number == 0:
                    return "0"
                digits = []
                while number > 0:
                    remainder = number % base
                    if remainder < 10:
                        digits.append(str(remainder))
                    else:
                        digits.append(chr(ord('A') + remainder - 10))
                    number //= base
                return ''.join(reversed(digits))
            
            result = f"Decimal (Base 10): {decimal}\n\n"
            result += f"Binary (Base 2): {binary}\n\n"
            result += f"Octal (Base 8): {octal}\n\n"
            result += f"Hexadecimal (Base 16): {hexadecimal}\n\n"
            
            for base in [3, 4, 5, 6, 7, 9, 12]:
                converted = convert_base_num(decimal, base)
                result += f"Base {base}: {converted}\n"
            
            self.display_result(self.base_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
    
    def calc_trigonometry(self):
        try:
            angle = float(self.trig_angle.get())
            rad = math.radians(angle)
            
            sin_val = math.sin(rad)
            cos_val = math.cos(rad)
            tan_val = math.tan(rad)
            
            result = f"sin({angle}°) = {sin_val:.6f}\ncos({angle}°) = {cos_val:.6f}\ntan({angle}°) = {tan_val:.6f}"
            self.display_result(self.trig_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_logarithm(self):
        try:
            num = float(self.log_num.get())
            base = float(self.log_base.get())
            
            if num <= 0 or base <= 0 or base == 1:
                messagebox.showerror("Error", "Invalid input")
                return
            
            result = math.log(num, base)
            text = f"log_{base}({num}) = {result:.6f}"
            self.display_result(self.log_result, text)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_exponential(self):
        try:
            calc_type = self.exp_type.get()
            
            if calc_type == "exponential":
                a = float(self.exp_base.get())
                x = float(self.exp_x.get())
                if a <= 0:
                    messagebox.showerror("Error", "Base must be positive")
                    return
                result = a ** x
                text = f"{a}^{x} = {result:.6f}"
            elif calc_type == "natural_log":
                x = float(self.exp_x.get())
                if x <= 0:
                    messagebox.showerror("Error", "Value must be positive")
                    return
                result = math.log(x)
                text = f"ln({x}) = {result:.6f}"
            elif calc_type == "log10":
                x = float(self.exp_x.get())
                if x <= 0:
                    messagebox.showerror("Error", "Value must be positive")
                    return
                result = math.log10(x)
                text = f"log10({x}) = {result:.6f}"
            
            self.display_result(self.exp_result, text)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_arithmetic_series(self):
        try:
            a = float(self.arith_a.get())
            d = float(self.arith_d.get())
            n = int(self.arith_n.get())
            
            if n <= 0:
                messagebox.showerror("Error", "n must be positive")
                return
            
            nth_term = a + (n - 1) * d
            sum_n = (n / 2) * (2 * a + (n - 1) * d)
            
            result = f"n-th term: {nth_term:.2f}\nSum of n terms: {sum_n:.2f}"
            self.display_result(self.arith_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_geometric_series(self):
        try:
            a = float(self.geo_a.get())
            r = float(self.geo_r.get())
            n = int(self.geo_n.get())
            
            if n <= 0:
                messagebox.showerror("Error", "n must be positive")
                return
            
            nth_term = a * (r ** (n - 1))
            sum_n = a * (1 - r**n) / (1 - r) if r != 1 else a * n
            
            result = f"n-th term: {nth_term:.2f}\nSum of n terms: {sum_n:.2f}"
            self.display_result(self.geo_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_vector(self):
        try:
            ax = float(self.vec_ax.get())
            ay = float(self.vec_ay.get())
            bx = float(self.vec_bx.get())
            by = float(self.vec_by.get())
            
            sum_vec = (ax + bx, ay + by)
            diff_vec = (ax - bx, ay - by)
            dot_product = ax * bx + ay * by
            mag_a = math.sqrt(ax**2 + ay**2)
            mag_b = math.sqrt(bx**2 + by**2)
            
            result = f"A + B = ({sum_vec[0]:.2f}, {sum_vec[1]:.2f})\n"
            result += f"A - B = ({diff_vec[0]:.2f}, {diff_vec[1]:.2f})\n"
            result += f"Dot Product: {dot_product:.2f}\n"
            result += f"|A| = {mag_a:.2f}\n|B| = {mag_b:.2f}"
            self.display_result(self.vec_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_complex(self, op):
        try:
            a1 = float(self.complex_a1.get())
            b1 = float(self.complex_b1.get())
            a2 = float(self.complex_a2.get())
            b2 = float(self.complex_b2.get())
            
            if op == 'add':
                real = a1 + a2
                imag = b1 + b2
                op_symbol = "+"
            else:
                real = a1*a2 - b1*b2
                imag = a1*b2 + a2*b1
                op_symbol = "×"
            
            sign = '+' if imag >= 0 else '-'
            result = f"({a1:.2f} + {b1:.2f}i) {op_symbol} ({a2:.2f} + {b2:.2f}i)\n= {real:.2f} {sign} {abs(imag):.2f}i"
            self.display_result(self.complex_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_pct_percent(self):
        try:
            value = float(self.pct_value.get())
            total = float(self.pct_total.get())
            
            if total == 0:
                messagebox.showerror("Error", "Total cannot be zero")
                return
            
            percent = (value / total) * 100
            result = f"{value} is {percent:.2f}% of {total}"
            self.display_result(self.pct_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def calc_pct_value(self):
        try:
            total = float(self.pct_total.get())
            percent = float(self.pct_percent.get())
            
            value = (percent / 100) * total
            result = f"{percent}% of {total} = {value:.2f}"
            self.display_result(self.pct_result, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathLifeGUI(root)
    root.mainloop()
