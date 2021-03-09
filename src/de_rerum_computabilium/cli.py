import click
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

console = Console()

RECONSTRUCTIONS = {
    "babylonian-sqrt": {
        "title": "Babylonian Square Root (YBC 7289)",
        "era": "Old Babylonian (c. 1800-1600 BC)",
        "discipline": "Arithmetic / Geometry",
        "module": "de_rerum_computabilium.reconstructions.babylonian_sqrt_ybc7289.algorithm"
    },
    "napier-logarithm": {
        "title": "Napier's Logarithm Table Construction",
        "era": "Early Modern (1614)",
        "discipline": "Astronomy / Navigation",
        "module": "de_rerum_computabilium.reconstructions.napier_logarithms.algorithm"
    },
    "jiuzhang-cuberoot": {
        "title": "Ancient Chinese Cube Root (Kai Lifang Shu)",
        "era": "Han Dynasty China (c. 1st century CE)",
        "discipline": "Arithmetic / Algebra",
        "module": "de_rerum_computabilium.reconstructions.jiuzhang_suanshu_cuberoot.algorithm"
    },
    "euclid-gcd": {
        "title": "Euclidean Algorithm (Anthyphaeresis)",
        "era": "Hellenistic Greece (c. 300 BC)",
        "discipline": "Arithmetic",
        "module": "de_rerum_computabilium.reconstructions.euclid_gcd.algorithm"
    },
    "babbage-engine": {
        "title": "Babbage Difference Engine No. 2",
        "era": "Victorian England (1847-1849)",
        "discipline": "Mechanical Tabulation",
        "module": "de_rerum_computabilium.reconstructions.babbage_difference_engine.algorithm"
    },
    "prosthaphaeresis": {
        "title": "Prosthaphaeresis (Multiplication via Trigonometry)",
        "era": "Late Renaissance (c. 1580s)",
        "discipline": "Astronomy",
        "module": "de_rerum_computabilium.reconstructions.prosthaphaeresis.algorithm"
    },
    "ptolemy-chords": {
        "title": "Ptolemy's Table of Chords",
        "era": "Hellenistic Astronomy (c. 150 AD)",
        "discipline": "Astronomy / Geometry",
        "module": "de_rerum_computabilium.reconstructions.ptolemy_chords.algorithm"
    },
    "runge-kutta": {
        "title": "Kutta's 1901 Worksheet (RK4)",
        "era": "Early 20th Century (1901)",
        "discipline": "Numerical Analysis / Differential Equations",
        "module": "de_rerum_computabilium.reconstructions.runge_kutta.algorithm"
    },
    "egyptian-multiplication": {
        "title": "Egyptian Multiplication",
        "era": "Ancient Egypt (c. 1550 BC)",
        "discipline": "Arithmetic",
        "module": "de_rerum_computabilium.reconstructions.egyptian_multiplication.algorithm"
    },
    "alkhwarizmi-quadratic": {
        "title": "Al-Khwarizmi Completing the Square",
        "era": "Islamic Golden Age (c. 820 AD)",
        "discipline": "Algebra",
        "module": "de_rerum_computabilium.reconstructions.alkhwarizmi_quadratic.algorithm"
    },
    "suanpan-addition": {
        "title": "Suanpan (Abacus) Addition",
        "era": "Ming Dynasty China (c. 14th Century)",
        "discipline": "Mechanical Calculation",
        "module": "de_rerum_computabilium.reconstructions.suanpan_addition.algorithm"
    },
    "briggs-logarithm": {
        "title": "Briggs' Common Logarithms",
        "era": "Early Modern (1624)",
        "discipline": "Arithmetic / Astronomy",
        "module": "de_rerum_computabilium.reconstructions.briggs_logarithm.algorithm"
    },
    "galton-quincunx": {
        "title": "Galton's Quincunx (Galton Board)",
        "era": "Victorian England (1873)",
        "discipline": "Statistics / Probability",
        "module": "de_rerum_computabilium.reconstructions.galton_quincunx.algorithm"
    },
    "slide-rule": {
        "title": "Slide Rule Multiplication",
        "era": "17th-20th Century",
        "discipline": "Mechanical Calculation",
        "module": "de_rerum_computabilium.reconstructions.slide_rule.algorithm"
    },
    "merton-mean-speed": {
        "title": "Merton Mean Speed Theorem",
        "era": "High Middle Ages (1330s)",
        "discipline": "Kinematics",
        "module": "de_rerum_computabilium.reconstructions.merton_mean_speed.algorithm"
    },
    "prony-cadastre": {
        "title": "Gaspard de Prony's Cadastre (Tier 3)",
        "era": "French Revolution (1790s)",
        "discipline": "Human Computing Factory",
        "module": "de_rerum_computabilium.reconstructions.prony_cadastre.algorithm"
    },
    "shanks-pi": {
        "title": "William Shanks' Pi (707 digits)",
        "era": "Victorian England (1873)",
        "discipline": "Number Theory",
        "module": "de_rerum_computabilium.reconstructions.shanks_pi.algorithm"
    },
    "newton-algebraic": {
        "title": "Newton's Algebraic Substitution",
        "era": "Early Modern (1669)",
        "discipline": "Calculus / Algebra",
        "module": "de_rerum_computabilium.reconstructions.newton_algebraic.algorithm"
    },
    "madhava-sine": {
        "title": "Madhava Sine Series",
        "era": "14th-Century Kerala (India)",
        "discipline": "Trigonometry / Infinite Series",
        "module": "de_rerum_computabilium.reconstructions.madhava_sine.algorithm"
    },
    "archimedes-pi": {
        "title": "Archimedes Pi (Method of Exhaustion)",
        "era": "Hellenistic Greece (c. 250 BC)",
        "discipline": "Geometry",
        "module": "de_rerum_computabilium.reconstructions.archimedes_pi.algorithm"
    }
}

