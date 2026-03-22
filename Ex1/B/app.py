from flask import Flask, render_template, request

app = Flask(__name__)

def primitive_roots(p):
    roots = []
    full_tables = {}

    for g in range(2, p):
        values = set()
        table = []

        for k in range(1, p):
            val = pow(g, k, p)
            table.append((k, val))
            values.add(val)

        if len(values) == p - 1:
            roots.append(g)
            full_tables[g] = table

    return roots, full_tables


@app.route("/", methods=["GET", "POST"])
def home():
    p = None
    roots = []
    tables = {}

    if request.method == "POST":
        p = int(request.form["prime"])
        roots, tables = primitive_roots(p)

    return render_template("index.html", p=p, roots=roots, tables=tables)


if __name__ == "__main__":
    app.run(debug=True)
