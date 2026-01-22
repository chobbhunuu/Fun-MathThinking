<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>คณิตคิดสนุก</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="game">
    <h1>🎮 คณิตคิดสนุก</h1>

    <div class="nums">
        {% for n in numbers %}
            <span class="num">{{ n }}</span>
        {% endfor %}
    </div>

    <div class="target">
        เป้าหมาย: <span id="target">{{ target }}</span>
    </div>

    <input id="expr" placeholder="เช่น (5+5)*9">
    <button onclick="send()">ส่ง</button>

    <div id="msg"></div>
</div>

<script>
function send() {
    fetch('/check', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            expr: document.getElementById('expr').value,
            target: Number(document.getElementById('target').innerText)
        })
    })
    .then(r => r.json())
    .then(d => {
        const m = document.getElementById('msg');
        if (d.error) m.innerText = "สมการผิด";
        else if (d.correct) m.innerText = "🎉 ถูกต้อง";
        else m.innerText = "❌ ได้ " + d.result;
    });
}
</script>

</body>
</html>
