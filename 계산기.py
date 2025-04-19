# tkinter는 파이썬에서 GUI(그래픽 사용자 인터페이스)를 만들 때 쓰는 기본 모듈입니다.
import tkinter as tk

# 계산을 수행하는 함수입니다.
def calculate():
    try:
        # entry 위젯에서 입력된 문자열(예: "2+3*4")을 가져옵니다.
        expression = entry.get()
        
        # eval() 함수는 문자열을 그대로 계산해주는 파이썬 내장 함수입니다.
        # 예: eval("2+3*4") → 14
        result = eval(expression)
        
        # 계산 전에 입력창을 비웁니다.
        entry.delete(0, tk.END)
        
        # 계산 결과를 문자열로 바꿔서 입력창에 표시합니다.
        entry.insert(0, str(result))
    
    except Exception as e:
        # 만약 수식이 잘못되었거나 오류가 발생했다면,
        # 입력창을 비우고 "오류"라고 표시해줍니다.
        entry.delete(0, tk.END)
        entry.insert(0, "오류")

# tkinter로 새 창(윈도우)을 하나 생성합니다.
root = tk.Tk()

# 창의 제목을 설정합니다.
root.title("초간단 계산기")

# 입력창(Entry 위젯)을 생성합니다.
# 사용자가 수식을 입력하거나 결과가 표시될 공간입니다.
entry = tk.Entry(
    root,           # 부모 위젯은 root (창 전체)
    width=25,       # 입력창 너비 (문자 수 기준)
    font=("Arial", 14),  # 글씨 크기와 폰트 설정
    justify="right"     # 입력된 글자가 오른쪽 정렬되도록 설정
)
# 입력창을 그리드(행/열) 레이아웃에 배치합니다.
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# row=0 → 첫 번째 줄, columnspan=4 → 4칸 차지, 패딩은 여백

# 계산기에 들어갈 버튼 텍스트들을 리스트로 만듭니다.
# 이 순서대로 버튼이 생성되고 배치될 예정입니다.
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# 버튼을 하나씩 생성하면서 화면에 배치합니다.
row = 1  # 버튼은 첫 번째 줄(entry) 밑인 1번 행부터 시작
col = 0  # 열은 0부터 시작

for btn_text in buttons:
    
    # 각 버튼이 눌렸을 때 어떤 동작을 할지 결정하는 함수입니다.
    def make_command(x=btn_text):  # 기본값 설정으로 반복문 문제 방지
        if x == "=":
            return calculate  # '=' 버튼이면 계산 함수 연결
        elif x == "C":
            return lambda: entry.delete(0, tk.END)  # 'C'는 입력창 비우기
        else:
            # 숫자나 연산자는 입력창에 해당 글자를 추가합니다.
            return lambda: entry.insert(tk.END, x)

    # 버튼 위젯을 생성합니다.
    btn = tk.Button(
        root,                  # 부모 위젯은 root
        text=btn_text,         # 버튼에 표시될 글자
        width=5, height=2,     # 버튼 크기
        font=("Arial", 12),    # 버튼 글자 크기
        command=make_command() # 눌렀을 때 실행할 함수
    )

    # 버튼을 그리드(행/열) 위치에 배치합니다.
    btn.grid(row=row, column=col, padx=5, pady=5)

    # 버튼을 오른쪽으로 이동시키기 위해 열 값 증가
    col += 1
    # 만약 열이 4를 넘으면 다음 줄(row)로 내려가고 열(col)은 0으로 초기화
    if col > 3:
        col = 0
        row += 1

# tkinter의 메인 루프를 실행합니다.
# 이게 있어야 창이 계속 유지되면서 버튼을 누를 수 있습니다.
root.mainloop()
