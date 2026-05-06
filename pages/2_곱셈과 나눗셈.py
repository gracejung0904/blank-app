import streamlit as st

st.title("📗 곱셈과 나눗셈 학습지")

st.markdown(
    """
    ### 1. 곱셈과 나눗셈이 뭐예요?

    - **곱셈(×)**은 같은 수를 여러 번 더하는 계산이에요.
      예를 들어 3 × 4는 3을 4번 더한 값으로 12가 됩니다.
    - **나눗셈(÷)**은 수를 여러 조각으로 나누는 계산이에요.
      예를 들어 12 ÷ 3은 12를 3개의 같은 그룹으로 나누면 각 그룹에 4가 들어가요.

    **중요한 점**
    - 곱셈은 "몇 번 더하는가"를 쉽게 계산합니다.
    - 나눗셈은 "몇 개씩 나누는가"를 계산합니다.
    """
)

st.header("📌 예시 문제")
with st.expander("곱셈 예시 보기"):
    st.write("2 × 3 = 6")
    st.write("4 × 5 = 20")
    st.write("7 × 2 = 14")

with st.expander("나눗셈 예시 보기"):
    st.write("12 ÷ 3 = 4")
    st.write("15 ÷ 5 = 3")
    st.write("18 ÷ 6 = 3")

st.markdown(
    """
    ### 2. 곱셈 문제를 풀어요
    아래 문제를 읽고 답을 입력하세요.
    """
)

multiplication_questions = [
    (3, 2),
    (5, 4),
    (6, 3),
    (7, 1),
    (4, 6),
]

mult_answers = []
for i, (a, b) in enumerate(multiplication_questions, start=1):
    answer = st.number_input(f"{i}. {a} × {b} =", min_value=0, max_value=200, value=0, key=f"mul_{i}")
    mult_answers.append(answer)

st.markdown("---")

st.markdown(
    """
    ### 3. 나눗셈 문제를 풀어요
    아래 문제를 읽고 답을 입력하세요.
    """
)

division_questions = [
    (12, 3),
    (20, 5),
    (15, 3),
    (18, 6),
    (9, 3),
]

div_answers = []
for i, (a, b) in enumerate(division_questions, start=1):
    answer = st.number_input(f"{i}. {a} ÷ {b} =", min_value=0, max_value=200, value=0, key=f"div_{i}")
    div_answers.append(answer)

st.markdown("---")

st.markdown("### 4. 정답 확인하기")
if st.button("정답 확인"):
    mul_correct = [a * b for a, b in multiplication_questions]
    div_correct = [a // b for a, b in division_questions]

    st.write("#### 곱셈 정답")
    for i, correct in enumerate(mul_correct, start=1):
        user = mult_answers[i - 1]
        result = "✅ 맞았어요" if user == correct else f"❌ 틀렸어요 (정답: {correct})"
        st.write(f"{i}. {multiplication_questions[i-1][0]} × {multiplication_questions[i-1][1]} = {user} → {result}")

    st.write("#### 나눗셈 정답")
    for i, correct in enumerate(div_correct, start=1):
        user = div_answers[i - 1]
        result = "✅ 맞았어요" if user == correct else f"❌ 틀렸어요 (정답: {correct})"
        st.write(f"{i}. {division_questions[i-1][0]} ÷ {division_questions[i-1][1]} = {user} → {result}")

st.markdown("---")

st.header("✏️ 추가 연습")
st.write("직접 문제를 만들어 보고 풀어보세요.")
for i in range(1, 4):
    st.text_input(f"연습 문제 {i}", value="", key=f"free2_{i}")

st.markdown(
    """
    ### 5. 공부 꿀팁
    - 곱셈은 덧셈을 빠르게 계산하는 방법이에요.
    - 나눗셈은 결과가 나눠지는 수보다 작거나 같아요.
    - 계산할 때 천천히 읽고, 곱셈과 나눗셈 기호를 꼭 확인하세요.
    """
)
