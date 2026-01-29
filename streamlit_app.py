import streamlit as st
import random, ast, operator

st.set_page_config(page_title="คณิตคิดสนุก")

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

st.title("🎯 เกมคณิตคิดสนุก🫣😽")

# สุ่มเลขครั้งแรก
if "numbers" not in st.session_state:
    st.session_state.numbers = [random.randint(1,9) for _ in range(5)]
    st.session_state.target = random.randint(9,50)

numbers = st.session_state.numbers
target = st.session_state.target

st.write("🔢 ตัวเลขที่ได้:", numbers)
st.write("🎯 เป้าหมาย🙌:", target)

expr = st.text_input(
    "พิมพ์วิธีคิดของคุณ (เช่น (1+2)*3 ):"
)

if st.button("ตรวจคำตอบ"):
    try:
        result = safe_eval(expr)
        if result == target:
            st.success(f"ถูกต้อง 🎉 ผลลัพธ์ = {result}")
        else:
            st.error(f"ยังไม่ถูก ❌ ได้ {result}")
    except:
        st.warning("รูปแบบสมการไม่ถูกต้อง")

if st.button("สุ่มโจทย์ใหม่"):
    st.session_state.numbers = [random.randint(1,9) for _ in range(5)]
    st.session_state.target = random.randint(9,50)
    st.experimental_rerun()



