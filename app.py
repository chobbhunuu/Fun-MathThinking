from flask import Flask, render_template, request, jsonify
import random, ast, operator

app = Flask(__name__)

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def safe_eval(expr):
    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.BinOp):
            return OPS[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )
        raise ValueError
    return eval_node(ast.parse(expr, mode='eval').body)

@app.route('/')
def index():
    return render_template(
        'index.html',
        numbers=[random.randint(0,9) for _ in range(5)],
        target=random.randint(9,999)
    )

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    try:
        result = safe_eval(data['expr'])
        return jsonify(correct=result == data['target'], result=result)
    except:
        return jsonify(error=True)

if __name__ == '__main__':
    app.run(debug=True)
