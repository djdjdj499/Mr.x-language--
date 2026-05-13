from flask import Flask, request, render_template_string

app = Flask(__name__)

# =========================================
# Mr.X Compiler
# =========================================

def compile_mrx(code):

    html = ""

    lines = code.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # عنوان
        if line.startswith("عنوان"):

            try:
                text = line.split('"')[1]

                html += f'''
                <h1 style="
                font-size:55px;
                margin-bottom:20px;
                color:#00ffe0;
                text-shadow:0 0 20px #00ffe0;
                ">
                {text}
                </h1>
                '''
            except:
                html += "<p style='color:red;'>خطأ في عنوان</p>"

        # نص
        elif line.startswith("نص"):

            try:
                text = line.split('"')[1]

                html += f'''
                <p style="
                font-size:22px;
                color:#cccccc;
                margin-bottom:20px;
                ">
                {text}
                </p>
                '''
            except:
                html += "<p style='color:red;'>خطأ في نص</p>"

        # زر
        elif line.startswith("زر"):

            try:
                text = line.split('"')[1]

                html += f'''
                <button style="
                padding:16px 35px;
                border:none;
                border-radius:14px;
                font-size:18px;
                cursor:pointer;
                background:linear-gradient(45deg,#00ffe0,#0077ff);
                color:white;
                margin:10px;
                box-shadow:0 0 20px rgba(0,255,224,.4);
                transition:.3s;
                ">
                {text}
                </button>
                '''
            except:
                html += "<p style='color:red;'>خطأ في زر</p>"

        # صورة
        elif line.startswith("صورة"):

            try:
                text = line.split('"')[1]

                html += f'''
                <img src="{text}" style="
                width:320px;
                border-radius:20px;
                margin:20px;
                border:2px solid #00ffe0;
                box-shadow:0 0 25px rgba(0,255,224,.4);
                ">
                '''
            except:
                html += "<p style='color:red;'>خطأ في صورة</p>"

        # حقل
        elif line.startswith("حقل"):

            try:
                text = line.split('"')[1]

                html += f'''
                <input placeholder="{text}" style="
                padding:15px;
                width:320px;
                border:none;
                border-radius:12px;
                margin:10px;
                font-size:18px;
                background:#111827;
                color:white;
                border:1px solid #00ffe0;
                ">
                '''
            except:
                html += "<p style='color:red;'>خطأ في حقل</p>"

        # قول
        elif line.startswith("قول"):

            try:
                text = line.split('"')[1]

                html += f'''
                <div style="
                margin:15px;
                font-size:22px;
                color:#00ff99;
                ">
                {text}
                </div>
                '''
            except:
                html += "<p style='color:red;'>خطأ في قول</p>"

    return html

# =========================================
# Main Page
# =========================================

@app.route("/", methods=["GET", "POST"])

def home():

    default_code = '''عنوان "Mr.X"

نص "لغة برمجة عربية مستقبلية"

زر "ابدأ"

حقل "اسمك"
'''

    code = default_code

    result = compile_mrx(default_code)

    if request.method == "POST":

        code = request.form.get("code", "")

        result = compile_mrx(code)

    page = f'''

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>Mr.X Playground</title>

</head>

<body style="
margin:0;
background:#050816;
color:white;
font-family:sans-serif;
display:flex;
height:100vh;
overflow:hidden;
">

<!-- Sidebar -->

<div style="
width:320px;
background:#0b1020;
padding:20px;
overflow:auto;
border-right:1px solid #1f2937;
box-shadow:0 0 20px rgba(0,0,0,.5);
">

<h1 style="
color:#00ffe0;
font-size:40px;
margin-bottom:5px;
text-shadow:0 0 20px #00ffe0;
">
Mr.X
</h1>

<p style="color:#94a3b8;">
Arabic Programming Language
</p>

<hr style="border-color:#1f2937;">

<h2 style="color:#00ffe0;">الأوامر</h2>

<pre style="color:#00ff99;">
عنوان "Coffee"

نص "أفضل قهوة"

زر "اطلب الآن"

صورة "coffee.jpg"

حقل "اسمك"

قول "hello"
</pre>

<hr style="border-color:#1f2937;">

<h2 style="color:#00ffe0;">Official</h2>

<p>Demo Version</p>

<p>
<a href="https://github.com/djdjdj499/Mr.x-language--.git"
target="_blank"
style="color:#00ffe0;">
GitHub Repository
</a>
</p>

<p>
01220940962
</p>

<hr style="border-color:#1f2937;">

<h2 style="color:#00ffe0;">Run On Linux / Termux</h2>

<pre style="color:#00ff99;">
pkg update -y
pkg upgrade -y

pkg install python git clang llvm nodejs -y

pip install flask lark llvmlite

git clone https://github.com/djdjdj499/Mr.x-language--.git

cd Mr.x-language--/mrx/playground

python app.py
</pre>

</div>

<!-- Main -->

<div style="
flex:1;
display:flex;
flex-direction:column;
overflow:hidden;
">

<!-- Topbar -->

<div style="
padding:20px;
background:#0b1020;
border-bottom:1px solid #1f2937;
display:flex;
align-items:center;
justify-content:space-between;
">

<h1 style="margin:0;color:#00ffe0;">
Mr.X Playground
</h1>

<div style="
background:#111827;
padding:10px 20px;
border-radius:12px;
color:#00ff99;
font-size:14px;
">
LIVE DEMO
</div>

</div>

<!-- Content -->

<div style="
display:flex;
flex:1;
overflow:hidden;
">

<!-- Editor -->

<div style="
width:50%;
padding:20px;
overflow:auto;
background:#050816;
">

<h2 style="color:#00ffe0;">
Editor
</h2>

<form method="POST">

<textarea
name="code"
style="
width:100%;
height:72vh;
background:#0f172a;
color:#00ff99;
font-size:18px;
padding:20px;
border:none;
border-radius:20px;
outline:none;
font-family:monospace;
box-shadow:0 0 20px rgba(0,255,224,.1);
">{code}</textarea>

<br><br>

<button type="submit"
style="
padding:16px 35px;
background:linear-gradient(45deg,#00ffe0,#0077ff);
color:white;
border:none;
border-radius:14px;
font-size:18px;
cursor:pointer;
box-shadow:0 0 20px rgba(0,255,224,.4);
">
Compile
</button>

</form>

</div>

<!-- Preview -->

<div style="
width:50%;
padding:20px;
background:#020617;
overflow:auto;
border-left:1px solid #1f2937;
">

<h2 style="color:#00ffe0;">
Preview
</h2>

<div style="
background:#0f172a;
padding:40px;
border-radius:24px;
min-height:72vh;
text-align:center;
box-shadow:0 0 30px rgba(0,255,224,.1);
">

{result}

</div>

</div>

</div>

</div>

</body>

</html>

'''

    return render_template_string(page)

# =========================================
# Run Server
# =========================================

app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)