@click.group()
def main():
    """DE RERUM COMPUTABILIUM: An executable history of calculation."""
    pass

@main.command()
def list():
    """List available historical reconstructions."""
    table = Table(title="Corpus of Reconstructions", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="white")
    table.add_column("Historical Era", style="green")
    table.add_column("Discipline", style="yellow")
    
    for rid, info in RECONSTRUCTIONS.items():
        table.add_row(rid, info["title"], info["era"], info["discipline"])
        
    console.print(table)

@main.command()
@click.argument('reconstruction_id')
def show(reconstruction_id):
    """Show details for a specific reconstruction."""
    if reconstruction_id not in RECONSTRUCTIONS:
        console.print(f"[red]Error: Reconstruction '{reconstruction_id}' not found.[/red]")
        return
        
    info = RECONSTRUCTIONS[reconstruction_id]
    console.print(f"\n[bold]{info['title']}[/bold]")
    console.print(f"Era: {info['era']}")
    console.print(f"Discipline: {info['discipline']}")
    console.print("\nTo run this reconstruction, use: [bold]drc run {reconstruction_id}[/bold]\n")

@main.command()
@click.argument('reconstruction_id')
@click.option('--mode', default='historical', help='Execution mode (historical, modern, trace)')
@click.option('--worksheet', is_flag=True, help='Generate a printable worksheet')
def run(reconstruction_id, mode, worksheet):
    """Run a historical reconstruction."""
    if reconstruction_id not in RECONSTRUCTIONS:
        console.print(f"[red]Error: Reconstruction '{reconstruction_id}' not found.[/red]")
        return
        
    trace = None
    
    if reconstruction_id == "babylonian-sqrt":
        from de_rerum_computabilium.reconstructions.babylonian_sqrt_ybc7289.algorithm import babylonian_sqrt
        from fractions import Fraction
        
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']}...[/bold cyan]")
        trace = babylonian_sqrt(2, Fraction(3, 2), iterations=2)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Decimal): {float(trace.steps[-1].result):.7f}")
            console.print(f"Result (Sexagesimal): {trace.steps[-1].precision}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "napier-logarithm":
        from de_rerum_computabilium.reconstructions.napier_logarithms.algorithm import NapierTableBuilder
        
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']}...[/bold cyan]")
        builder = NapierTableBuilder()
        builder.build_first_table()
        trace = builder.trace
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Built First Table (101 values).")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "jiuzhang-cuberoot":
        from de_rerum_computabilium.reconstructions.jiuzhang_suanshu_cuberoot.algorithm import chinese_cube_root
        
        N = click.prompt("Enter an integer to find its cube root", type=int, default=1860872)
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']} for {N}...[/bold cyan]")
        
        trace = chinese_cube_root(N)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Root): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")

    elif reconstruction_id == "euclid-gcd":
        from de_rerum_computabilium.reconstructions.euclid_gcd.algorithm import euclidean_algorithm_historical
        
        a = click.prompt("Enter first integer (magnitude)", type=int, default=1071)
        b = click.prompt("Enter second integer (magnitude)", type=int, default=462)
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']} for {a} and {b}...[/bold cyan]")
        
        trace = euclidean_algorithm_historical(a, b)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Greatest Common Measure): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")

    elif reconstruction_id == "babbage-engine":
        from de_rerum_computabilium.reconstructions.babbage_difference_engine.algorithm import babbage_engine
        
        cycles = click.prompt("Enter number of cycles to run", type=int, default=5)
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']}...[/bold cyan]")
        
        trace = babbage_engine(cycles, 41, 2, 2)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Final Result: {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "prosthaphaeresis":
        from de_rerum_computabilium.reconstructions.prosthaphaeresis.algorithm import ProsthaphaeresisComputer
        
        x = click.prompt("Enter first number to multiply", type=float, default=314.15)
        y = click.prompt("Enter second number to multiply", type=float, default=271.82)
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']}...[/bold cyan]")
        
        computer = ProsthaphaeresisComputer()
        trace = computer.multiply(x, y)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result: {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "ptolemy-chords":
        from de_rerum_computabilium.reconstructions.ptolemy_chords.algorithm import ptolemy_chords_reconstruction
        
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']}...[/bold cyan]")
        
        trace = ptolemy_chords_reconstruction()
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Final Interpolation (Crd 1): {trace.steps[-1].precision}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "runge-kutta":
        from de_rerum_computabilium.reconstructions.runge_kutta.algorithm import runge_kutta_historical
        
        console.print(f"[bold cyan]Running {RECONSTRUCTIONS[reconstruction_id]['title']} (dy/dx = y)...[/bold cyan]")
        
        trace = runge_kutta_historical(1.0, 0.1)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (y at next step): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")

    elif reconstruction_id == "egyptian-multiplication":
        from de_rerum_computabilium.reconstructions.egyptian_multiplication.algorithm import egyptian_multiplication
        a = click.prompt("Enter first number", type=int, default=23)
        b = click.prompt("Enter second number", type=int, default=15)
        trace = egyptian_multiplication(a, b)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result: {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")

    elif reconstruction_id == "alkhwarizmi-quadratic":
        from de_rerum_computabilium.reconstructions.alkhwarizmi_quadratic.algorithm import al_khwarizmi_quadratic
        p = click.prompt("Enter p for x^2 + px = q", type=float, default=10.0)
        q = click.prompt("Enter q", type=float, default=39.0)
        trace = al_khwarizmi_quadratic(p, q)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Root): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "suanpan-addition":
        from de_rerum_computabilium.reconstructions.suanpan_addition.algorithm import suanpan_addition
        a = click.prompt("Enter first number", type=int, default=274)
        b = click.prompt("Enter second number", type=int, default=189)
        trace = suanpan_addition(a, b)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result: {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "briggs-logarithm":
        from de_rerum_computabilium.reconstructions.briggs_logarithm.algorithm import briggs_logarithm
        x = click.prompt("Enter x to find log10(x)", type=float, default=2.0)
        trace = briggs_logarithm(x)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result: {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "galton-quincunx":
        from de_rerum_computabilium.reconstructions.galton_quincunx.algorithm import galton_quincunx
        beans = click.prompt("Enter number of beans", type=int, default=100)
        rows = click.prompt("Enter number of rows", type=int, default=10)
        trace = galton_quincunx(beans, rows)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Distribution): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "slide-rule":
        from de_rerum_computabilium.reconstructions.slide_rule.algorithm import slide_rule_multiply
        a = click.prompt("Enter first number", type=float, default=2.5)
        b = click.prompt("Enter second number", type=float, default=3.2)
        trace = slide_rule_multiply(a, b)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result: {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "merton-mean-speed":
        from de_rerum_computabilium.reconstructions.merton_mean_speed.algorithm import merton_mean_speed
        vi = click.prompt("Enter initial velocity", type=float, default=0.0)
        vf = click.prompt("Enter final velocity", type=float, default=10.0)
        t = click.prompt("Enter time", type=float, default=5.0)
        trace = merton_mean_speed(vi, vf, t)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Distance): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "prony-cadastre":
        from de_rerum_computabilium.reconstructions.prony_cadastre.algorithm import prony_cadastre_tier3
        trace = prony_cadastre_tier3(0.0, 0.01, -0.0001, 0.000001, 5)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Sequence): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "shanks-pi":
        from de_rerum_computabilium.reconstructions.shanks_pi.algorithm import shanks_pi
        digits = click.prompt("Enter digits of Pi to calculate", type=int, default=20)
        trace = shanks_pi(digits)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result: {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")
            
    elif reconstruction_id == "newton-algebraic":
        from de_rerum_computabilium.reconstructions.newton_algebraic.algorithm import newton_algebraic_method
        trace = newton_algebraic_method(2.0, 3)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Root approx): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")

    elif reconstruction_id == "madhava-sine":
        from de_rerum_computabilium.reconstructions.madhava_sine.algorithm import madhava_sine
        arc = click.prompt("Enter arc in minutes (e.g. 1800 for 30 deg)", type=float, default=1800.0)
        trace = madhava_sine(arc)
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (R*sin): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")

    elif reconstruction_id == "archimedes-pi":
        from de_rerum_computabilium.reconstructions.archimedes_pi.algorithm import archimedes_pi
        trace = archimedes_pi()
        if mode == 'trace':
            console.print(str(trace))
        else:
            console.print(f"Result (Inscribed 96-gon Ratio): {trace.steps[-1].result}")
            console.print(f"Historical labor cost: {trace.total_cost()} operations")

    if worksheet and trace is not None:
        from de_rerum_computabilium.core.worksheet import generate_worksheet
        filename = f"{reconstruction_id}_worksheet.md"
        generate_worksheet(trace, filename)
        console.print(f"[bold green]Worksheet generated at {filename}[/bold green]")

if __name__ == "__main__":
    main()
